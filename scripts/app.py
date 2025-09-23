import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
from collections import defaultdict
import datetime

# =========================
# 1) ARQUIVOS CSV
# =========================
books_csv = 'BX_Books.csv'
ratings_csv = 'BX-Book-Ratings.csv'
users_csv = 'BX-Users.csv'

# =========================
# 2) LEITURA DOS DADOS
# =========================
print("Lendo arquivos CSV...")
books = pd.read_csv(
    books_csv, sep=';', encoding='latin-1',
    names=['ISBN', 'Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher', 'Image-URL-S', 'Image-URL-M', 'Image-URL-L'],
    header=None, on_bad_lines='skip', dtype={'ISBN': str, 'Year-Of-Publication': str}
)
ratings = pd.read_csv(
    ratings_csv, sep=';', encoding='latin-1',
    names=['User-ID', 'ISBN', 'Book-Rating'],
    header=None, on_bad_lines='skip', dtype={'User-ID': str, 'ISBN': str, 'Book-Rating': str}
)
users = pd.read_csv(
    users_csv, sep=';', encoding='latin-1',
    names=['User-ID', 'Location', 'Age'],
    header=None, on_bad_lines='skip', dtype={'User-ID': str, 'Location': str, 'Age': str}
)

# =========================
# 3) LIMPEZA DE DADOS
# =========================
print("\nIniciando a limpeza dos dados...")

# --- Limpeza de Tipos e Nulos ---
print(f"Formato original de 'ratings': {ratings.shape}")
ratings['Book-Rating'] = pd.to_numeric(ratings['Book-Rating'], errors='coerce')
users['Age'] = pd.to_numeric(users['Age'], errors='coerce')
books['Year-Of-Publication'] = pd.to_numeric(books['Year-Of-Publication'], errors='coerce')

# Remove linhas onde a conversão para número falhou ou a nota é zero (considerando apenas avaliações explícitas > 0)
ratings = ratings.dropna(subset=['Book-Rating'])
ratings = ratings[ratings['Book-Rating'] > 0]
print(f"Formato de 'ratings' após remover nulos e notas zero: {ratings.shape}")

# --- Tratamento de Dados Inválidos (Outliers) ---
# Idade: Mantém apenas idades entre 5 e 100 anos.
users.loc[(users.Age > 100) | (users.Age < 5), 'Age'] = np.nan

# Ano de Publicação: Mantém apenas anos realistas.
current_year = datetime.datetime.now().year
books.loc[(books['Year-Of-Publication'] > current_year) | (books['Year-Of-Publication'] == 0), 'Year-Of-Publication'] = np.nan

print("Limpeza de dados concluída.")

# =========================
# 4) ANÁLISE EXPLORATÓRIA DE DADOS (EDA)
# =========================
print("\nIniciando a Análise Exploratória de Dados (EDA)...")
# Para a análise, vamos juntar os dataframes
data_analise = ratings.merge(users, on='User-ID', how='left').merge(books, on='ISBN', how='left')

# --- Gráfico 1: Distribuição das Avaliações dos Livros ---
plt.figure(figsize=(10, 6))
sns.countplot(x='Book-Rating', data=data_analise, palette='viridis')
plt.title('Distribuição das Avaliações dos Livros', fontsize=15)
plt.xlabel('Avaliação')
plt.ylabel('Contagem')
plt.show()
print("Insight: A maioria das avaliações são altas (7 a 10), mostrando um viés positivo dos usuários ao avaliar.")

# --- Gráfico 2: Distribuição da Idade dos Usuários ---
plt.figure(figsize=(10, 6))
sns.histplot(data_analise['Age'].dropna(), bins=30, kde=True)
plt.title('Distribuição da Idade dos Usuários', fontsize=15)
plt.xlabel('Idade')
plt.ylabel('Contagem')
plt.show()
print("Insight: O público principal do dataset está na faixa de 20 a 40 anos.")

# --- Gráfico 3: Distribuição do Ano de Publicação dos Livros ---
plt.figure(figsize=(10, 6))
sns.histplot(data_analise['Year-Of-Publication'].dropna(), bins=40, kde=True)
plt.title('Distribuição do Ano de Publicação', fontsize=15)
plt.xlabel('Ano de Publicação')
plt.ylabel('Contagem de Livros')
plt.xlim(1950, current_year) # Foco nos anos mais relevantes
plt.show()
print("Insight: A maioria dos livros avaliados foi publicada entre 1990 e 2005.")

# --- Ranking 1: Top 10 Livros Mais Avaliados ---
print("\n--- Top 10 Livros Mais Avaliados ---")
top_10_livros = data_analise['Book-Title'].value_counts().head(10)
print(top_10_livros)

# --- Ranking 2: Top 10 Autores Mais Populares ---
print("\n--- Top 10 Autores Mais Populares ---")
top_10_autores = data_analise['Book-Author'].value_counts().head(10)
print(top_10_autores)

# =========================
# 5) PRÉ-PROCESSAMENTO PARA O MODELO DE RECOMENDAÇÃO
# =========================
print("\nIniciando o pré-processamento para o modelo...")
# Esta filtragem é crucial para reduzir a esparsidade da matriz e evitar erros de memória.
user_counts = data_analise['User-ID'].value_counts()
book_counts = data_analise['ISBN'].value_counts()
min_book_ratings = 50
min_user_ratings = 50

# Filtra livros e usuários com base nos thresholds definidos
popular_books_isbn = book_counts[book_counts >= min_book_ratings].index
data_filtered = data_analise[data_analise['ISBN'].isin(popular_books_isbn)]
active_users_id = user_counts[user_counts >= min_user_ratings].index
data_filtered = data_filtered[data_filtered['User-ID'].isin(active_users_id)]
print(f"Formato do dataset final para o modelo: {data_filtered.shape}")

# =========================
# 6) PREPARAÇÃO E TREINAMENTO DO MODELO
# =========================
print("\nCriando a matriz de avaliações e treinando o modelo KNN...")
ratings_matrix = data_filtered.pivot_table(index='User-ID', columns='ISBN', values='Book-Rating').fillna(0)
ratings_sparse = csr_matrix(ratings_matrix.values)
model_knn = NearestNeighbors(metric='cosine', algorithm='brute')
model_knn.fit(ratings_sparse)
print("Modelo treinado com sucesso.")

# =========================
# 7) FUNÇÃO DE RECOMENDAÇÃO
# =========================
def gerar_recomendacoes_para_usuario(user_id, ratings_matrix, model, books_df, n_neighbors=6, rating_threshold=7, n_recommendations=10):
    if user_id not in ratings_matrix.index:
        print(f"ERRO: Usuário {user_id} não encontrado nos dados filtrados.")
        return []

    user_index = ratings_matrix.index.get_loc(user_id)
    distances, indices = model.kneighbors(ratings_matrix.iloc[user_index, :].values.reshape(1, -1), n_neighbors=n_neighbors)
    similar_users_indices = indices.flatten()[1:]
    similar_users_ids = ratings_matrix.index[similar_users_indices]
    livros_avaliados_pelo_usuario_original = set(ratings_matrix.loc[user_id][ratings_matrix.loc[user_id] > 0].index)
    recomendacoes = defaultdict(int)

    for similar_user_id in similar_users_ids:
        livros_bem_avaliados = ratings_matrix.loc[similar_user_id][ratings_matrix.loc[similar_user_id] > rating_threshold].index
        for isbn in livros_bem_avaliados:
            if isbn not in livros_avaliados_pelo_usuario_original:
                recomendacoes[isbn] += 1
    
    if not recomendacoes:
        return []

    isbns_ordenados = sorted(recomendacoes.keys(), key=lambda isbn: recomendacoes[isbn], reverse=True)
    titulos_recomendados = []
    for isbn in isbns_ordenados:
        titulo = books_df[books_df['ISBN'] == isbn]['Book-Title'].values
        if len(titulo) > 0 and titulo[0] not in titulos_recomendados:
             titulos_recomendados.append(titulo[0])
        if len(titulos_recomendados) >= n_recommendations:
            break
            
    return titulos_recomendados

# =========================
# 8) EXECUÇÃO E EXIBIÇÃO DO EXEMPLO
# =========================
if not ratings_matrix.empty:
    # Escolhe um usuário aleatório da matriz para garantir que o teste funcione
    user_id_para_recomendar = np.random.choice(ratings_matrix.index)
    print(f"\n--- Gerando recomendações para o Usuário: {user_id_para_recomendar} ---")

    # Chama a função para obter a lista de livros
    lista_de_livros = gerar_recomendacoes_para_usuario(
        user_id=user_id_para_recomendar,
        ratings_matrix=ratings_matrix,
        model=model_knn,
        books_df=books
    )

    # Exibe os resultados
    if lista_de_livros:
        print(f"\nTop {len(lista_de_livros)} livros recomendados:")
        for i, titulo in enumerate(lista_de_livros):
            print(f"{i+1}: {titulo}")
    else:
        print("Não foi possível gerar recomendações para este usuário com os critérios atuais.")
else:
    print("\nNão há dados suficientes para treinar o modelo após a filtragem. Tente diminuir os thresholds 'min_book_ratings' e 'min_user_ratings'.")


print("\nScript executado com sucesso!")

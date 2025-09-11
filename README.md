# Sistema de Recomendação de Livros para Apoiar o ODS 9: Indústria, Inovação e Infraestrutura

Este repositório contém o desenvolvimento de um sistema de recomendação de livros como parte do **Projeto Aplicado III** do curso de Tecnologia em Ciência de Dados da Universidade Presbiteriana Mackenzie. O projeto visa aplicar técnicas de inteligência artificial e aprendizado de máquina para personalizar o acesso à leitura, contribuindo para o **ODS 9 - Indústria, Inovação e Infraestrutura** da ONU.

## 📖 Visão Geral

A crescente disponibilidade de informações e o avanço tecnológico transformaram a forma como o conhecimento é produzido, compartilhado e consumido. Nesse contexto, os sistemas de recomendação surgem como ferramentas essenciais para auxiliar usuários na descoberta de livros relevantes, reduzindo o esforço necessário para selecionar obras de interesse em meio a grandes volumes de dados.

## 🎯 Objetivo do Projeto

### Objetivo Geral
Desenvolver um sistema de recomendação de livros que sugira obras semelhantes e bem avaliadas, promovendo acesso direcionado à leitura e apoiando iniciativas de inovação relacionadas ao ODS 9.

### Objetivos Específicos
- **Análise Exploratória**: Explorar e analisar o conjunto de dados Book Crossing Dataset
- **Implementação de Técnicas**: Aplicar algoritmos de recomendação combinando atributos dos livros (autor, editora, ano de publicação) e métricas de popularidade (avaliações dos usuários)
- **Avaliação de Resultados**: Utilizar métricas adequadas como precisão, recall e RMSE para validar a eficácia do sistema
- **Conexão com ODS 9**: Relacionar os resultados ao contexto do ODS 9, evidenciando a contribuição para inovação, acesso à leitura e fortalecimento da infraestrutura digital

## 📊 Dataset Utilizado

O projeto utiliza o **Book Crossing Dataset**, composto por tres arquivos principais:

- **BX-Books.csv**: Catálogo com informações de 271.381 livros, incluindo ISBN, título, autor, ano de publicação, editora e links para imagens das capas
- **BX-Users.csv**: Base de usuários com 278.860 registros contendo localização e idade dos leitores
- **BX-Book-Ratings.csv**: Matriz de avaliações com 1.149.781 registros de notas (escala 0-10) atribuídas pelos usuários aos livros

Este dataset público e internacional permite a criação de um sistema robusto e replicável, adequado para análises de comportamento de leitura e desenvolvimento de algoritmos de recomendação personalizados.

## 🌍 Alinhamento com o ODS 9

O projeto contribui diretamente para o **ODS 9 - Indústria, Inovação e Infraestrutura** através de três pilares fundamentais:

### 🚀 **Inovação**
- Aplicação de técnicas avançadas de inteligência artificial e aprendizado de máquina
- Desenvolvimento de soluções digitais inovadoras para recomendação personalizada
- Implementação de algoritmos de filtragem colaborativa e baseada em conteúdo

### 🏗️ **Infraestrutura**
- Criação de base tecnológica para futuras plataformas digitais (aplicativos, sites, bibliotecas virtuais)
- Desenvolvimento de pipeline de dados escalável e reutilizável
- Estruturação de repositório organizado seguindo melhores práticas de engenharia de dados

### 🏭 **Indústria**
- Fortalecimento do setor editorial através do incentivo ao consumo de livros
- Apoio à indústria cultural e criativa nacional e internacional
- Criação de valor para editoras e livrarias através de recomendações direcionadas

## 🔬 Premissas e Metodologia Inicial

### **Abordagem Metodológica**
O sistema será desenvolvido utilizando técnicas híbridas de recomendação:

1. **Filtragem Baseada em Conteúdo**: Análise de atributos dos livros (gênero, autor, editora, ano)
2. **Filtragem Colaborativa**: Identificação de padrões nas avaliações de usuários similares
3. **Sistemas Híbridos**: Combinação das abordagens para maior precisão e cobertura

### **Pipeline de Desenvolvimento**
1. **Coleta e Preparação**: Download e tratamento do Book Crossing Dataset
2. **Limpeza de Dados**: Remoção de duplicatas, tratamento de valores ausentes e padronização
3. **Análise Exploratória (EDA)**: Análise estatística descritiva das distribuições de autores, avaliações, editoras e padrões de leitura
4. **Modelagem**: Implementação de algoritmos de recomendação utilizando bibliotecas como scikit-learn e surprise
5. **Avaliação**: Validação através de métricas de precisão, recall, RMSE e análise qualitativa dos resultados

### **Premissas Técnicas**
- Utilização de Python como linguagem principal de desenvolvimento
- Aplicação de técnicas de processamento de linguagem natural para análise de títulos e metadados
- Implementação de métodos de avaliação offline utilizando divisão temporal dos dados
- Consideração de aspectos de cold start para novos usuários e livros

## 👥 Equipe de Desenvolvimento

**Membros do Grupo:**
- **Gustavo José Fermiano** - RA: 104409293
- **Kelly Haro Vasconcellos** - RA: 10441014  
- **Wesley Rodrigo dos Santos** - RA: 10433408

## 📅 Cronograma de Execução

O projeto será desenvolvido em **4 etapas principais**:

- **📋 Etapa 1** - Organização inicial (Agosto - Setembro): Formação do grupo, definição do tema, estruturação do repositório
- **🔬 Etapa 2** - Pesquisa e prova de conceito (Setembro - Outubro): Levantamento teórico, exploração de dados e desenvolvimento de protótipo
- **⚙️ Etapa 3** - Análise e ajustes metodológicos (Outubro): Avaliação de resultados preliminares e refinamento da metodologia
- **📊 Etapa 4** - Consolidação e apresentação (Novembro): Organização dos resultados finais e preparação da apresentação

## 📈 Entregas Esperadas

Como resultado do projeto, esperamos desenvolver:

- **Sistema de Recomendação Funcional**: Algoritmo capaz de sugerir livros personalizados
- **Análise de Impacto**: Relatório detalhado sobre a contribuição para o ODS 9
- **Documentação Técnica**: Guias de implementação e reprodução dos resultados

---

## 📚 Referências Iniciais

- Organização das Nações Unidas (ONU). **Objetivos de Desenvolvimento Sustentável – ODS 9**: Indústria, Inovação e Infraestrutura. Disponível em: https://sdgs.un.org/goals/goal9
- Book Crossing Dataset. Disponível em: https://www.kaggle.com/datasets/ruchi798/bookcrossing-dataset/data
- Repositório do Projeto. GitHub - Projeto Aplicado III

---

> **Nota**: Este projeto está em desenvolvimento progressivo. O README será atualizado conforme o avanço das entregas e implementações.
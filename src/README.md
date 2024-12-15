# 🐍 Pasta `src/` - Scripts Python do Projeto

Esta pasta contém os **scripts Python** desenvolvidos para as principais etapas do projeto **"Predição da Depressão Estudantil"**. Esses scripts permitem executar as análises, pré-processamento, treinamento e avaliação do modelo de forma automatizada.

---

## 📂 **Conteúdo dos Scripts**

1. **`preprocess.py`** - 🧹 **Pré-Processamento dos Dados**  
   - **Objetivo**: Realizar o pré-processamento necessário para preparar os dados para modelagem.
   - **Principais Funções**:
      - Tratamento de valores ausentes.
      - Codificação de variáveis categóricas (Label Encoding e One-Hot Encoding).
      - Padronização das variáveis numéricas.
   - **Como executar**:
      ```bash
      python src/preprocess.py
      ```
   - **Saída**:
      - Dados pré-processados prontos para uso nos modelos.

2. **`train_model.py`** - 🤖 **Treinamento do Modelo**  
   - **Objetivo**: Treinar o modelo de aprendizado de máquina utilizando o conjunto de dados preparado.
   - **Principais Funções**:
      - Carregamento dos dados pré-processados.
      - Treinamento inicial do modelo **Random Forest**.
      - Salvamento do modelo treinado em formato `.pkl`.
   - **Como executar**:
      ```bash
      python src/train_model.py
      ```
   - **Saída**:
      - Arquivo do modelo treinado salvo para uso posterior.

3. **`evaluate_model.py`** - 📈 **Avaliação do Modelo**  
   - **Objetivo**: Avaliar o desempenho do modelo treinado no conjunto de teste.
   - **Principais Funções**:
      - Cálculo de métricas de desempenho: Acurácia, precisão, recall, F1-score.
      - Geração da **Curva ROC** e cálculo do **AUC**.
      - Relatório de classificação.
   - **Como executar**:
      ```bash
      python src/evaluate_model.py
      ```
   - **Saída**:
      - Relatórios e gráficos de desempenho do modelo.

---

## 🚀 **Como Utilizar os Scripts**

1. **Certifique-se de que as dependências estão instaladas**:
   ```bash
   pip install -r requirements.txt
2. Execute os scripts na sequência:
- Pré-processamento:
   ```bash
   python src/preprocess.py
- Treinamento do Modelo:
   ```bash
  python src/train_model.py
- Avaliação do Modelo:
   ```bash
   python src/evaluate_model.py
3. Resultados:
- Arquivo do modelo treinado: ```model.pkl``` (salvo na pasta ```reports/```).
- Relatórios e gráficos de desempenho.

---

# 🧩 Objetivos dos Scripts
Os scripts automatizam as principais etapas do projeto:
- Pré-processamento de dados.
- Construção e treinamento do modelo.
- Avaliação detalhada com métricas e visualizações.

---

# 📌 Observações
- Certifique-se de que o dataset está armazenado na pasta ```data/```.
- Modificações nos scripts devem ser documentadas para garantir reprodutibilidade.
- Ajuste os caminhos de entrada/saída caso necessário.
     

# 🎓 Predição da Depressão Estudantil

### 📌 **Objetivo**
Este projeto tem como objetivo prever a probabilidade de um estudante sofrer de depressão com base em fatores acadêmicos, financeiros e emocionais. Utilizando um **modelo Random Forest**, realizamos análises detalhadas e propomos estratégias para identificação precoce e suporte a estudantes em risco.

---

## 📂 **Estrutura do Projeto**

- **📁 data**: Contém o dataset utilizado no projeto.
   - Dataset original: [Student Depression Dataset](https://www.kaggle.com/datasets/hopesb/student-depression-dataset)

- **📁 notebooks**: Notebooks com o passo a passo do projeto:
   - `1_exploratory_analysis.ipynb`: Análise exploratória dos dados (EDA).
   - `2_model_training.ipynb`: Construção e treinamento inicial do modelo.
   - `3_model_optimization.ipynb`: Tuning de hiperparâmetros e avaliação final.

- **📁 src**: Scripts Python:
   - `preprocess.py`: Pré-processamento dos dados.
   - `train_model.py`: Treinamento do modelo.
   - `evaluate_model.py`: Avaliação do modelo.

- **📁 reports**: Relatórios e gráficos gerados:
   - **Importância das Variáveis** 🧩
   - **Curva ROC** 📈
   - **Desempenho do Modelo** 🏆

- **📁 docs**: Documentação detalhada com visão geral e insights do projeto.

---

## 🚀 **Principais Ferramentas e Bibliotecas**
- **Python 3.8+**
- **Pandas**: Manipulação e análise de dados.
- **Matplotlib & Seaborn**: Visualização de dados.
- **Scikit-learn**: Construção e avaliação do modelo.
- **Jupyter Notebook**: Documentação e execução de códigos.

---

## 🛠️ **Como Executar o Projeto**

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/matheuscsf/student-depression-prediction.git
   cd student-depression-prediction
 
2. Instale as dependências:

```bash
pip install -r requirements.txt
```
3. Acesse os notebooks:
- Execute os notebooks localmente para ver o passo a passo da análise.

---

4. Execute os scripts:
- Pré-processamento: ```python src/preprocess.py```
- Treinamento: ```python src/train_model.py```
- Avaliação: ```python src/evaluate_model.py```

---

# 🔑 Principais Achados

- A variável **"Have you ever had suicidal thoughts?"** é a mais importante na previsão de depressão.
- Pressão acadêmica, estresse financeiro e horas de estudo/trabalho são fatores críticos associados à depressão.
- O modelo Random Forest apresentou:
  - Acurácia: 84,4%
  - Recall: 89,3%
  - AUC: 0,92 (excelente capacidade de distinção entre classes).
 
---

# 🧠 Intervenções Propostas
- **Identificação Precoce**: Uso do modelo para monitorar fatores críticos.
- **Suporte Acadêmico**: Flexibilização de prazos e programas de tutoria.
- **Assistência Financeira**: Bolsas e programas de educação financeira.
- **Apoio Emocional**: Aconselhamento psicológico e campanhas de saúde mental.
- **Hábitos Saudáveis**: Promoção de sono adequado, alimentação saudável e atividades físicas.

---

# 🤝 Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

# 📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar e modificar.

# 📒 Pasta `notebooks/` - Notebooks do Projeto

Esta pasta contém os **notebooks Jupyter** que documentam o passo a passo do projeto **"Predição da Depressão Estudantil"**. Cada notebook corresponde a uma etapa específica do desenvolvimento, desde a análise exploratória até a otimização do modelo.

---

## 📂 **Conteúdo dos Notebooks**

1. **`1_exploratory_analysis.ipynb`** - 📊 **Análise Exploratória dos Dados (EDA)**  
   - **Objetivo**: Explorar e compreender os dados do projeto.  
   - **Principais Etapas**:
      - Visualização da distribuição das variáveis.
      - Análise de valores ausentes e inconsistências.
      - Identificação das variáveis mais relevantes.
      - Insights iniciais sobre padrões e tendências.

2. **`2_model_training.ipynb`** - 🤖 **Construção e Treinamento do Modelo**  
   - **Objetivo**: Construir o modelo inicial de aprendizado de máquina.  
   - **Principais Etapas**:
      - Separação das variáveis independentes (**X**) e dependente (**y**).
      - Divisão dos dados em treino e teste (70/30).
      - Padronização das variáveis numéricas.
      - Treinamento inicial com o algoritmo **Random Forest**.
      - Avaliação preliminar com métricas como acurácia, precisão e recall.

3. **`3_model_optimization.ipynb`** - ⚙️ **Otimização e Avaliação do Modelo**  
   - **Objetivo**: Melhorar o desempenho do modelo através de ajustes e avaliações mais robustas.  
   - **Principais Etapas**:
      - Tuning de hiperparâmetros utilizando **GridSearchCV**.
      - Análise de **importância das variáveis**.
      - Avaliação do modelo otimizado com:
         - **Curva ROC** e **AUC**.
         - Relatório de classificação final.
      - Interpretação dos resultados e principais conclusões.

4. **`saude_mental_estudantes.ipynb`** - ✅​ **Notebook completo**

---

## 🚀 **Como Executar os Notebooks**

1. Certifique-se de que todas as **dependências estão instaladas**:
   ```bash
   pip install -r requirements.txt
  ``
2.Abra os notebooks usando o Jupyter Notebook ou Jupyter Lab:
   ```bash
jupyter notebook
  ````
3. Navegue até a pasta ```notebooks/``` e execute os arquivos na sequência:
- ```1_exploratory_analysis.ipynb```
- ```2_model_training.ipynb```
- ```3_model_optimization.ipynb```

---

# 🧩 Objetivos dos Notebooks
Os notebooks fornecem:
- Um **passo a passo claro e organizado** para replicação do projeto.
- Visualizações interativas e insights detalhados.
- Documentação do processo de construção e avaliação do modelo de aprendizado de máquina.

---

# 📌 Observações
- Os notebooks utilizam o dataset original armazenado na pasta data/.
- Para melhor visualização, execute os notebooks localmente ou no Google Colab.
- Modificações nos dados ou nos parâmetros do modelo devem ser documentadas.

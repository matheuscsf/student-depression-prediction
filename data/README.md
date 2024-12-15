# 📊 Pasta `data/` - Dados do Projeto

Esta pasta contém os **dados utilizados no projeto** para a **predição da depressão estudantil**.

---

## 📄 **Conteúdo da Pasta**

- **`student_depression.csv`**: 
   - Arquivo original com os dados utilizados no projeto.
   - Fonte: [Kaggle - Student Depression Dataset](https://www.kaggle.com/datasets/hopesb/student-depression-dataset)
   - **Descrição**:
      - Contém informações sobre fatores emocionais, acadêmicos, financeiros e hábitos de estudantes.
      - Tamanho: ~27.901 registros e 18 colunas.

---

## 📊 **Variáveis no Dataset**

| **Variável**                                 | **Descrição**                                      |
|---------------------------------------------|--------------------------------------------------|
| `id`                                        | Identificador único do participante.              |
| `Gender`                                    | Gênero do participante (Masculino/Feminino).      |
| `Age`                                       | Idade do participante.                            |
| `City`                                      | Cidade onde reside.                               |
| `Profession`                                | Profissão (ex.: Estudante).                       |
| `Academic Pressure`                         | Nível de pressão acadêmica (Escala de 1 a 5).     |
| `Work Pressure`                             | Nível de pressão no trabalho.                     |
| `CGPA`                                      | Desempenho acadêmico (média de notas).            |
| `Study Satisfaction`                        | Nível de satisfação com os estudos.               |
| `Job Satisfaction`                          | Satisfação com o trabalho.                        |
| `Sleep Duration`                            | Duração média do sono diário.                     |
| `Dietary Habits`                            | Hábitos alimentares (Saudáveis/Moderados/Não).    |
| `Degree`                                    | Grau acadêmico (ex.: BSc, M.Tech).                |
| `Have you ever had suicidal thoughts?`      | Pensamentos suicidas (Sim/Não).                   |
| `Work/Study Hours`                          | Horas diárias dedicadas a estudo ou trabalho.     |
| `Financial Stress`                          | Nível de estresse financeiro (Escala de 1 a 5).   |
| `Family History of Mental Illness`          | Histórico familiar de doença mental (Sim/Não).    |
| `Depression`                                | Diagnóstico de depressão (0 = Não, 1 = Sim).      |

---

## 🔍 **Como Utilizar os Dados**

1. **Baixe os Dados**:
   - Se necessário, faça o download do dataset original pelo [link do Kaggle](https://www.kaggle.com/datasets/hopesb/student-depression-dataset).

2. **Carregue os Dados**:
   Utilize bibliotecas como `pandas` para carregar os dados em um DataFrame:
   ```python
   import pandas as pd
   df = pd.read_csv("data/student_depression.csv")
   print(df.head())
   ````
3. Pré-Processamento:
- Antes de treinar os modelos, é importante realizar etapas de **limpeza, tratamento de valores ausentes e codificação de variáveis**.

---

# 📌 Observações

- O dataset está em formato ```.csv``` e é utilizado em todas as etapas do projeto.
- Caso o arquivo seja modificado ou atualizado, mantenha uma cópia do original e documente as mudanças.
- Sempre respeite os direitos do autor e credite a fonte ao utilizar os dados.

# Importação das bibliotecas essenciais
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.metrics import roc_curve, roc_auc_score

data = pd.read_csv("Student_Depression_Dataset.csv")
data.head()

# Remover linhas com valores ausentes
dados_limpos = data.dropna()

# Verificar se ainda há valores ausentes
valores_ausentes_apos_limpeza = dados_limpos.isnull().sum().sum()

valores_ausentes_apos_limpeza

# Criar cópias para preservar o dataset original e preparar para codificação
dados_codificados = dados_limpos.copy()

# Identificar variáveis categóricas e aplicar LabelEncoder
variaveis_categoricas = dados_codificados.select_dtypes(include=['object']).columns
label_encoder = LabelEncoder()

# Aplicar a codificação
for coluna in variaveis_categoricas:
    dados_codificados[coluna] = label_encoder.fit_transform(dados_codificados[coluna])

# Verificar o resultado
dados_codificados.head()

# Identificar colunas numéricas (excluindo categoricamente codificadas)
colunas_numericas = dados_codificados.select_dtypes(include=['float64', 'int64']).columns

# Aplicar Min-Max Scaling
scaler = MinMaxScaler()
dados_normalizados = dados_codificados.copy()
dados_normalizados[colunas_numericas] = scaler.fit_transform(dados_codificados[colunas_numericas])

# Verificar resultado da normalização
dados_normalizados.head()

# Tratando os valores ausentes na variável "Financial Stress" com a média
media_financial_stress = data['Financial Stress'].mean()
data['Financial Stress'].fillna(media_financial_stress, inplace=True)

# Verificando novamente se há valores ausentes
valores_ausentes_pos_tratamento = data.isnull().sum()
valores_ausentes_pos_tratamento

# Aplicando Label Encoding para variáveis com poucas categorias
label_encoder_cols = ['Gender', 'Have you ever had suicidal thoughts ?', 'Family History of Mental Illness']
label_encoder = LabelEncoder()

for col in label_encoder_cols:
    data[col] = label_encoder.fit_transform(data[col])

# Aplicando One-Hot Encoding para variáveis com múltiplas categorias
one_hot_cols = ['Sleep Duration', 'Dietary Habits', 'Degree', 'City', 'Profession']
data = pd.get_dummies(data, columns=one_hot_cols, drop_first=True)

# Verificando as primeiras linhas dos dados após codificação
data.head()
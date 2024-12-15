# Separando as variáveis independentes (X) e dependente (y)
X = data.drop(columns=['Depression', 'id'])  # Removendo a variável-alvo e a coluna de ID
y = data['Depression']

# Verificando as dimensões das variáveis
dimensoes_X = X.shape
dimensoes_y = y.shape

dimensoes_X, dimensoes_y

# Dividindo os dados em treino e teste (70% treino, 30% teste)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Verificando as dimensões dos conjuntos
dimensoes_treino = X_treino.shape, y_treino.shape
dimensoes_teste = X_teste.shape, y_teste.shape

dimensoes_treino, dimensoes_teste

# Identificando variáveis numéricas contínuas
variaveis_numericas = ['Age', 'Academic Pressure', 'Work Pressure', 'CGPA', 'Study Satisfaction',
                       'Job Satisfaction', 'Work/Study Hours', 'Financial Stress']

# Aplicando padronização (StandardScaler) apenas às variáveis contínuas
scaler = StandardScaler()
X_treino[variaveis_numericas] = scaler.fit_transform(X_treino[variaveis_numericas])
X_teste[variaveis_numericas] = scaler.transform(X_teste[variaveis_numericas])

# Verificando as primeiras linhas após a padronização
X_treino.head()
X_teste.head()

# Inicializando o modelo Random Forest
random_forest = RandomForestClassifier(random_state=42, n_estimators=100)

# Treinando o modelo com os dados de treino
random_forest.fit(X_treino, y_treino)

# Realizando previsões no conjunto de teste
y_pred = random_forest.predict(X_teste)

# Calculando métricas de desempenho
acuracia = accuracy_score(y_teste, y_pred)
precisao = precision_score(y_teste, y_pred)
recall = recall_score(y_teste, y_pred)
f1 = f1_score(y_teste, y_pred)
relatorio_classificacao = classification_report(y_teste, y_pred, target_names=["Não", "Sim"])

precisao

recall

f1

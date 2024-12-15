# Calculando a matriz de confusão
matriz_confusao = confusion_matrix(y_teste, y_pred)

# Visualizando a matriz de confusão
plt.figure(figsize=(8, 6))
sns.heatmap(matriz_confusao, annot=True, fmt="d", cmap="Blues", xticklabels=["Não", "Sim"], yticklabels=["Não", "Sim"])
plt.title("Matriz de Confusão - Random Forest")
plt.xlabel("Previsões do Modelo")
plt.ylabel("Valores Reais")
plt.show()

print("\nRelatório de Classificação:")
print(relatorio_classificacao)

print("\nAcurácia:", acuracia)

# Analisando a importância das variáveis
feature_importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': random_forest.feature_importances_
}).sort_values(by='Importance', ascending=False)

# Plotando as 10 variáveis mais importantes
plt.figure(figsize=(10, 8))
sns.barplot(x='Importance', y='Feature', data=feature_importances.head(10))
plt.title('Importância das Variáveis - Top 10')
plt.xlabel('Importância')
plt.ylabel('Variáveis')
plt.show()

# Exibindo as 10 principais variáveis
feature_importances.head(10)

# Definindo a grade de hiperparâmetros para otimização
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5],
    'min_samples_leaf': [1, 2]
}

# Inicializando o modelo Random Forest
random_forest = RandomForestClassifier(random_state=42)

# Configurando o GridSearchCV
grid_search = GridSearchCV(estimator=random_forest, param_grid=param_grid, 
                           cv=3, scoring='accuracy', verbose=2, n_jobs=-1)

# Executando o GridSearchCV
grid_search.fit(X_treino, y_treino)

# Melhor modelo e hiperparâmetros# Melhor modelo e hiperparâmetros
melhores_parametros = grid_search.best_params_
melhor_modelo = grid_search.best_estimator_
melhores_parametros

melhores_parametros = grid_search.best_params_
melhor_modelo = grid_search.best_estimator_
melhores_parametros

# Treinando o modelo com os melhores parâmetros encontrados
modelo_otimizado = RandomForestClassifier(
    n_estimators=200, 
    max_depth=None, 
    min_samples_split=5, 
    min_samples_leaf=2, 
    random_state=42
)

modelo_otimizado.fit(X_treino, y_treino)

# Realizando previsões no conjunto de teste
y_pred_otimizado = modelo_otimizado.predict(X_teste)

acuracia_otimizada = accuracy_score(y_teste, y_pred_otimizado)
precisao_otimizada = precision_score(y_teste, y_pred_otimizado)
recall_otimizado = recall_score(y_teste, y_pred_otimizado)
f1_otimizado = f1_score(y_teste, y_pred_otimizado)
relatorio_otimizado = classification_report(y_teste, y_pred_otimizado, target_names=["Não", "Sim"])
matriz_confusao_otimizada = confusion_matrix(y_teste, y_pred_otimizado)

acuracia_otimizada

precisao_otimizada

recall_otimizado

f1_otimizado

print("\nRelatório de Classificação:")
print(relatorio_otimizado)

print("\nAcurácia:", acuracia)

# Visualizando a matriz de confusão
plt.figure(figsize=(8, 6))
sns.heatmap(matriz_confusao_otimizada, annot=True, fmt="d", cmap="Blues", xticklabels=["Não", "Sim"], yticklabels=["Não", "Sim"])
plt.title("Matriz de Confusão - Random Forest")
plt.xlabel("Previsões do Modelo")
plt.ylabel("Valores Reais")
plt.show()

# Calculando probabilidades para a curva ROC
y_probabilidades = modelo_otimizado.predict_proba(X_teste)[:, 1]

# Calculando a curva ROC
fpr, tpr, thresholds = roc_curve(y_teste, y_probabilidades)
auc = roc_auc_score(y_teste, y_probabilidades)

# Plotando a curva ROC
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'AUC = {auc:.2f}')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
plt.title('Curva ROC - Random Forest Otimizado')
plt.xlabel('Falso Positivo (FPR)')
plt.ylabel('Verdadeiro Positivo (TPR)')
plt.legend(loc='lower right')
plt.show()

auc
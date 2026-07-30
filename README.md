# 🎓 Datathon FIAP: Associação Passos Mágicos
**Sistema de Inteligência Educacional e Alerta Precoce de Defasagem**

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-orange.svg)
![Streamlit](https://img.shields.io/badge/Deploy-Streamlit-red.svg)
![Status](https://img.shields.io/badge/Status-Concluído-success.svg)

## 📌 Acesso Rápido ao Projeto
* **Aplicação Web (Deploy):** [Acessar o Dashboard Interativo](https://datathon-fiap-alt.streamlit.app/) *(Insira o seu link final aqui)*
* **Notebook de Modelagem:** [Acessar Google Colab](./Datathon_Fase5.ipynb)

---

## 📖 Contexto e Desafio de Negócio
A **Associação Passos Mágicos** é uma ONG com mais de 30 anos de atuação focada em transformar a vida de crianças e jovens em vulnerabilidade social por meio da educação. A ONG avalia seus alunos através do **PEDE (Pesquisa do Desenvolvimento Educacional)**, um índice multidimensional.

**O Desafio:** Como utilizar o histórico de dados (2022 a 2024) para identificar padrões de comportamento e notas, prevenindo a defasagem escolar e a evasão antes que ocorram?

## 💡 A Solução: Sistema de Alerta Precoce
Desenvolvemos uma solução analítica e preditiva ponta a ponta. Através de um painel longitudinal (cruzamento de safras), treinamos algoritmos de **Machine Learning (Random Forest)** para prever a probabilidade de um estudante cair de rendimento no próximo ciclo.

A solução foi dividida em dois cenários estratégicos:
1. **Modelo de Diagnóstico Completo:** Utiliza o histórico de notas + comportamento. (Acurácia Global: 76%, ROC-AUC: 0.85).
2. **Modelo de Alerta Precoce (Comportamental):** Ignora as notas acadêmicas e avalia **apenas** Engajamento, Autoavaliação e Aspectos Psicopedagógicos. Atingiu **71% de Recall** para risco, provando que é possível salvar o aluno antes mesmo que as notas baixas apareçam.

---

## 🛠️ Stack Tecnológico
* **Linguagem:** Python
* **Manipulação de Dados:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (RandomForestClassifier)
* **Visualização (EDA):** Matplotlib, Seaborn
* **Deploy e Web App:** Streamlit, Streamlit Cloud

---

## 📂 Estrutura do Repositório

```text
├── app.py                            # Script principal do Dashboard em Streamlit
├── requirements.txt                  # Dependências para o deploy na nuvem
├── modelo_passos_magicos_rf.pkl      # Modelo de Machine Learning serializado (joblib)
├── features_modelo.pkl               # Lista de features obrigatórias para predição
├── Datathon_Fase5.ipynb              # Notebook original com toda a EDA e Treinamento
└── README.md                         # Documentação do projeto

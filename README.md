# 🎓 Sistema de Inteligência Educacional e Alerta Precoce de Defasagem
> **FIAP - Pós-Graduação em Data Analytics** > *Tech Challenge - Fase 5: Datathon Associação Passos Mágicos*

Análise longitudinal de dados educacionais e deploy de um modelo preditivo (Random Forest) para triagem comportamental e prevenção de queda de rendimento em alunos em situação de vulnerabilidade social.

---

## 🚀 Link da Aplicação em Produção
O sistema web foi implantado com sucesso no Streamlit Community Cloud e pode ser acessado em tempo real pelas equipes pedagógicas e psicológicas da ONG através do link abaixo:

🔗 **[Acessar o Painel de Alerta Precoce](https://datathon-fiap-alt.streamlit.app/)** *(Nota: Insira o seu link final do Streamlit aqui)*

---

## 📌 O Problema de Negócio e a Solução
A **Associação Passos Mágicos** atua há mais de 30 anos transformando a vida de crianças e jovens através da educação. O acompanhamento dos alunos é feito através do Índice de Desenvolvimento Educacional (INDE), uma métrica multidimensional que avalia notas, engajamento, questões socioemocionais e autoavaliação.

O desafio central (Datathon) foi criar uma ferramenta analítica que utilizasse o histórico de dados (safras 2022 a 2024) para identificar os alunos com maior probabilidade de entrar em defasagem escolar no ciclo seguinte. 

**Nossa Entrega:**
1. **Dashboard Exploratório:** Resposta baseada em dados às 11 Questões de Negócio levantadas pela ONG.
2. **Modelo Preditivo Web:** Uma ferramenta de triagem para intervir *antes* que as notas caiam.
3. **Gerador Prescritivo de Plano de Ação:** Um algoritmo que varre a base de alunos e exporta uma planilha automática (Excel) indicando exatamente que tipo de ajuda cada estudante precisa (Reforço, Psicólogo, Mentoria).

---

## 📊 Performance e Arena de Modelos

O projeto foi estruturado através de um pipeline de Ciência de Dados no Google Colab. Realizamos um benchmarking (Arena de Modelos) comparando Regressão Logística, XGBoost e Random Forest, sagrando este último como o campeão absoluto de estabilidade para os nossos dados não-lineares.

Dividimos a solução em dois cenários estratégicos:

1. **Cenário 1 (Modelo de Diagnóstico Completo):** Inclui o histórico acadêmico completo, utilizando as Notas (IDA) e o Índice Geral anterior (INDE).
   * **ROC-AUC:** `0.708`
   * **Acurácia:** `65.3%`
   * *Aplicação:* Fechamento de ciclo e planejamento de turmas/bolsas para o ano seguinte.

2. **Cenário 2 (Modelo Comportamental / Alerta Precoce):** Remove os dados de notas. Desafia a IA a estimar o risco de defasagem avaliando **exclusivamente** indicadores comportamentais: Engajamento (IEG), Autoavaliação (IAA), Psicológico (IPP) e Psicossocial (IPS).
   * **Recall para Risco:** `71.00%` (Alta sensibilidade para capturar quem precisa de ajuda urgente).
   * *Aplicação:* Intervenção preventiva no meio do ano letivo.

---

## 📂 Estrutura do Repositório (Arquitetura Flat)

Para garantir máxima eficiência no deploy contínuo da aplicação no Streamlit Cloud, o repositório adota a estrutura unificada na raiz:

```text
├── app.py                         # Código-fonte da aplicação web interativa em Streamlit
├── requirements.txt               # Especificação de dependências (Pandas, Scikit-Learn, etc.)
├── modelo_passos_magicos_rf.pkl   # Pipeline do modelo preditivo campeão (Random Forest)
├── features_modelo.pkl            # Lista de features obrigatórias mapeadas para o formulário
├── Datathon_Fase5.ipynb           # Notebook original com Análise Exploratória (EDA) e Modelagem
└── README.md                      # Documentação estratégica do projeto (esta vitrine)

# 🎓 Sistema de Inteligência Educacional e Alerta Precoce de Defasagem
> **FIAP - Pós-Graduação em Data Analytics** > *Tech Challenge - Fase 5: Datathon Associação Passos Mágicos*

Análise longitudinal de dados educacionais e deploy de um modelo preditivo baseado em algoritmos de Random Forest para triagem comportamental e prevenção de queda de rendimento em alunos em situação de vulnerabilidade social.

---

## 🚀 Link da Aplicação em Produção
O sistema web foi implantado com sucesso no Streamlit Community Cloud e pode ser acessado em tempo real pelas equipes pedagógicas e psicológicas da ONG através do link abaixo:

🔗 **[Acessar o Painel de Alerta Precoce](https://datathon-fiap-alt.streamlit.app/)**

---

## 📌 O Problema de Negócio
A **Associação Passos Mágicos** atua há mais de 30 anos transformando a vida de crianças e jovens através da educação de qualidade. O acompanhamento dos alunos é feito através do Índice de Desenvolvimento Educacional (INDE), uma métrica multidimensional que avalia notas, engajamento, questões socioemocionais e autoavaliação.

O desafio central deste Datathon foi criar uma ferramenta analítica que utilizasse o histórico de dados (safras 2022 a 2024) para identificar os alunos com maior probabilidade de entrar em defasagem escolar no ciclo seguinte. Esta aplicação atua como uma **ferramenta de triagem e intervenção**, permitindo que tutores e psicólogos atuem *antes* que as notas do aluno caiam de forma irreversível.

---

## 📊 Performance e Resultados do Modelo

O projeto foi estruturado através de um pipeline de Ciência de Dados no Google Colab, culminando em um estudo comparativo que dividiu a previsão em dois cenários estratégicos:

1. **Cenário 1 (Modelo de Diagnóstico Completo):** Inclui o histórico acadêmico completo, utilizando as Notas (IDA) e o Índice Geral anterior (INDE) para prever a tendência futura.
   * **ROC-AUC alcançado:** `0.672`
   * **Acurácia:** `~61.00%`
   * *Aplicação:* Fechamento de ciclo e planejamento de turmas e bolsas para o ano seguinte.

2. **Cenário 2 (Modelo Comportamental / Alerta Precoce):** Remove os dados de desempenho acadêmico (notas) do treinamento. Desafia a Inteligência Artificial a estimar o risco de defasagem avaliando **exclusivamente** indicadores comportamentais: Engajamento (IEG), Autoavaliação (IAA) e Avaliação Psicopedagógica (IPP).
   * **Recall para Risco:** `71.00%` (Alta sensibilidade para capturar quem precisa de ajuda).
   * **ROC-AUC:** `0.667`
   * *Aplicação:* Intervenção preventiva no meio do ano letivo (antes do fechamento das notas finais).

---

## 📂 Estrutura do Repositório (Arquitetura Flat)

Para garantir máxima eficiência no deploy contínuo da aplicação e evitar quebras de caminhos no ambiente do Streamlit Cloud, o repositório adota a estrutura unificada na raiz:

```text
├── app.py                         # Código-fonte da aplicação web interativa em Streamlit
├── requirements.txt               # Especificação de dependências e bibliotecas (Pandas, Scikit-Learn, etc.)
├── modelo_passos_magicos_rf.pkl   # Pipeline do modelo preditivo Random Forest serializado
├── features_modelo.pkl            # Lista de features obrigatórias mapeadas para o formulário
├── Datathon_Fase5.ipynb           # Notebook original com Análise Exploratória (EDA) e Modelagem
└── README.md                      # Documentação estratégica do projeto (esta vitrine)

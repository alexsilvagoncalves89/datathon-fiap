import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E ESTILO GLOBAL (COMPATÍVEL COM DARK/LIGHT MODE)
# ==============================================================================
st.set_page_config(
    page_title="Passos Mágicos | Alerta Precoce de Defasagem",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS corrigida para forçar cor de texto legível
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #1F4E79;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #555555;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background-color: #f0f4f8;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 6px solid #1F4E79;
        margin-bottom: 1rem;
        color: #111111 !important;
    }
    .card h4 {
        color: #1F4E79 !important;
        font-weight: bold;
        margin-top: 0;
    }
    .card p {
        color: #222222 !important;
        font-size: 1.05rem;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. CARREGAMENTO DO MODELO DE MACHINE LEARNING
# ==============================================================================
@st.cache_resource
def load_model():
    modelo = joblib.load('modelo_passos_magicos_rf.pkl')
    features = joblib.load('features_modelo.pkl')
    return modelo, features

try:
    modelo, features = load_model()
    model_loaded = True
except Exception as e:
    model_loaded = False
    st.error(f"Erro ao carregar o modelo treinado: {e}")

# ==============================================================================
# 3. MENU LATERAL DE NAVEGAÇÃO (SIDEBAR)
# ==============================================================================
st.sidebar.markdown("# 🎓 Passos Mágicos")
st.sidebar.markdown("### 📌 Menu Principal")

pagina = st.sidebar.radio(
    "Navegue pelas seções:",
    [
        "🏠 Visão Geral", 
        "📊 Análise Exploratória (EDA)", 
        "🤖 Simulador Preditivo", 
        "🎯 Conclusões & Impacto"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "**Datathon FIAP - Pós-Graduação em Data Analytics**\n\n"
    "**Projeto:** Previsão do Risco de Defasagem Educacional\n"
    "**Tech:** Python | Scikit-Learn | Streamlit"
)

# ==============================================================================
# PÁGINA 1: 🏠 VISÃO GERAL
# ==============================================================================
if pagina == "🏠 Visão Geral":
    st.markdown("<div class='main-header'>🎓 Associação Passos Mágicos</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>Plataforma de Inteligência Educacional e Alerta Precoce de Defasagem</div>", unsafe_allow_html=True)

    st.markdown("""
    ### 🌟 Sobre a Organização
    A **Associação Passos Mágicos** atua há mais de 30 anos transformando a vida de crianças e jovens em situação de vulnerabilidade social através da educação de qualidade, apoio psicopedagógico e ampliação de horizontes.

    ### 🎯 O Desafio do Datathon
    Com o objetivo de potencializar a retenção dos estudantes e prevenir a queda no rendimento escolar, desenvolvemos este sistema preditivo baseado na **Pesquisa do Desenvolvimento Educacional (PEDE)**.
    """)

    st.markdown("---")
    
    # KPIs Rápidos Atualizados com os Dados Reais do seu Modelo
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Alunos Avaliados", "678 Estudantes", delta="Painel 2023-2024")
    col2.metric("Dimensões Analisadas", "7 Indicadores", delta="PEDE")
    col3.metric("Acurácia (Alerta Precoce)", "64%", delta="Cenário Comportamental")
    col4.metric("Recall do Risco", "71%", delta="Captura de Queda de Rendimento")

    st.markdown("---")
    st.markdown("""
    <div class='card'>
        <h4>💡 Proposta de Valor do Projeto</h4>
        <p>A partir dos dados históricos dos ciclos 2022, 2023 e 2024, a ferramenta identifica padrões de comportamento (engajamento, psicopedagógico e autoavaliação) para <b>emitir um alerta preventivo antes mesmo que o aluno tire notas baixas</b> nas avaliações finais. O modelo de Alerta Precoce atinge 71% de sensibilidade (recall) na identificação de alunos em risco.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# PÁGINA 2: 📊 ANÁLISE EXPLORATÓRIA (EDA)
# ==============================================================================
elif pagina == "📊 Análise Exploratória (EDA)":
    st.title("📊 Análise Exploratória e Dimensões do PEDE")
    st.write("Entenda a composição dos indicadores que alimentam o modelo preditivo.")

    tabs = st.tabs(["📚 Dicionário de Indicadores", "📈 Panorama dos Dados"])

    with tabs[0]:
        st.subheader("Os 7 Pilares do Índice de Desenvolvimento Educacional (INDE)")
        
        st.markdown("""
        * **INDE (Índice do Desenvolvimento Educacional):** Nota global multidimensional do estudante.
        * **IAN (Indicador de Adequação de Nível):** Avalia se o aluno está na série correta para sua idade.
        * **IDA (Indicador de Desempenho Acadêmico):** Média ponderada das notas de Português e Matemática.
        * **IEG (Indicador de Engajamento):** Frequência, presença e entrega das tarefas no programa.
        * **IPP (Indicador Psicopedagógico):** Avaliação contínua feita pela equipe de psicologia e pedagogia.
        * **IPV (Indicador do Ponto de Virada):** Avaliação de autonomia, maturidade e inteligência emocional.
        * **IAA (Indicador de Autoavaliação):** Nota atribuída pelo próprio estudante sobre o seu processo de aprendizagem.
        """)

    with tabs[1]:
        st.subheader("Destaques da Análise Longitudinal (2022 - 2024)")
        st.write("Principais achados identificados durante a EDA no Google Colab:")
        
        col1, col2 = st.columns(2)
        with col1:
            st.info("📌 **Soberania do Histórico:** O INDE do ciclo anterior representa ~45% do peso de decisão para prever a tendência futura do aluno.")
        with col2:
            st.success("🧠 **O Sinal Comportamental:** O modelo de 'Alerta Precoce' alcançou **71% de Recall** para identificar queda de rendimento, provando que desengajamento antecede notas baixas.")

# ==============================================================================
# PÁGINA 3: 🤖 SIMULADOR PREDITIVO (MACHINE LEARNING)
# ==============================================================================
elif pagina == "🤖 Simulador Preditivo":
    st.title("🤖 Simulador do Alerta Precoce")
    st.write("Ajuste os indicadores do estudante abaixo para calcular o risco de defasagem para o próximo ciclo.")

    st.markdown("---")

    col1, col2 = st.columns(2)
    entradas = {}

    with col1:
        st.markdown("#### 📌 Histórico & Desempenho Acadêmico")
        entradas['INDE_2023'] = st.slider("INDE do Ano Anterior (Histórico)", 0.0, 10.0, 7.5, step=0.1)
        entradas['IDA'] = st.slider("IDA - Desempenho Acadêmico (Notas)", 0.0, 10.0, 7.0, step=0.1)
        entradas['IAN'] = st.slider("IAN - Adequação de Nível/Idade", 0.0, 10.0, 5.0, step=0.1)

    with col2:
        st.markdown("#### 🧠 Indicadores Comportamentais & Sociais")
        entradas['IEG'] = st.slider("IEG - Engajamento e Frequência", 0.0, 10.0, 8.0, step=0.1)
        entradas['IPP'] = st.slider("IPP - Avaliação Psicopedagógica", 0.0, 10.0, 7.0, step=0.1)
        entradas['IAA'] = st.slider("IAA - Autoavaliação do Aluno", 0.0, 10.0, 8.0, step=0.1)
        entradas['IPV'] = st.slider("IPV - Ponto de Virada", 0.0, 10.0, 7.0, step=0.1)

    st.markdown("---")

    if st.button("🚀 Processar Diagnóstico Preditivo", use_container_width=True):
        if model_loaded:
            df_input = pd.DataFrame([entradas])[features]
            predicao = modelo.predict(df_input)[0]
            probabilidade = modelo.predict_proba(df_input)[0][1]

            st.subheader("📊 Diagnóstico da Inteligência Artificial")

            if predicao == 1:
                st.error(f"🚨 **ALERTA CRÍTICO DE DEFASAGEM!** Probabilidade estimada de queda de rendimento: **{probabilidade * 100:.1f}%**")
                st.warning("💡 **Plano de Ação Sugerido:** Recomendada intervenção psicopedagógica prioritária e acompanhamento quinzenal de tarefas/presença.")
            else:
                st.success(f"✅ **ESTUDANTE EM TRAJETÓRIA SAUDÁVEL!** Probabilidade de defasagem baixa: **{probabilidade * 100:.1f}%**")
                st.info("💡 **Plano de Ação Sugerido:** Aluno com padrão estável. Manter o plano pedagógico padrão de acompanhamento.")
        else:
            st.error("Não foi possível realizar a predição. O modelo não foi carregado corretamente.")

# ==============================================================================
# PÁGINA 4: 🎯 CONCLUSÕES & IMPACTO
# ==============================================================================
elif pagina == "🎯 Conclusões & Impacto":
    st.title("🎯 Recomendação Estratégica de Consultoria")
    st.write("Diretrizes de aplicação prática para a equipe gestora da Passos Mágicos.")

    st.markdown("""
    ### 📌 Recomendações Acionáveis:

    1. **Operacionalização do Alerta Precoce:**
       * **Foco no Recall (71%):** O modelo comportamental prioriza não deixar nenhum aluno em risco passar despercebido, mesmo antes da divulgação das notas finais do semestre.
       
    2. **Ações para Evitar a Inércia Negativa:**
       * Como o $INDE$ histórico responde por ~45% do risco futuro, alunos que apresentarem estagnação no 1º semestre devem receber tutoria individual preventiva.

    3. **Adoção Prática do Dashboard:**
       * Utilizar este simulador nas reuniões de conselho pedagógico para priorizar a distribuição de bolsas e atendimento psicossocial.
    """)

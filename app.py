import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Passos Mágicos - Alerta Precoce",
    page_icon="🎓",
    layout="centered"
)

# ==========================================
# 2. CARREGAMENTO DO MODELO (Cache para performance)
# ==========================================
@st.cache_resource
def load_model():
    # Carrega o modelo treinado e as features esperadas
    modelo = joblib.load('modelo_passos_magicos_rf.pkl')
    features = joblib.load('features_modelo.pkl')
    return modelo, features

modelo, features = load_model()

# ==========================================
# 3. INTERFACE DO USUÁRIO (FRONT-END)
# ==========================================
st.title("🎓 Datathon: Associação Passos Mágicos")
st.subheader("Sistema de Alerta Precoce de Defasagem (Machine Learning)")
st.write("Insira os indicadores atuais do estudante para prever a probabilidade de queda no Índice de Desenvolvimento Educacional (INDE) no próximo ciclo.")

st.markdown("---")

# Criando colunas para organizar os inputs de forma elegante
col1, col2 = st.columns(2)
entradas = {}

with col1:
    st.markdown("**📌 Indicadores Acadêmicos e Histórico**")
    entradas['INDE_2023'] = st.slider("INDE do Ano Anterior", 0.0, 10.0, 7.5, step=0.1)
    entradas['IDA'] = st.slider("IDA (Desempenho Acadêmico)", 0.0, 10.0, 7.0, step=0.1)
    entradas['IAN'] = st.slider("IAN (Adequação de Nível)", 0.0, 10.0, 5.0, step=0.1)

with col2:
    st.markdown("**🧠 Indicadores Comportamentais**")
    entradas['IEG'] = st.slider("IEG (Engajamento)", 0.0, 10.0, 8.0, step=0.1)
    entradas['IPP'] = st.slider("IPP (Avaliação Psicopedagógica)", 0.0, 10.0, 7.0, step=0.1)
    entradas['IAA'] = st.slider("IAA (Autoavaliação)", 0.0, 10.0, 8.0, step=0.1)
    entradas['IPV'] = st.slider("IPV (Ponto de Virada)", 0.0, 10.0, 7.0, step=0.1)

st.markdown("---")

# ==========================================
# 4. BOTÃO DE PREDIÇÃO E RESULTADOS
# ==========================================
if st.button("🚀 Prever Risco de Defasagem", use_container_width=True):
    # Transforma o dicionário em DataFrame, garantindo a ordem exata das colunas do modelo
    df_input = pd.DataFrame([entradas])[features]
    
    # Faz a predição (0 = Manteve/Evoluiu, 1 = Caiu) e pega a probabilidade
    predicao = modelo.predict(df_input)[0]
    probabilidade = modelo.predict_proba(df_input)[0][1]

    st.subheader("📊 Diagnóstico do Modelo")
    
    if predicao == 1:
        st.error(f"🚨 **ALERTA CRÍTICO!** A probabilidade de defasagem/queda de rendimento é de **{probabilidade * 100:.1f}%**")
        st.warning("💡 **Recomendação Prescritiva:** O modelo identificou um padrão de risco. É recomendado agendar uma intervenção psicopedagógica imediata e revisar o nível de engajamento do aluno.")
    else:
        st.success(f"✅ **ALUNO ESTÁVEL!** A probabilidade de queda de rendimento é baixa (**{probabilidade * 100:.1f}%**)")
        st.info("💡 **Recomendação Prescritiva:** O aluno apresenta indicadores saudáveis de evolução. Manter o acompanhamento padrão de fechamento de fase.")

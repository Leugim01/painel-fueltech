# app.py
import streamlit as st
import random
import time

st.set_page_config(layout="centered", page_title="Painel FuelTech")

st.title("🏍️ Painel FuelTech Simulado")

# Inputs
consumo = st.number_input("Quantos km por litro sua moto faz?", min_value=1.0, step=0.1)
preco_gasolina = st.number_input("Qual o preço da gasolina por litro (R$)?", min_value=0.0, step=0.1)
aem_ativo = st.toggle("Ativar modo econômico (AEM)", value=True)

# Lógica de economia
if consumo > 0 and preco_gasolina > 0:
    economia_percentual = 0.2 if aem_ativo else 0.0
    consumo_com_economia = consumo / (1 - economia_percentual)
    economia_por_km = preco_gasolina * (1/consumo - 1/consumo_com_economia)
    economia_mensal = economia_por_km * 2000

    st.success(f"Com economia: {consumo_com_economia:.2f} km/l")
    st.info(f"Economia por km: R$ {economia_por_km:.3f}")
    st.warning(f"Projeção mensal: R$ {economia_mensal:.2f}")

    # Simulador
    velocidade = st.slider("Velocidade (km/h)", 0, 120, 0)
    rpm = int((velocidade / 85) * 11000)
    tps = random.randint(10, 70)
    potencia = round((tps / 100) * 100, 1)
    marcha = min(1 + velocidade // 15, 5)
    distancia = round(velocidade / 60, 2)

    st.subheader("📊 Dados em tempo real")
    col1, col2, col3 = st.columns(3)
    col1.metric("RPM", rpm)
    col2.metric("Marcha", marcha)
    col3.metric("TPS", f"{tps}%")

    col4, col5 = st.columns(2)
    col4.metric("Potência", f"{potencia}%")
    col5.metric("Distância estimada (1 min)", f"{distancia} km")

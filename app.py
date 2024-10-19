import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Cabeçalhos de entrada
st.header("Gráfico de Burndown")
sprint = st.text_input("Sprint", "Sprint 1")
total_horas = st.number_input("Total de Horas", value=120, step=1)
quantidade_dias = st.number_input("Quantidade de Dias", value=10, step=1)

# Cálculos para o burndown
horas_estimadas = total_horas
horas_por_dia = 12
dias = list(range(quantidade_dias + 1))
estimado = [horas_estimadas - horas_por_dia * i for i in dias]

# Simulação de horas restantes (aqui você pode substituir por dados reais)
restante = [horas_estimadas - (10 * i) for i in dias]  # Simulação

# Criando o DataFrame para o gráfico
df = pd.DataFrame({
    "Dias": dias,
    "Estimado": estimado,
    "Restante": restante
})

# Plotando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df["Dias"], df["Estimado"],
         label="Estimado", color="blue", marker='o')
plt.plot(df["Dias"], df["Restante"], label="Restante", color="red", marker='o')
plt.title(f"Burndown Chart - {sprint}")
plt.xlabel("Dias")
plt.ylabel("Horas")
plt.legend()

# Mostrando o gráfico no Streamlit
st.pyplot(plt)

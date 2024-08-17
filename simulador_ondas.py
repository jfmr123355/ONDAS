import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def calcular_onda(opcion, valor1, valor2=None):
    if opcion == 1:  # Calcular frecuencia
        v = valor1
        λ = valor2
        f = v / λ
        descripcion = f"La frecuencia es {f:.2f} Hz"

    elif opcion == 2:  # Calcular longitud de onda
        v = valor1
        f = valor2
        λ = v / f
        descripcion = f"La longitud de onda es {λ:.2f} metros"

    elif opcion == 3:  # Calcular velocidad de la onda
        f = valor1
        λ = valor2
        v = f * λ
        descripcion = f"La velocidad de la onda es {v:.2f} m/s"

    elif opcion == 4:  # Calcular periodo
        v = valor1
        λ = valor2
        T = λ / v
        f = 1 / T
        descripcion = f"El periodo es {T:.2f} segundos"

    else:
        descripcion = "Opción no válida"
        st.write(descripcion)
        return

    st.write(descripcion)

    # Generar una representación gráfica de la onda
    if opcion == 1:  # Frecuencia dada
        f = valor1
        λ = valor2

    elif opcion == 2:  # Longitud de onda dada
        λ = valor1
        f = valor2

    elif opcion == 3:  # Velocidad dada
        λ = valor2
        f = valor1

    elif opcion == 4:  # Periodo dado
        T = valor1
        f = 1 / T
        λ = valor2

    # Generar la gráfica
    x = np.linspace(0, 2.5 * λ, 1000)  # Mostrar 2.5 longitudes de onda
    y = np.sin(2 * np.pi * x / λ)    # Función seno ajustada a la longitud de onda

    # Configurar la gráfica
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title(f"Representación gráfica de una onda con frecuencia {f:.2f} Hz y longitud de onda {λ:.2f} m")
    ax.set_xlabel("Posición (metros)")
    ax.set_ylabel("Amplitud")
    ax.grid(True)
    st.pyplot(fig)

# Aplicación Streamlit
st.title("Simulador de Onda")

opcion = st.radio(
    "Selecciona la opción que quieres calcular:",
    [1, 2, 3, 4],
    format_func=lambda x: {
        1: "Calcular Frecuencia",
        2: "Calcular Longitud de Onda",
        3: "Calcular Velocidad",
        4: "Calcular Periodo"
    }[x]
)

if opcion == 1:
    st.write("Para calcular la frecuencia, debes ingresar:")
    st.write("- Velocidad de la onda (m/s)")
    st.write("- Longitud de onda (m)")
    valor1 = st.number_input("Velocidad de la onda (m/s)", format="%.2f")
    valor2 = st.number_input("Longitud de onda (m)", format="%.2f")

elif opcion == 2:
    st.write("Para calcular la longitud de onda, debes ingresar:")
    st.write("- Velocidad de la onda (m/s)")
    st.write("- Frecuencia (Hz)")
    valor1 = st.number_input("Velocidad de la onda (m/s)", format="%.2f")
    valor2 = st.number_input("Frecuencia (Hz)", format="%.2f")

elif opcion == 3:
    st.write("Para calcular la velocidad de la onda, debes ingresar:")
    st.write("- Frecuencia (Hz)")
    st.write("- Longitud de onda (m)")
    valor1 = st.number_input("Frecuencia (Hz)", format="%.2f")
    valor2 = st.number_input("Longitud de onda (m)", format="%.2f")

elif opcion == 4:
    st.write("Para calcular el periodo, debes ingresar:")
    st.write("- Longitud de onda (m)")
    st.write("- Velocidad de la onda (m/s)")
    valor1 = st.number_input("Longitud de onda (m)", format="%.2f")
    valor2 = st.number_input("Velocidad de la onda (m/s)", format="%.2f")

if st.button("Calcular"):
    if valor1 and valor2 is not None:
        calcular_onda(opcion, valor1, valor2)
    else:
        st.write("Por favor, ingresa todos los valores necesarios.")

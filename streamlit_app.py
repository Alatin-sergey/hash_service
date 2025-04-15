import streamlit as st
import requests
import os

# Адрес FastAPI приложения
#FASTAPI_URL = "http://localhost:8000"
FASTAPI_URL = os.environ.get("FASTAPI_URL", "http://localhost:8000")

st.title("Hashing number")

number = st.number_input("Enter a number", value=0, step=1)
method = st.selectbox("Choose a hashing algorithm", ["div", "multi", "universal", "sha_256"])

if st.button("Calculate"):
    try:
        # Отправляем запрос к FastAPI
        response = requests.get(f"{FASTAPI_URL}/hash/{method}/{number}")

        # Проверяем статус код ответа
        if response.status_code == 200:
            # Получаем JSON-ответ
            data = response.json()
            # Отображаем результат
            st.write(f"Hash value (hashing algorithm {method}): {data['hash']}")
        else:
            # Отображаем сообщение об ошибке
            st.error(f"Error: {response.status_code} - {response.json()['detail']}")

    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to FastAPI: {e}")
    except Exception as e:
        st.error(f"An unexpected error has occurred: {e}")
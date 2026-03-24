import requests
import streamlit as st

BASE_URL = "http://localhost:8888"  # change if needed


def safe_parse_response(response):
    try:
        data = response.json()
        print("DEBUG RESPONSE:", data)

        # Case 1: dict with nested content
        if isinstance(data, dict):
            if isinstance(data.get("output"), dict):
                return data["output"].get("content", str(data))
            return data.get("output", str(data))

        # Case 2: plain string
        return str(data)

    except Exception as e:
        return f"Error parsing response: {e}"


def get_mistral_response(input_text):
    try:
        response = requests.post(
            f"{BASE_URL}/proverb/invoke",
            json={"input": {"topic": input_text}},
            timeout=120
        )
        return safe_parse_response(response)

    except Exception as e:
        return f"Backend Error: {e}"


def get_gemma_response(input_text):
    try:
        response = requests.post(
            f"{BASE_URL}/essay/invoke",
            json={"input": {"topic": input_text}},
            timeout=120
        )
        return safe_parse_response(response)

    except Exception as e:
        return f"Backend Error: {e}"


# -----------------------------
# Streamlit UI
# -----------------------------

st.title('Dual ChatBot(Mistral & Gemma) using Langchain & Langserve!!')

input_text = st.text_input("Write a proverb on")
input_text1 = st.text_input("Write an essay on")

if input_text:
    st.write(get_mistral_response(input_text))

if input_text1:
    st.write(get_gemma_response(input_text1))
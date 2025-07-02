
from query_gen import generate_sql_query
from db_exe import execute_sql_query
from config import schema_description
import requests
import threading
from langdetect import detect
from flask import Flask, request, jsonify

# ----------------------
# FLASK APP + ENDPOINTS
# ----------------------
app = Flask(__name__)
OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_natural_response(user_question, sql_query, results, temperature=0.3):
    detected_lang = detect(user_question)

    if detected_lang == "es":
        prompt = f"""
Eres un asistente amigable que responde en español de forma clara y concisa.
Dado el resultado de una consulta SQL, devuelve una respuesta natural que le diga al usuario lo que encontró.

Pregunta del usuario:
{user_question}

Consulta SQL generada:
{sql_query}

Resultado de la consulta:
{results}

Regresa solo una respuesta clara en español, sin mencionar la consulta SQL.
"""
    else:
        prompt = f"""
You are a friendly assistant who responds clearly and naturally in English.
Given the result of an SQL query, provide a natural answer that tells the user what was found.

User question:
{user_question}

Generated SQL query:
{sql_query}

Query result:
{results}

Only return a clear response in English, with a human tone, without mentioning SQL or query details.
"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "temperature": temperature,
        "stream": False,
        "max_tokens": 250
    }

    try:
        response = requests.post("http://localhost:11434/api/generate", json=payload)
        response.raise_for_status()
        return response.json()["response"].strip()
    except Exception as e:
        return f"(Error generando respuesta natural: {e})"

@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("message")
    print("Question",question)
    if not question:
        return jsonify({"error": "Missing 'message' field"}), 400

    try:
        sql = generate_sql_query(question, schema_description)
        results = execute_sql_query(sql)
        natural = generate_natural_response(question, sql, results)
        print("Natural",natural)
        return jsonify({
            "sender": "bot",
            "message": natural
        })
    except Exception as e:
        return jsonify({"sender": "bot", "message": str(e)}), 500

@app.route("/api/generate-sql", methods=["POST"])
def generate_sql():
    data = request.get_json()
    question = data.get("message")
    if not question:
        return jsonify({"error": "Missing 'message' field"}), 400

    try:
        sql = generate_sql_query(question, schema_description)
        return jsonify({"sender": "bot", "message": sql})
    except Exception as e:
        return jsonify({"sender": "bot", "message": str(e)}), 500

def start_flask():
    app.run(host="0.0.0.0", port=5001, debug=False)

# ----------------------
# MODO CONSOLA INTERACTIVA
# ----------------------
def main():
    # Iniciar la API en segundo plano
    threading.Thread(target=start_flask, daemon=True).start()
    print("🔌 API Flask corriendo en http://localhost:5001")

    while True:
        natural_language_query = input(" Tu consulta: ").strip()

        if natural_language_query.lower() in ["salir", "exit", "quit"]:
            print("\n adiós user.")
            break

        try:
            sql_query = generate_sql_query(natural_language_query, schema_description)
            print("\n Consulta generada:")
            print(sql_query)

            result = execute_sql_query(sql_query)

            print("\n Resultado de la consulta:")
            if result:
                for row in result:
                    print(row)
            else:
                print("Sin resultados.")

            natural_response = generate_natural_response(natural_language_query, sql_query, result)
            print("\n Respuesta natural:")
            print(natural_response)
            print("\n" + "-"*60 + "\n")

        except Exception as e:
            print(f" Error: {str(e)}\n")

if __name__ == "__main__":
    main()

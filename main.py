from query_gen import generate_sql_query
from db_exe import execute_sql_query
from config import schema_description
# import ollama
import requests

def generate_natural_response(user_question, sql_query, results, temperature=0.3):
    prompt = f"""
Eres un asistente amigable que responde en español de forma clara y concisa.
Dado el resultado de una consulta SQL, devuelve una respuesta natural que le diga al usuario lo que encontró.

Pregunta del usuario:
{user_question}

Consulta SQL generada:
{sql_query}

Resultado de la consulta:
{results}

Regresa solo una respuesta clara en español, con un tono humano, sin mencionar la consulta SQL.
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

def main():
    # print("\n Asistente de base de datos - Haz tus preguntas en lenguaje natural.")
    # print("Escribe 'salir' para terminar.\n")

    while True:
        natural_language_query = input(" Tu consulta: ").strip()

        if natural_language_query.lower() in ["salir", "exit", "quit"]:
            print("\n adios user.")
            break

        try:
            # Generar SQL
            sql_query = generate_sql_query(natural_language_query, schema_description)
            print("\n Consulta generada:")
            print(sql_query)

            # Ejecutar SQL
            result = execute_sql_query(sql_query)

            print("\n Resultado de la consulta:")
            if result:
                for row in result:
                    print(row)
            else:
                print("Sin resultados.")

            # Respuesta en lenguaje natural
            natural_response = generate_natural_response(natural_language_query, sql_query, result)
            print("\n Respuesta natural:")
            print(natural_response)
            print("\n" + "-"*60 + "\n")

        except Exception as e:
            print(f" Error: {str(e)}\n")

if __name__ == "__main__":
    main()

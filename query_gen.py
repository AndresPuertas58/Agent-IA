import ollama 
import re

def generate_sql_query(natural_language_query, schema_description):

    """
    Genera una consulta SQL valida a partir de una pregunta en lenguaje natural.
    """


    prompt = f"""
You are an expert SQL generator, Givin a user's question and the schema, respond ONLY with the SQL query.

Shema:
{schema_description}

User's question: 
{natural_language_query}

"""
    response = ollama.generate(model="llama3:latest", prompt=prompt)
    raw_sql = response["response"].strip()

    cleaned_sql = re.sub(r"^```(?:sql)?\s*|\s*```$", "", raw_sql.strip(), flags=re.IGNORECASE | re.MULTILINE)
    
    return cleaned_sql
import ollama

def explaint_result(natural_question, sql_query, result):
    prompt = f"""
You are a helpful assistant. Based on the user's question, the SQL query and the result, explain clearly

Question: {natural_question}
SQL Query: {sql_query}
Result: {result}


respond in natural language(Spanish).
"""
    response = ollama.generate(model="llama3:latest", prompt=prompt)
    return response["response"].strip()
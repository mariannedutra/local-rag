from query import query_rag
from langchain_community.llms.ollama import Ollama

EVAL_PROMPT = """
Modelo de resposta correta: {expected_response}
Resposta recebida: {actual_response}
----- 
(Responda com 'true' ou 'false') A resposta recebida está de acordo com o modelo de resposta correto? 
"""

def query_and_validate(question: str, expected_response: str):
    response_text = query_rag(question)
    prompt = EVAL_PROMPT.format(
        expected_response=expected_response, actual_response=response_text
    )

    model = Ollama(model="llama3:8b-instruct-q8_0",base_url="http://localhost:11434")
    evaluation_results_str = model.invoke(prompt)
    evaluation_results_str_cleaned = evaluation_results_str.strip().lower()

    if "true" in evaluation_results_str_cleaned:
        print("\033[92m" + f"Resposta: {evaluation_results_str_cleaned}" + "\033[0m")
        return True
    elif "false" in evaluation_results_str_cleaned:
        print("\033[91m" + f"Resposta: {evaluation_results_str_cleaned}" + "\033[0m")
        return False
    else:
        raise ValueError(
            f"Resultado inválido. Não é possível determinar se é verdadeiro ou falso."
        )

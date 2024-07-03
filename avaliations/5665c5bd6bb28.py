from avaliation import query_and_validate


def test_11():
    assert query_and_validate(
        question="Qual autor de SentimentALL: Ferramenta para Análise de Sentimentos em Português?",
        expected_response="William Christhie Caproni de Oliveira.",
    )
def test_12():
    assert query_and_validate(
        question="Qual a banca examinadora do trabalho de William Christhie Caproni de Oliveira?",
        expected_response="Parcilene Fernandes de Brito (Orientadora),Jackson Gomes de Souza e Fabiano Fagundes",
    )
def test_13():
    assert query_and_validate(
        question="Qual é o nome da ferramenta apresentada no TCC de William Christhie Caproni de Oliveira?",
        expected_response="SentimentALL.",
    )
def test_14():
    assert query_and_validate(
        question="Quais lexicons de sentimentos foram utilizados no protótipo da ferramenta SentimentALL para análise de sentimentos?",
        expected_response="SentiLex e LIWC.",
    )
def test_15():
    assert query_and_validate(
        question="Descreva o processo de desenvolvimento e teste da ferramenta SentimentALL, incluindo as tecnologias e métodos usados, conforme apresentado no resumo.",
        expected_response= "Desenvolvimento do Protótipo: "
                            "Linguagem de programação: Java. "
                            "API do corretor ortográfico: CogrOO. "
                            "Lexicons de sentimentos: SentiLex e LIWC. "
                            "Processo de Teste: "
                            "Contexto: Turismo, especificamente comentários sobre atrações, hotéis e restaurantes de destinos turísticos brasileiros. "
                            "Corpus: Quase um milhão e meio de comentários extraídos do site Trip Advisor. "
                            "Ferramentas usadas: "
                            "Para extração de dados: Import.IO. "
                            "Para transformação de dados: Kettle – Spoon. "
                            "Para armazenamento: SGBD SQL Server. "
                            "Análise: Incluiu a normalização, o Processamento de Linguagem Natural (PLN) e a Análise de Sentimentos no nível de aspectos."
)
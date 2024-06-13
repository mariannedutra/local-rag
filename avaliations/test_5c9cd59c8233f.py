from avaliation import query_and_validate

def test_01():
    assert query_and_validate(
        question="Qual nome do autor de Utilização de Redes Neurais Artificiais para Controlar um Agente em um Jogo de Estratégia em Tempo Real?",
        expected_response="Haroldo Fernando Fritsch.",
    )
def test_02():
    assert query_and_validate(
        question="Qual a banca examinadora do trabalho de Haroldo Fernando Fritsch?",
        expected_response="Jackson Gomes de Souza (Orientador), Parcilene Fernandes de Brito, Edeílson Milhomem da Silva",
    )
def test_03():
    assert query_and_validate(
        question="Qual é o nome do jogo usado como ambiente para a aplicação das Redes Neurais Artificiais no TCC de Haroldo Fernando Fritsch?",
        expected_response="Starcraft",
    )
def test_04():
    assert query_and_validate(
        question="Qual é o nome do algoritmo de aprendizagem supervisionada utilizado no desenvolvimento do NPC no trabalho de Haroldo Fernando Fritsch?",
        expected_response="Algoritmo backpropagation",
    )
def test_05():
    assert query_and_validate(
        question="Quais são os principais desafios mencionados no trabalho ao utilizar jogos de estratégia em tempo real como plataforma para testes e validação de métodos e algoritmos de Inteligência Artificial?",
        expected_response="Estratégia de coleta e alocação de recursos",
    )
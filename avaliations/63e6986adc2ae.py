from avaliation import query_and_validate


def test_06():
    assert query_and_validate(
        question="Qual o autor de Ferramenta para Anotação de Entidades Nomeadas?",
        expected_response="Vinícius Dias dos Santos",
    )
def test_07():
    assert query_and_validate(
        question="Qual a banca examinadora do trabalho de Vinícius Dias dos Santos?",
        expected_response="Fábio Castro Araújo (Orientador),Jackson Gomes de Souza, Parcilene Fernandes de Brito",
    )
def test_08():
    assert query_and_validate(
        question="Qual é o nome da ferramenta apresentada no TCC de Vinícius Dias dos Santos?",
        expected_response="Ferramenta para Anotação de Entidades Nomeadas.",
    )
def test_09():
    assert query_and_validate(
        question="Quais são as tecnologias e bibliotecas utilizadas na construção da ferramenta web para anotação de entidades nomeadas mencionadas no resumo?",
        expected_response="O framework Angular e as bibliotecas Angular Material e PrimeNG.",
    )
def test_10():
    assert query_and_validate(
        question="Descreva as funcionalidades dos três módulos desenvolvidos na ferramenta para anotação de entidades nomeadas mencionados no resumo de Vinícius Dias dos Santos.",
        expected_response="Módulo de barra de navegação: Controla a navegação e gera o arquivo de exportação de entidades."
        "Módulo de categorias: Gerencia as categorias que o usuário utiliza para classificar entidades. "
        "Módulo de anotação: Disponibiliza as funcionalidades para que o usuário anote entidades no texto."
    )
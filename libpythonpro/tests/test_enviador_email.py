import pytest

from libpythonpro.spam.enviador_email import Enviador


def test_enviador_email():
    enviador = Enviador()
    assert enviador is not None


# Teste parametrizado.
# Esse tipo de teste é usado quando é preciso testar vários parâmetros dentro do método.
@pytest.mark.parametrize(
    'remetente',
    ['dacio@email.com', 'foo@bar.com.br']
)
def test_remetente_email(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'suporte@email.com',
        'Análise de conteúdo',
        'Relatório de análise de conteúdo'
    )
    assert remetente in resultado

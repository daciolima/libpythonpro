import pytest

from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='dacio', email='dacio@email.com.br'),
            Usuario(nome='wal', email='wal@email.com.br'),

        ],
        [
            Usuario(nome='dacio', email='dacio@email.com.br'),
        ]
    ]
)
def test_qtd_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_spam = EnviadorSpam(sessao, enviador)
    enviador_spam.enviar_emails(
        'dacio@email.com.br',
        'Curso Python',
        'Configura o conteúdo'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_spam(sessao):
    usuario = Usuario(nome='dacio', email='dacio@email.com.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_spam = EnviadorSpam(sessao, enviador)
    enviador_spam.enviar_emails(
        'wal@email.com.br',
        'Curso Python',
        'Configura o conteúdo'
    )
    assert enviador.parametros_envio == (
        'wal@email.com.br',
        'dacio@email.com.br',
        'Curso Python',
        'Configura o conteúdo'
    )

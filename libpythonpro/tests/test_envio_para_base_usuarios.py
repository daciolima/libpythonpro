from unittest.mock import Mock

import pytest

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
    enviador = Mock()
    enviador_spam = EnviadorSpam(sessao, enviador)
    enviador_spam.enviar_emails(
        'dacio@email.com.br',
        'Curso Python',
        'Configura o conteúdo'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_spam(sessao):
    usuario = Usuario(nome='dacio', email='dacio@email.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_spam = EnviadorSpam(sessao, enviador)
    enviador_spam.enviar_emails(
        'wal@email.com.br',
        'Curso Python',
        'Configura o conteúdo'
    )
    enviador.enviar.assert_called_once_with(
        'wal@email.com.br',
        'dacio@email.com.br',
        'Curso Python',
        'Configura o conteúdo'
    )

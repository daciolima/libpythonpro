from libpythonpro.spam.enviador_email import Enviador
from libpythonpro.spam.main import EnviadorSpam


def test_envio_spam(sessao):
    enviador_spam = EnviadorSpam(sessao, Enviador())
    enviador_spam.enviar_emails(
        'dacio@email.com.br',
        'Curso Python',
        'Configura o conteúdo'
    )

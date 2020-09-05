from libpythonpro.spam.modelos import Usuario


# @pytest.fixture(scope='function')  # Uma única instância a cada função do modulo(arquivo)
# @pytest.fixture(scope='session')  # Uma única instância no modulo e para todos os relacionados a este.


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='dacio', email='dacio@email.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='dacio', email='dacio@email.com.br'),
                Usuario(nome='wal', email='wal@email.com.br')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

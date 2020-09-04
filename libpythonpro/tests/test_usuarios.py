from libpythonpro.spam.modelos import Usuario


# @pytest.fixture(scope='function')  # Uma única instância a cada função do modulo(arquivo)
# @pytest.fixture(scope='session')  # Uma única instância no modulo e para todos os relacionados a este.


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='dacio')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='dacio'), Usuario(nome='wal')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

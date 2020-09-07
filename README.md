# Repositório de exemplo do projeto PyTools.
##### Conteúdo sobre:
> - Criação de lib, config de setup e upload para site https://pypi.org
> - Exercícios de testes unitários com pytest e pytest.fixture
> - Integração Contínua com o travis-CI.
> - Verificação de código dentro das recomedações pep8 com flake8.
> - Estatística de código testados com o pyup.
> - Gerenciador de ambiente com o pipenv.

[![Build Status](https://travis-ci.org/daciolima/libpythonpro.svg?branch=master)](https://travis-ci.org/daciolima/libpythonpro)
[![Updates](https://pyup.io/repos/github/daciolima/libpythonpro/shield.svg)](https://pyup.io/repos/github/daciolima/libpythonpro/)
[![Python 3](https://pyup.io/repos/github/daciolima/libpythonpro/python-3-shield.svg)](https://pyup.io/repos/github/daciolima/libpythonpro/)
[![codecov](https://codecov.io/gh/daciolima/libpythonpro/branch/master/graph/badge.svg)](https://codecov.io/gh/daciolima/libpythonpro)
##### Para instalar o setup da lib como teste:
> - Criar um .venv de teste para lib, ativar e depois rodar o comando; 
```console
pip install -e <path_diretorio_file_setup>
```

Alguns comandos git: 
1 - Os comandos tags serve para gerar tags no seu projeto
servindo também como nota de release(versão). 
```console
git tag <Nome da Tag>
git push --tags
```
2 - Para gerar o arquivo da lib pra enviar ao pypi.org
deve-se após todas as configurações e testes roda o comando:
```console
python setup.py sdist
```
2.1 - Também para subir o arquivo para o pypi.org deve
instalar a dependência: pip install twine.
2.2 - Após a instalação rode o comando do terminal para realizar o 
upload da lib para o pypi.org. DA forma abaixo será enviado todos os arquivos 
dentro do diretório dist.
```console
twine upload dist/*
```
3 - Rodando o pytest
```console
pytest <Nome_Diretorio_Package>
```
4 - Medidor de cobertura de teste
```console
pytest libpythonpro --cov=<Pasta_raiz_de_teste>
```

#### Arquivos de confs
> - .travis.yml -> Contém as confs de integração contínua do travis-ci;
> - .pyup.yml -> Confs do medidor de código testados;
> - .flake8 -> Conf para análise de código dentro das recomendações pep8;
> - setup.py -> Arquivo para empacotar a lib a ser enviada para o pypi.org;
> - MANIFEST.in -> Contém informações a serem carregadas na criação da lib pelo setup.py;
> - LICENSE -> Guarda informação da licença da lib;
> - Pipfile e Pipfile.lock -> Arquivo de confs do gerenciador de ambiente pipenv.
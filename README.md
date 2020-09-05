# Repositório de exemplo do projeto PyTools.
# Conteúdo de exercício de testes e CI.

[![Build Status](https://travis-ci.org/daciolima/libpythonpro.svg?branch=master)](https://travis-ci.org/daciolima/libpythonpro)
[![Updates](https://pyup.io/repos/github/daciolima/libpythonpro/shield.svg)](https://pyup.io/repos/github/daciolima/libpythonpro/)
[![Python 3](https://pyup.io/repos/github/daciolima/libpythonpro/python-3-shield.svg)](https://pyup.io/repos/github/daciolima/libpythonpro/)
[![codecov](https://codecov.io/gh/daciolima/libpythonpro/branch/master/graph/badge.svg)](https://codecov.io/gh/daciolima/libpythonpro)
##### Para instalar o setup da libcomo teste:
> - Crie um venv de teste e ative-a;
> - Rode o comando: 
```console
pip install -e <path_diretorio_file_setup>
```

COMANDOS: 
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

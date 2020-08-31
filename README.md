# Repositório de exemplo do projeto PyTools.
# Confs de travis-ci, pyup e arquivos requirements!

[![Build Status](https://travis-ci.org/daciolima/libpythonpro.svg?branch=master)](https://travis-ci.org/daciolima/libpythonpro)
[![Updates](https://pyup.io/repos/github/daciolima/libpythonpro/shield.svg)](https://pyup.io/repos/github/daciolima/libpythonpro/)
[![Python 3](https://pyup.io/repos/github/daciolima/libpythonpro/python-3-shield.svg)](https://pyup.io/repos/github/daciolima/libpythonpro/)

##### Para instalar o setup da libcomo teste:
> - Crie um venv de teste e ative-a;
> - Rode o comando: 
```console
pip install -e <path_diretorio_file_setup>
```

OBS: 
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

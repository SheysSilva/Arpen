#CONSULTA ATF
###### Empresa: **Contagil**

Este projeto tem como finalidade gerar consultas automaticas no sistema de Administração Tributária e Financeira([ATF](https://www4.receita.pb.gov.br/atf/)), pertencente a Secretaria de Estado da Fazenda.

Instalação pelo terminal

```
pip install selenium
pip install pytest
pip install datatime
```

###Instalação automatica (Linux)

> Abra o arquivo e mude a rota de acesso ao seu projeto.

Acesse a pasta [install](/install) e execute o arquivo install.sh

###Instalação automatica (Windows)

> Abra o arquivo e mude a rota de acesso ao seu projeto.

Acesse a pasta [install](/install) e execute o arquivo install.bat

_Obs: Caso não funcione a instalação automatica no windows, tente por linha de comando no terminal após realizar as devidas configurações no sistema._

###Para fazer a solicitação dos arquivos no ATF

Acesse o terminal do seu sistema operacional e rode o comando abaixo.

```
python solicitation.py
```

Ou execute os seguintes arquivos abaixo de acordo com o seu sistema operacional.

######Linux

Acesse a pasta [run](/run) e execute o arquivo run_solicitation.sh

######Windows

Acesse a pasta [run](/run) e execute o arquivo run_solicitation.bat


###Para fazer o download dos arquivos solicitados

Acesse o terminal do seu sistema operacional e rode o comando abaixo.

```
python download.py
```

Ou execute os seguintes arquivos abaixo de acordo com o seu sistema operacional.

######Linux

Acesse a pasta [run](/run) e execute o arquivo run_download.sh

######Windows

Acesse a pasta [run](/run) e execute o arquivo run_download.bat


######Site: [Contagil]()
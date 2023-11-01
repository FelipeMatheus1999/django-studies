# Django Studies

<br>

## Descrição
> Projeto que desenvolvi estudando ***Django*** e aplicando conceitos que acho interressantes levar para os projetos que trablaho.

<br>

## Como rodar o projeto?
> __Primeiro Passo__ <br> <br>
> Crie um arquivo ***.env*** para configurar a aplicação. <br>
> Use o arquivo ***.env.example*** para configurar corretamente as variáveis. <br><br>
> __Segundo Passo__ <br> <br>
> User o comando ***make build*** para construir os container da aplicação. <br><br>
>  __Terceiro Passo__ <br><br>
> User o commando ***make run*** para subir o servidor na porta __8000__.

<br>

## Possíveis problemas
> __Falta do volume docker - django-studies_pg_data__  <br><br>
> Se o servidor não subir na porta 8000 reclamando que não existe volume, use ***sudo docker volume create django-studies_pg_data***. <br><br>
> __Erros ao usar comandos Make__ <br><br>
> Certifique-se de instalar o ***Make*** no seu terminal, isso pode gerar erro ao tentar executar os comandos ***Make*** <br><br>
> Ex:
> ```python
> user@P58TRV8: make -version
> GNU Make 4.3
> Built for x86_64-pc-linux-gnu
> Copyright (C) 1988-2020 Free Software Foundation, Inc.
> License GPLv3+: GNU GPL version 3 or later <http://gnu.> org/licenses/gpl.html>
> This is free software: you are free to change and
> redistribute it.
> There is NO WARRANTY, to the extent permitted by law. 
>```
> Se make não estiver instalado você pode fazer isso:
> ```
> sudo apt update
> sudo apt upgrade
> sudo apt install make
> ```
> Outo problema que pode acontecer é você não possuir o plugin do ***docker compose***, se olhar no arquivo ***Makefile*** todos os comandos do docker não usando o ```-``` para uniar as duas palavras, isso acontece pois o plugin do ***docker compose*** facilita a nossa escrita.
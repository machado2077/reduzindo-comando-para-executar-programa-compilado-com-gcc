# REDUZINDO O COMANDO PARA EXECUTAR CÓDIGO COMPILADO COM GCC.

## Sobre o Projeto

Esse programa consiste em facilitar o comando via terminal utilizado para compilar e executar códigos em C utilizando o compilador GCC.

## Por que?
O programa foi concebido a partir da necessidade de facilitar o processo de execução de um programa em C. O comando em um emulador de terminal, no caso o bash, é algo do tipo:

```bash
$ gcc programa.c -o programa && ./programa
```

O objetivo seria parametrizar o nome do programa em apenas um comando que iria compilar e executar este. A seguir, o protótipo:

```bash
$ <meu_alias> programa.c
```

## Como executar.

### Pré-requisitos:
- Python 3
- Compilador GCC

Após clonar esse repositório, acesse o diretório local correspondente, acesse o seu emulador de terminal e insira o comando do tipo:

```bash
$ python3 main.py <caminho para o arquivo em C>
```

É possível também atribuir um outro nome para o código C executável, passando o nome como segundo parametro ao rodar o programa em python:

```bash
$ python3 main.py <caminho para o arquivo em C> <novo nome do executável>
```
Após isto, é conveniente criar um alias para o comando python que invoca o módulo main.py, a fim e dar maior praticidade.
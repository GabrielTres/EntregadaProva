![GitHub top language](https://img.shields.io/github/languages/top/mdietterle/prova_testes_2024)

# Prova de Testes de Software

Você irá clonar o repositório em https://github.com/mdietterle/prova_testes_2024, e irá criar testes de software para as funções constantes no arquivo `stat_funcs.py`

O arquivo `main.py` contém chamadas às funções constantes em `stat_funcs.py` para demonstrar que elas são funcionais, ou seja, retornam valores.

## Atividades da avaliação:

1.  Os testes devem ser criados dentro da pasta testes.
2.  Editar o arquivo `conftest.py` para criar fixtures e outros itens que você julgar que devam estar no arquivo.
3.  Existe um ***pequeno erro*** (proposital) que você deve localizar e corrigir para que os testes funcionem. Também existem **pequenas alterações** que você deverá fazer no arquivo `main.py` caso queira executar as funções diretamente para entender seu funcionamento.
4. Implementar testes para cada função constante em `stat_funcs.py` em um arquivo separado.
5.  Deve ser possível executar TODOS os testes usando o comando `pytest`  (sem parâmetros) na raiz do projeto.
6.  Você deverá usar anotações de parametrização (**parametrize**) de testes em ao menos um teste de cada função, para repetir o mesmo teste com vários valores diferentes.
7.  Importante criar anotações nas funções de testes para que os testes possam ser executados em grupos (**mark**).
8.  Criar ao menos um teste de falha esperada (**xfail**) em cada arquivo de testes. 
9.  A entrega da avaliação será feita via **github**, e você irá anexar o link para o repositório na atividade do teams que será aberta.
    

## IMPORTANTE:

- A prova será avaliada somente via link do github. **QUALQUER OUTRO MEIO DE ENTREGA SERÁ DESCONSIDERADO.**  
- O commit que será avaliado deve ter a mensagem “**Entrega da prova**”
-   Caso seja detectado um commit feito após as **22h 20min** do dia da avaliação (hora limite para entrega da avaliação), ela não será corrigida e será atribuída nota 0 (ZERO) à avaliação
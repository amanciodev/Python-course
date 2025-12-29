# O QUE É O GIT?

O Git é um sistema de **Controle de Versionamento de Arquivos**, em inglês, *Version Control System*.

Vamos supor que nós temos o nosso código e estamos trabalhando em um projeto, e em certo momento,
outra pessoa que está trabalhando nesse mesmo projeto pede para que você altere alguma parte do seu código.
Você altera, e depois a mesma pessoa fala que não precisava tirar, e que pode voltar com aquela parte que você removeu.

E agora?

É aí que o Git entra!! 🤩🤩

O Git nos permite ter controle de tudo o que já escrevemos no nosso código/projeto: qualquer alteração, até partes
que foram apagadas ou nomes de arquivos que foram renomeados.

Quando usamos Git, podemos ter múltiplas pessoas trabalhando no mesmo projeto e até no mesmo arquivo, sem que haja
nenhum conflito. Mesmo se cada um estar em sua casa, em países diferentes e sem comunicação prévia 🙏🙏


# E O QUE É O GITHUB?

O GitHub é uma plataforma para você hospedar seus projetos de programação, arquivos de configuração ou qualquer coisa
que você ache importante relacionada à programação.

Vamos dar uma olhadinha no GitHub...

**Coisas importantes para vermos no GitHub:**
1. Repositórios
2. Favoritar Repositórios
3. Forks
4. Pesquisas


# GIT BRANCH

O Branch é uma ramificação que vamos fazer no nosso projeto.
Branch significa **"ramificação"** em português.

Quando estamos desenvolvendo, podemos usar uma linha cronológica só.
Vamos dar um exemplo de uma ordem cronológica do desenvolvimento de uma página Web:

1. No primeiro dia criamos o cabeçalho da página, e subimos para o Git
2. No segundo dia criamos o corpo da página, e subimos para o Git
3. No terceiro dia criamos o rodapé da página, e subimos para o Git

A nossa ordem cronológica ficaria mais ou menos assim:

| Criei o rodapé
| Criei o corpo
| Criei o cabeçalho


Mas nós temos a possibilidade de não ficarmos postando tudo na mesma linha cronológica e criar ramificações (branches)
do nosso projeto. Vamos ver um exemplo mais complexo da nossa página:

|______ Merge
|______ Criei a página de produtos
|______ Criei a página de contatos
|______ Adicionei imagem de fundo
| Criei o rodapé
| Criei o corpo
| Criei o cabeçalho


Mas por quê criamos branches?

Em projetos maiores e mais complexos, é boa prática termos diversas linhas cronológicas para cada alteração, e no fim,
juntamos todas na linha cronológica principal. Isso evita (ou diminui as chances) dos famosos
**MERGE CONFLICTS** 😱😱


# PALAVRINHAS COMUNS QUANDO NOS REFERIMOS AO GIT

## 1. Commit
O nosso GitHub não atualiza automaticamente o nosso repositório se nós só alterarmos o nosso código no nosso computador.
Nós precisamos usar o comando **Commit** para isso.

É como se estivéssemos salvando o nosso código e falando:

> "Git, essa é a nova versão do meu projeto. Salve ela, por favor!!"


## 2. Push
O Push é o comando que usamos para **enviar** o nosso código do nosso computador para o GitHub.

Ou seja, quando nós fazemos alterações no nosso projeto, damos Commit, mas
**O CÓDIGO AINDA ESTÁ SÓ NA NOSSA MÁQUINA**.

Quando usamos Push, estamos falando para o Git:

> "Git, pode mandar tudo isso que eu acabei de salvar para o GitHub, por favor!!"

Depois do Push, o nosso repositório no GitHub fica atualizado com a nova versão do projeto.
Se outra pessoa estiver trabalhando com você no mesmo projeto, ela só vai ver suas alterações
**depois que você fizer o Push**.


## 3. Pull
O Pull é o **oposto do Push**.
Ele serve para **baixar** as atualizações do GitHub para o nosso computador.

Vamos supor que outra pessoa do time fez alterações no projeto e deu Commit + Push.
O código novo está no GitHub, mas **não está ainda na nossa máquina**.

Se nós começarmos a programar antes do Pull, podemos estar escrevendo código novo em cima de código antigo,
e isso pode gerar conflitos no futuro.

Quando usamos o Pull, estamos falando:

> "Git, traz para mim tudo o que mudou no GitHub e atualiza meu projeto local."

Sempre que trabalhamos em equipe, é uma boa prática dar um Pull primeiro, para garantir que estamos trabalhando
com a versão mais atual do projeto.


## 4. Merge
O Merge é a ação de juntarmos uma branch em outra branch.
Uma linha cronológica em outra linha cronológica.

Imagine que temos a nossa linha cronológica principal e outra linha cronológica que criamos para resolver algum bug.
Quando o bug estiver resolvido, nós vamos querer juntar a linha cronológica do bug resolvido com a linha cronológica principal.

Essa ação de juntar duas ou mais linhas cronológicas é chamada de **MERGE**.


## 5. Local e Remote
O **Local** é a nossa máquina.
O **Remote** é o nosso GitHub.

Quando nós estamos desenvolvendo um projeto, temos o código na nossa máquina (repositório local).
Quando fazemos Commit e Push, o nosso código sai da nossa máquina e fica salvo no Remote, que no nosso caso é o GitHub.

Dessa maneira, podemos trocar de computador, excluir o projeto da nossa máquina, formatar o computador, voltar depois
de anos e ainda assim o nosso projeto sempre estará salvo, porque ele está salvo no GitHub.

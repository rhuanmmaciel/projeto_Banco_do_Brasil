# 2 - Pilha

A primeira estrutura de dados que vamos ver é a Pilha. A pilha é uma estrutura bastante simples que tem a seguinte característica: 

> Um elemento entra sempre pelo topo. Ao remover um elemento, só podemos removê-lo pelo topo. 

Essa característica significa dizer que não podemos remover imediatamente qualquer elementos desejado, é necessário obedecer esta ordem. Pense em uma pilha de pratos de louça que a nossa mãe tanto ama. Já pensou em remover um prato que está no meio da pilha e, por essa decisão, deixar cair os pratos de cima? Não queremos nem imaginar o problemão, em?

Logicamente que o mais pudente é retirar os pratos de cima um a um e colocar em algum outo lugar, até que possamos - com segurança - pegar o prato desejado. Então, vamos criar um algoritmo simples para modelar isso:

- Pega a pilha de pratos
- Remove o prato que está no topo desta pilha
- Coloca o prato do lado

Bem, isso deve se repetir até que cheguemos ao prato desejado, então...

- Pega a pilha de pratos
- Até chegar ao prato desejado
	- Remove o prato que está no topo desta pilha
	- Coloca o prato do lado

Quando chegar ao prato, devemos retirá-lo e usá-lo, além de recolocar os pratos no local (sim, somos organizados)! 

- Pega a pilha de pratos
- Até chegar ao prato desejado
	- Remove o prato que está no topo desta pilha
	- Coloca o prato do lado
- Pega o prato desejado
- Até que a pilha do lado seja esvaziada
	- Remover o prato que está no topo desta segunda pilha
	- Coloca o prato na pilha principal novamente

> Ufa! Não quebramos nenhum prato, pois seguimos o protocolo correto para a remoção segura. 

Basicamente esta é a ideia de pilha, você já deve ter entendido. Podemos então usar uma modelagem para essa situação. Como já conhecemos bem POO e gostamos de criar objetos, vamos pensar que o prato pode ser uma objeto do tipo Prato, ou de modo mais geral, um Item.  Outra coisa que devemos ter em mente é: *"devemos usar um vetor para armazenar muitos elementos, pois uma variável não daria conta!"*.

Então, temos:

- Uma classe Item;
- Um vetor.


Mas uma estrutura de dados não é formada apenas por locais onde podemos armazenar coisas ou objetos soltos no ar. Devemos criar operações que **garantam uma certa organização**, neste caso a organização da pilha: entra no topo, sai do topo. É interessante observar, caso ainda não tenha pensado nisso, que o elemento que entra do último é o primeiro a sair e o primeiro a entrar é o último a sair. Por esse motivo, a pilha é chamada de FILO (*First In, Last Out*).

Então, além dos dados, temos:

- Operação de inserir
- Operação de remover


### 2.1 - Inserindo dados em uma Pilha**

Mas como controlar que vou inserir no topo? Bem isso é simples, vamos pensar que temos um vetor de 10 elementos e no início todos são nulos. 

    [null, null, null, null, null, null, null, null, null, null]

Eu posso inserir na posição 0, ela será nosso topo.

    ["Prato A", null, null, null, null, null, null, null, null, null]

Se desejo inserir novamente, eu coloco todos os elemento para a a próxima posição e insiro na posição 0 novamente.

	["Prato B", "Prato A", null, null, null, null, null, null, null, null]


Você certamente já percebeu que eu precisaria transpor os elementos, posição por posição até disponibilizar um local vazio no início:

	int i = tamanho_pilha-1;
	while( (i > 0) && (pilha[i] = null) && (pilha[i-1] != null) )
		pilha[i] = pilha[i-1];
		i = i-1
 
	pilha[0] = "Prato C";


Nossa!!! Mas isso é muito custoso, não acha? Pense em uma Pilha de  1 milhão de dados. Quando tivermos ao menos 50% da Pilha com dados, teremos 500 mil alocações. No final, teremos 999.999 alocações, apenas para inserir um único elemento. **Nossa!!**.

**Usando um Topo**

Uma solução para esse problema é: criar uma variável que armazenará o valor (índice) do topo e assim, poderemos sempre inserir em uma posição vazia. No primeiro caso que apresentamos, o topo poderia ser -1 (pois a Pilha está vazia). Você deve pensar: "Mas na outra solução, se a inserção for no fundo, teríamos o mesmo resultado!". Não! Ainda seria preciso achar a posição vazia. 
	
	topo = -1
	[null, null, null, null, null, null, null, null, null, null]

Seguiremos:

	//inserindo o Prato A
	topo = 0
	["Prato A", null, null, null, null, null, null, null, null, null]
	//inserindo o Prato B
	topo = 1
	["Prato A", "Prato B", null, null, null, null, null, null, null, null]

Mas como ficaria esse algoritmo?

	topo++;
	pilha[topo] = "Prato C";

Só isso? Sim!!! Além de ter menos linhas, há menos necessidade de acesso aos dados. Agora, quando a pilha estiver com 50% de dados, teremos a mesma quantidade de operação que ele como 100% dos dados. **Que legal!!!**

### 2.2 - Removendo dados na Pilha

Analogicamente, na solução antiga precisaríamos percorrer todo o vetor até encontrar uma posição onde o próximo elemento é nulo, guardar este valor e colocar um valor nulo no local.

	["Prato A", "Prato B", "Prato C", "Prato D", null, null, null, null, null, null]

Vejamos:

- pilha na posição 0 é null?  // Não
- pilha na posição 1 é null?  // Não
- pilha na posição 2 é null?  // Não
- pilha na posição 3 é null?  // Não
- pilha na posição 4 é null?  // Sim
- guarde o valor da posição 3
- coloque null na posição 3
	
	["Prato A", "Prato B", "Prato C", null, null, null, null, null, null, null]

Sim, podemos usar o loop;
- n = 0
- Enquanto pilha na posição (n + 1)for diferente de null
	- n++
- Se n < tamanho da pilha
	- guarde o valor da posição n 
	- coloque null na posição n 


Já percebemos que essa solução não é ideal, por motivos claros e sabemos que o uso de uma variável de controle como o topo é ideal. Mas como ficaria esse código? Vamos ver:

	String item = pilha[topo]
	topo--
	return item

Pois é, só isso!!! Assim como a inserção, a remoção é muito simples. Logicamente que isso deve ser inserido em uma função, mas isso veremos mais a frente. 


**Verificações, porque não?**

>  You have a error of type 'StackOverflow' on line 4 - Pilha.java

Sim, ninguém quer ver um erro similar no seu mega projeto que demorou 10 dias para ser implementado, horas antes de vencer o prazo de envio ao professor da disciplina. Certamente o papo de "O cachorro comeu minha atividade" não vai colar. Então, precisamos fazer verificações no nosso projeto, para eliminar de uma vez por todas esses erros. 

Um pilha pode ser implementada com vetor ou com lista, neste caso estamos aprendendo como implementá-la em vetor e isso trás algumas limitações como por exemplo um tamanho máximo fixo de elementos que ele aceita. Como foi dito na Seção 2, existem dois motivos para verificarmos uma pilha baseada em vetor: *inserir em uma pilha cheia e remover em uma pilha vazia*.

A condição para um pilha está vazia é simples e já vimos aqui, é justamente o estado inicial dela, onde o topo é -1. 

	if(topo == -1)
		pilhavazia = true

Já a condição para ela está cheia ainda não vimos e vou dizer agora: basta que o topo seja igual ao tamanho do vetor - 1. Isso porque inserimos no vetor na posição "topo" e se topo é igual a o tamanho do vetor ou maior, não poderíamos inserir, pois é uma posição inválida.

	topo = 3
	["Prato A", "Prato B", "Prato C", "Prato D"]

Podemo inserir no topo? Vejamos:

- O topo será incrementado, ou seja virará 4
- Inserimos no vetor na posição 4 //Erro 

Isso certamente ocorrerá em erro, pois em um vetor de 4 posições (tamanho igual a 4), temos a primeira posição válida, a posição 0 e a última a 3. Ou seja, achamos um limite que é justamente quando o topo é igual à 3 (tamanho - 1).

	if(topo == tamanho_pilha - 1)
		pilhacheia = treu


**Observações**

Alguns exemplos aqui são didáticos, no sentido de que você entenda o problema. O código a seguir pode apresentar algumas diferenças, mas isso não impacta na solução do problema. Caso ainda ache que um algoritmo pode ser solucionado de apenas uma única forma, espero que reflita sobre isso. Esse é o momento! 


### 2.4 - Overview

Agora você está pronto para consultar o código da Pilha.java que implementamos.

```java
public class PilhaV<T> {

	/**
	* Array da Pilha 
	*/
	private T[] arrayPilha;
	/**
	* Atributo para armazenar o indice do topo da pilha
	*/
	private int topo;
	
	/**
	* Contrutor da Pilha
	* @param max Tamanho da pilha
	*/
	public PilhaV(int max){
		//instanciando um vetor genérico (cria um vetor do tipo Objetc e faz o cast (conversão) para o tipo T
		arrayPilha = (T[]) new Object[max];
		topo = -1;
	}
	
	/**
	* Insere um elemento se a pilha não estiver cheia
	* @param elemento Elemento a ser inserido na pilha
	* @return retora true se a operação foi bem sucedida
	*/
	public boolean inserir(T elemento) {		
		if(!this.estaCheia()) {
		topo++;
		arrayPilha[topo] = elemento;
		return true;
	}
	
	return false;
	}
	
	/**
	* Remove um elemento da pilha, se ela não esiver vazia
	* @return retorna o elemento se a operação foi bem sucedida
	*/
	public T remover() {		
	
	
	if(!this.estaVazia()) {			
		return arrayPilha[topo--];
	}
	
	return null;
	
	}
	
	/**
	* Verifica se a pilha está vazia
	* @return retorna true se a pilha estiver vazia
	*/
	public boolean estaVazia() {		
		return topo == -1;
	}
	
	/**
	* Verifica se a pilha está cheia
	* @return retorna true se a pilha estiver cheia
	*/
	public boolean estaCheia() {		
		return topo == arrayPilha.length-1;
	}
}
```

Retirado do repositório: https://github.com/LuisAraujo/Estrutura-de-Dados-em-Java

# 4 - Listas Simplesmente Encadeada

Parabéns, espero que até aqui vocês tenham compreendido o conceito de Pilha e Fila. Caso contrário eu lhe deixo uma máxima que sempre digo: 

> Não importa o quanto você veja, leia ou ouça, você só aprenderá de fato se tentar. O erro nesta fase é normal, mas você deve lidar com ele, verificá-lo, analisá-lo. Isso só ocorrerá se testar o seu código, só assim chegará ao topo, não só da pilha (rs), mas da montanha. Lugar em que habitam os *programadores(as)-ninjas*! 

Assim, Lista Simplesmente Encadeada é uma estrutura multifacetada, ela possui variações dos métodos de inserção e remoção, diferentemente da Fila e Pilha que só permitiam a entrada e saída de dados de um único local. Existem muitos tipos de Lista, mas agora falaremos apenas da Simplesmente Encadeada. Assim, sempre que mencionarmos o termo Lista, nesta Seção, estamos nos referindo à Lista Simplesmente Encadeada.

A Lista está mais próxima de um Vetor do que das estruturas que fizemos até aqui, por isso mesmo é que ela pode ser utilizada em substituição dos vetores, nas Pilhas e Filas, eliminando os problemas de limitação e de desperdício de espaço de memória. Assim, as Listas alocam memória quando necessário e despejam quando não precisam mais. 


**Saindo de Vetor e indo para lista**

Bem, já que listas podem substituir vetores, podemos então modificar os nossos códigos de Pilha e Fila para utilizarem Listas. Por isso, no início deste material estávamos nos referindo à Pilhas e Filas baseadas em vetores (pois não é o único modo de implementação). Mas antes disso, vamos entender como as Listas funcionam.

### 4.1 - A Lista

**O Nó**

Um nó segundo o [Dicionário Online de Português](https://www.dicio.com.br/no-2/) é: *Enlaçamento de fios, de linhas, de cordas, de cordões, fazendo com que suas extremidades passem uma pela outra, amarrando-as*.

Essa definição não é muito boa para o nosso caso, mas o própio dicionário diz, em outra definição: *Vínculo; ligação estreita entre pessoas por afeição ou parentesco*. Bem, agora sim, isso pode ser útil! 

Nós de uma Lista possuem vínculos, como vizinhos. Pense que uma lista é um conjuntos de Nós ligados por arestas e que essas arestas. Além de serem conectados por duas arestas, os Nós possuem propriedades (valores que podemos alocar neles). Fica claro aqui que o Nó é o elemento principal da nossa lista. 

Os Nós, então, se ligam a outros Nós, através das arestas. No Java arestas são objetos ou referências que aqui chamaremos de próximo, afinal um Nó A está ligado ao próximo Nó, o B. 

Pensando assim, em uma possível classe chamada Nó, teríamos duas propriedades, ou atributos, importantes: **o valor que ele armazena** (que pode ser de qualquer tipo, desde um inteiro até um objeto de uma Classe criada por nós) e a** referência para o próximo nó**. 

Em Linguagem C, essa referência é feita com ponteiros, mas aqui em Java os objetos são como ponteiros, eles apontam para um local na memória no qual aquele valor está armazenado. Experimente criar dois objetos e imprimi-los com *System.out.print*.

Então, se os objetos são ponteiros (ou referências), só precisamos colocá-los neste atributo (próximo) e tudo está conectado. Já que um Nó se liga à outro Nó, só precisamos da referência desse outro Nó. Vamos ver como isso ficaria:

    ```java
    public class No<T> {
    	private T valor;
    	private No proximo;	
    } 
	``` 

Voltaremos para o Nó depois, mas, por hora, assuma que esta é a "cara" dele. Antes disso, que tal criarmos o construtor? Bem, o ideal é passar esse valor por parâmetro e deixar o próximo Nó como nulo, pois ao ser criado o nó ainda não estará na lista, não estará ligado, portanto.  

	```java
    public class No<T> {
    	private T valor;
    	private No proximo;	

		public No(T valor) {
			this.valor = valor;
			proximo = null;
		}
    } 
	``` 

**A lista, uma cadeia de Nós**

Okay, agora temos um nó, se juntarmos os nós, eles formarão uma lista. Por exemplo:


	```java
	No a = new No(4);
	No b = new No(5);
	//esse método coloca o parâmetro b - do tipo Nó - em próximo, do objeto a
	a.setProximo(b);
	``` 
Mas como queremos criar um projeto em POO, o ideal seria ter uma classe que armazenasse os nós e que tivesse os métodos tal como inserir, remover e buscar o Nó, não é? 

Então, vamos pensar: "Se um conjunto de Nó é uma Lista, podemos chamar essa classe, que guardará os Nó, de Lista". Isso é semanticamente bom! Mas o que teria nesta Lista? 

1. - Todos os nós criados? 
1. - Teríamos várias variáveis para os nós? 
1. - Um vetor de nós? 

Opa! Mas tudo isso não iria limitar o número de nós? A resposta é: Sim! 

Vamos lá, se um Nó é ligado sempre ao próximo nó, não há, na lista, um Nó "solto no ar", ou seja, que não esteja ligado a outro nó (com exceção da primeira inserção de um nó em uma lista vazia). 

> Então, isso quer dizer que, se eu tenho a referência do primeiro nó eu posso chegar a todos os nós da lista? Sim, isso mesmo e é justamente por isso que não precisamos de um vetor de nós, precisamos apenas do primeiro. 

Mas por qual motivo não guardo o segundo, terceiro ou o último Nó? Bem, o primeiro é o único nó na lista que tem acesso a todos, pois ele tem como próximo o segundo e assim por diante. O segundo nó não tem acesso ao primeiro, só ao próximo, o terceiro, e assim por diante. O mesmo ocorre para o último, afinal ele nem próximo possui (continua como nulo), senão ele não seria o último.
  	
	```java
	public class Lista<T> {
		private No<T> primeiro;
	}
	```

### 4.2 -Inserindo na Lista

Como já foi dito, uma lista está mais para um vetor do que para uma Pilha ou Fila.  Pense bem: Em um vetor nós podemos inserir na posição 0, na posição lenght-1 ou em qualquer outra posição, certo? A lista tem o mesmo comportamento, nela é possível inserir na posição 0, aqui chamamos isso de inserir no início da lista. Podemos inserir no final (idem à length-1), ou em qualquer outras posição qualquer. Vamos ver essas possibilidades, nesta Seção.

Existem muitos tipos de lista, *e.g.,* simplesmente encadeada, circular, duplamente encadeada entre outras variações. O que temos que ter em mente é: estamos querendo eliminar duas coisas: desperdício de espaço e redimencionamento, problemas do vetor. 

Temos que lembrar também que se uma lista está mais para uma nova forma de armazenar cadeias de elementos, podemos, com ela, criar uma Pilha e uma Fila (como fizemos com o vetor). Sim, basta apenas utilizar os métodos de inserir e remover de modo que as regas sejam respeitada: FIFO e LIFO. 

Inicialmente vamos ver operações de uma lista simples ou simplesmente encadeada. 
 
#### 4.2.1 - Inserindo no início

Inserir no início é simples, basta apenas:

- Cria um novo nó
- Dizer que o seu próximo é o que esta agora como primeiro
- Dizer que ele agora é o novo primeiro

Mas como seria isso? Vejamos em Java:

	´´´java
    public void inserirNoInicio(T  valor) {
    		No<T> novo_no = new No<T>(valor);
			novo_no.proximo = primeiro;
			primeiro = novo_no
	}

	´´´
 
#### 4.2.1 - Inserindo no final

Inserir no final é simples também, basta apenas:

- Cria um novo nó
- Andar até o último nó
- Dizer que o próximo desse último nó é o novo nó

Em Java seria:

	´´´java
    public void inserirNoFinal(T  valor) {
    		No<T> novo_no = new No<T>(valor);
			No auxiliar = primeiro;
			while(auxiliar.proximo != null) {
				auxiliar = auxiliar.proximo;
			}
			auxiliar.proximo = novo_no.proximo
	}



#### 4.2.1 - Inserindo de forma ordenada

Inserir de forma ordenada é a forma mais complexa, mais ainda assim não é nenhum *Dragão Branco de Olhos Azuis*. Temos que verificar alguns pontos:

1. Se vamos inserir no início (caso o meu valor inserido seja menor que o valor do primeiro nó)
2. Se vamos inserir no final (caso o meu valor inserido seja maior que todos os nós na lista)
3. Se vamos inserir no meio (caso o meu valor seja um valor entre dois nós da lista)

- Cria um novo nó
- Andar até encontrar um nó maior que ele
- Dizer que o próximo do nó é este nó de valor maior
- (Atenção) Dizer que o próximo nó do nó anterior a este de valor maior é o novo nó (*Ok, leia novamente para entender!*)

	´´´java
	public void inserirNoMeio(T  valor) {
		No<T> novo_no = new No<T>(valor);
	
		No<T> auxiliar = primeiro;
		 
		while((auxiliar != null) && ( auxiliar.obterValor().compareTo(novo_no.obterValor() )) == -1  )
		{
 
			auxiliar = auxiliar.obterProximo();
		}
	 
		auxiliar.proximo(novo_no);	 
	
	}
	´´´

Mas calma! E se a lista estiver vazia? O while não executará e ocorrerá um erro em "auxiliar.proximo", pois ele é nulo. Vamos Ajustar? Que tal criar uma verificação para isso?

	´´´java
	public void inserirNoMeio(T  valor) {
		No<T> novo_no = new No<T>(valor);
	
		No<T> auxiliar = primeiro;
		 
		
		while((auxiliar != null) && ( auxiliar.obterValor().compareTo(novo_no.obterValor() )) == -1  )
		{
 
			auxiliar = auxiliar.obterProximo();
		}

	 	if(this.primeiro == null) { 
			this.primeiro = novo_no;
		else
			auxiliar.proximo(novo_no);
			
	}
	´´´

Ok, revolvemos isso. Agora pense que o nó a ser inserido é maior que todos os nós, teríamos que inserir no final. Neste caso, ocorreria em erro, pelo mesmo motivo anterior. Então, que tal ter outro auxiliar (auxiliar2), que vem um nó antes do auxiliar? Assim poderíamos dizer que o próximo do auxiliar2 seria o nosso novo nó e isso não traria nenhum erro.

	´´´java
 		public void inserirNoMeio(T  valor) {
		No<T> novo_no = new No<T>(valor);
	
		No<T> auxiliar = primeiro;
		No<T> auxiliar2 = null;
		
		while((auxiliar != null) && ( auxiliar.obterValor().compareTo(novo_no.obterValor() )) == -1  )
		{
 			auxiliar2 = auxiliar;
			auxiliar = auxiliar.proximo();
		}

	 	if(this.primeiro == null) { 
			this.primeiro = novo_no;
		else{
			novo_no.proximo = null;
			auxiliar2.proximo = novo_no;
		}
			 
	}
	´´´


Ótimo, como novo_no é o último, o próximo dele pode ser null. Agora vamos imaginar que a lista possui nós e o meu nó é menor que o primeiro nó. Por exemplo, em  uma lista: 2,3,5 e 6 (em ordem) eu desejo inseri o 1. O nosso loop iria parar na primeira comparação, pois "auxiliar.obterValor().compareTo(novo_no.obterValor() )" retornaria 1. Isso nos levaria a entrar no *else* e aí encontramos mais um problema, pois novo_no.proximo não poderia ser null. Ele deveria ser, na verdade primeiro. 
	´´´java
	public void inserirNoMeio(T  valor) {
		No<T> novo_no = new No<T>(valor);
	
		No<T> auxiliar = primeiro;
		No<T> auxiliar2 = null;
		
		while((auxiliar != null) && ( auxiliar.obterValor().compareTo(novo_no.obterValor() )) == -1  )
		{
 			auxiliar2 = auxiliar;
			auxiliar = auxiliar.proximo();
		}

	 	if(this.primeiro == null) { 
			this.primeiro = novo_no;
		else{
			novo_no.proximo = this.primeiro
			auxiliar2.proximo = novo_no;
		}
	}
	´´´


Okay, já estamos finalizando, tenha um  pouco mais de calma!!! Agora pense na última ocasião, onde a minha lista possui nós e eu quero inserir no meio de dois nós. Por exemplo, inserir o 4 (entre o 3 e o 5). Neste caso, auxiliar estaria em 5 e auxiliar2 em 3. Logicamente que o próximo do auxiliar2 será novo_no e o próximo de novo_no será 5.

Isso não seria possível com "novo_no.proximo = this.primeiro". Mas pensando bem, no caso de ele ser inserido no início, o auxiliar seria primeiro ainda (pois dizemos inicialmente que auxiliar = primeiro. Então posso trocar   "novo_no.proximo = this.primeiro" para  "novo_no.proximo = auxiliar" e isso funcionaria nos dois caso: inserir antes de todos e no meio de dois nós. 

O problema é que, caso o auxiliar seja o primeiro nó, auxiliar2 será null e isso ocasionaria um erro. Além disso, se queremos inserir no início, o "ponteiro" do primeiro deverá ser atualizado. Então vamos adicionar esse trecho:
	
	´´´java
	[...]
	else if(auxiliar == this.primeiro) {		
			novo_no.inserirProximo(this.primeiro);
			this.primeiro = novo_no;
	}
	[...]
	´´´
 

Vamos lá, veja como ficou:
	
	´´´java
	public void inserirNoMeio(T  valor) {
		No<T> novo_no = new No<T>(valor);
	
		No<T> auxiliar = primeiro;
		No<T> auxiliar2 = null;
		
		while((auxiliar != null) && ( auxiliar.obterValor().compareTo(novo_no.obterValor() )) == -1  )
		{
 			auxiliar2 = auxiliar;
			auxiliar = auxiliar.proximo();
		}

	 	if(this.primeiro == null) { 
			this.primeiro = novo_no;
		}else if(auxiliar == this.primeiro) {	
			novo_no.proximo = this.primeiro;
			this.primeiro = novo_no;
		}else{
			novo_no.proximo = auxiliar; 
			auxiliar2.proximo = novo_no;
		}	 
	}
	´´´

Pronto!

### 4.3 -Buscando na Lista

Podemos buscar um nó na lista pelo seu valor ou pelo seu índice. Vamos ver buscar antes de remover, pois ele irá nos ajudar a remover um Nó. 

#### 4.3.1 - Buscando um nó pelo seu valor

Para buscar é simples, devemos apenas executar o loop com um auxiliar percorrendo a lista até que o valor seja encontrado ou até chegar ao final da lista:
	
	´´´java
	public No<T> buscar(T valor) {
		 
		No<T> auxiliar = primeiro;
		 
		while((auxiliar != null) && (auxiliar.obterValor().compareTo( valor )) != 0  )
		{
			auxiliar = auxiliar.proximo;
		}
		
		return auxiliar;
	}
	´´´

#### 4.3.1 - Buscando um nó pelo índice

Podemos modificar um pouco esse método e buscar com índice
	
	´´´java
	public No<T> buscarPorIndice(int indice) {
		 
		No<T> auxiliar = primeiro;
		int contador = 0; 
		while((auxiliar != null) && (contador < indice))
		{
			auxiliar = auxiliar.proximo;
			contator++;
		}	
		return auxiliar;
	}
	´´´

Sim, é muito simples! 


#### 4.3.1 - Outras formas de Busca

Assim com a Pilha e Fila, podemos implementar métodos de busca que acessem o primeiro item:
	
	´´´java
	return this.primeiro
	´´´

ou o final:
	´´´java
	auxiliar = this.primeiro
	while((auxiliar.proximo != null))
	{
		auxiliar = auxiliar.proximo;
	}

	return auxilia;
	´´´

### 4.4 -Removendo da Lista

Remover um nó é similar à inserção e à busca, podemos remover no início, no final ou remover um nó específico baseado em valor ou índice dele. 

#### 4.4.1 - Removendo um nó no início

Bem, se estamos removendo do início é sinal que o segundo nó será o nosso novo início. O segundo nó é o próximo do primeiro, certo? Então que tal fazermos isso:
	
	´´´java
	public No<T> removerInicio() {
		 
		No<T> auxiliar = primeiro;
		primeiro = primeiro.próximo;
		auxiliar.proximo = null;
		return auxiliar;
	}
	´´´

#### 4.4.2 - Removendo um nó no final

Remover no final significa que o penúltimo nó será o novo último. Para ser considerado um último nó, na lista, este nó deve ter o seu próximo igual à null (não possui próximo). Então, vamos até o penúltimo nó e dizer que o próximo dele é *null*. Mas como fazemos isso? Assim:
	
	´´´java
	public No<T> removerFinal() {
		 
		No<T> auxiliar = primeiro;
		No<T> auxiliar2 = null;

		while((auxiliar.proximo != null))
		{
			auxiliar2 = auxiliar;
			auxiliar = auxiliar.proximo;
		}

		auxiliar2.proximo = null;

		return auxiliar;
	}
	´´´

#### 4.4.3 - Removendo um nó pelo seu valor

Já sabemos buscar pelo valor do Nó! Temos apenas que considerar algumas coisas referentes ao modo de deleção (início, meio ou final), assim como na inserção.

	´´´java
	public void removerPorValor(T valor) {
		No<T> novo_no = new No<T>(valor);
	
		No<T> auxiliar = primeiro;
		No<T> auxiliar2 = null;
		
		while((auxiliar != null) && (auxiliar.obterValor().compareTo( valor )) != 0  )
		{
			auxiliar2 = auxiliar;
			auxiliar = auxiliar.proximo;
		}

	
		if(auxiliar == null){
			System.out.println("Valor não existe na lista");
		}else if(auxiliar == this.primeiro) {	
			this.primeiro = auxiliar.próximo;
			return primeiro;
		}else{
			auxiliar2.proximo = auxiliar.próximo;
		}
	}
	´´´

#### 4.4.4 - Removendo um nó pelo índice

O código para remover pelo índice é similar à remoção como valor, adicionando o contato, como na busca por índice.

	´´´java
	public void removerPorIndice(int indice) {
		No<T> novo_no = new No<T>(valor);
	
		No<T> auxiliar = primeiro;
		No<T> auxiliar2 = null;
		
		int contador = 0; 
		while((auxiliar != null) && (contador < indice))
		{
			auxiliar = auxiliar.proximo;
			contator++;
		}

	
		if(auxiliar == null){
			System.out.println("Valor não existe na lista");
		}else if(auxiliar == this.primeiro) {	
			this.primeiro = auxiliar.próximo;
			return primeiro;
		}else{
			auxiliar2.proximo = auxiliar.próximo;
		}
	}
	´´´

#### 4.4.5 - Removendo um nó pelo índice

Pensando bem, criamos os métodos de busca por valor e por índice, não seria legal usar esses métodos para retornar o Nó e depois fazer a remoção? Isso fica como desafio.

Formalizando:

**1 - Implemente o métodos de removerPorValor e removerPorIndice usando o método de buscarPorValor e buscarPorIndice.**


**Overview**

```java
public class No<T extends Comparable<T>> {
	
	private T valor;
	private No proximo;
	
	public No(T valor) {
		this.valor = valor;
		proximo = null;
	}
	
	/**obtém o próximo nó */
	public No<T> obterProximo() {
		return this.proximo;
	}
	/**inserir o próximo nó */
	public void inserirProximo(No proximo) {
		this.proximo = proximo;
	}
	/**inserir o valor no nó */
	public void inserirValor(T valor) {
		this.valor= valor;
	}
	/**obter o valor do nó */
	public T obterValor() {
		return this.valor;
	}
	
	//métod toString para exibir o nó
	public String toString() {
		return this.valor.toString();
	}
	
}



public class Lista<T extends Comparable<T>> {
	
	public void inserir(T  valor) {
		No<T> novo_no = new No<T>(valor);
		
		No<T> auxiliar = primeiro;
		No<T> auxiliar2 = null;
		
		while((auxiliar != null) && ( auxiliar.obterValor().compareTo( novo_no.obterValor() )) == -1  )
		{
			auxiliar2 = auxiliar;
			auxiliar = auxiliar.obterProximo();
		}
		
		if(this.primeiro == null) { 
			this.primeiro = novo_no;
		
		}else if(auxiliar == this.primeiro) {
			
			novo_no.inserirProximo(this.primeiro);
			this.primeiro = novo_no;
			
		}else {
			novo_no.inserirProximo(auxiliar);
			auxiliar2.inserirProximo(novo_no);	
		}
	
	}

	public No<T> remover(T valor) {
		
		No<T> auxiliar = primeiro;
		No<T> auxiliar2 = null;

		while((auxiliar != null) && (auxiliar.obterValor().compareTo( valor )) != 0  )
		{
		
			auxiliar2 = auxiliar;
			auxiliar = auxiliar.obterProximo();
		}
		
		
		if(auxiliar == this.primeiro) {
			
			No retorno = this.primeiro;
			this.primeiro = this.primeiro.obterProximo();
			return retorno;
		
		}else if(auxiliar != null)
			auxiliar2.inserirProximo(auxiliar.obterProximo());
		
		return auxiliar;
		
	}

	public No<T> buscar(T valor) {
		 
		No<T> auxiliar = primeiro;
		 
		while((auxiliar != null) && (auxiliar.obterValor().compareTo( valor )) != 0  )
		{
			 
			auxiliar = auxiliar.obterProximo();
		}
		
	
		 
		return auxiliar;
	}
	 
	public String toString() {
		String s = "";
		No<T> auxiliar = primeiro;
		
		while(auxiliar != null)
		{
			//incrementa o valor
			s+= auxiliar.obterValor().toString() + " - ";
			//pula para o próximo
			auxiliar = auxiliar.obterProximo();
		}
		
		return s;
	} 
	
}
```

Retirado do repositório: https://github.com/LuisAraujo/Estrutura-de-Dados-em-Java

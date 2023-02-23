# 3 - Fila

Bem, chegamos a nossa segunda estrutura de dados: a Fila. Quando falamos em fila, já pensamos em filas de banco, atendimento e etc. Você irá se espantar se eu lhe disser que é justamente isso. Lembra que falamos sobre "Modelagem Computacional"? Pois é, aqui vamos modelar uma Fila. Intuitivamente a Fila tem a seguinte característica:

> Um elemento entra sempre no final. Ao remover um elemento só podemos remover o elemento no início.

Isso quer dizer que não podemos remover um elemento se ele não for o elemento que está no início (o próximo a ser atendido). Já pensou se você está em uma Fila, esperando cerca de 30 minutos, é o próximo a ser atendido, e alguém passa na sua frente, sem nenhuma justificativa? É realmente indignante! 

Como fizemos com a Pilha, faremos um algoritmo informal para atender pessoas em Fila. Imagine esse cenário: Uma pessoa D chega ao Banco e verifica que a fila para o atendimento que deseja já possui a pessoa A, B e C.

 
* A pessoa D entra no final da fila
* A pessoa A é atendida!
	* *A pessoa B é a próxima a ser atendida*.
* A pessoa B é atendida!
	* *A pessoa C é a próxima a ser atendida*.
* A pessoa C é atendida!
	* *A pessoa D é a próxima a ser atendida*.
* A pessoa D é atendida!

Bem, há uma repetição aqui, então vamos ajustar usando loop:

* A pessoa D entra no final da fila
* Atá que a pessoa C seja atendida!
	* *Atender Próxima pessoa*
* A pessoa D é atendida!

> Ok, garantimos que a pessoa 'D' será atendida conforme sua posição, assim uma pessoa 'E' não será atendida antes dela.

Assim como fizemos com Pilha, vamos também implementar algo mais formal usando a linguagem de programação Java para isso. Como queremos usar POO, vamos criar algumas classes para serem a "forma" dos nossos objetos. Vamos criar o elemento, um Item que será colocado na Fila e a própria fila, para isto usaremos um simples vetor.

Então:

* Uma classe item (sim, podemos usar a mesma da pilha, copie para o seu novo projeto).
* Um vetor.

Além dos locais de armazenamento, precisamos garanti as operações da Fila. A Fila - diferentemente da Pilha - é uma estrutura onde o último elemento a entrar será também o último a sair, isso quer dizer que o primeiro a entrar será o primeiro a sair, por isso ela é conhecida como FIFO (*First Input First Output*).

Então, além dos dados temos:

* Operação de inserir
* Operação de remover


### 3.1 - Inserindo dados na Fila

Mas como controlar que vou inserir no início? Ok, se você pensou "vou usar o mesmo que fiz na pilha", você está no caminho certo. Vamos pensar que temos um vetor de 10 elementos e no inicio todos são nulos.

	[null, null, null, null, null, null, null, null, null, null]

Eu posso inserir na posição com menor índice que possui o valor null, ela será o nosso final.

	["Pessoa A", null, null, null, null, null, null, null, null, null]

Se desejo inserir novamente, eu coloco na próxima posição com menor índice que esteja vazia (null).

	["Pessoa A", "Pessoa B", null, null, null, null, null, null, null, null]

Você certamente já percebeu que eu precisaria verificar, posição por posição até chegar a uma vazia:

	int pos_vazia = 0;
	while( (i< tamanho_fila) && (fila[i] != null) )
		pos_vazia++;
	
	if(pos_vazia < tamanho_fila)
		fila[i] = "Prato C";

**Nossa!!!** Mas isso é muito custoso! Pense em uma Fila de 1 milhão de lugares. Quando tivermos que inserir o primeiro elemento, faremos 999.999 comparações apenas para inserir um único elemento. 


**Usando o fim** (um primo distante do topo)

Uma solução para esse problema é criar uma variável que armazenará o valor (índice) do fim, assim como o topo. Com isso, poderemos sempre inserir em uma posição vazia. No primeiro caso que apresentamos, o fim inicial poderia ter o valor 0.

	fim = 0
	[null, null, null, null, null, null, null, null, null, null]

Seguiremos:
	
	//Inserir Pessoa A
	fim = 1
	["Pessoa A", null, null, null, null, null, null, null, null, null]
	//Inserir Pessoa B
	fim = 2
	["Pessoa A", "Pessoa B", null, null, null, null, null, null, null, null]

Mas como ficaria esse algoritmo?

	//Inserir Pessoa C
	fila[fim] = "Prato C";
	fim++


Só isso? Sim!!! Como na Pilha, além de ter menos linhas, temos menos acesso aos dados. Agora, quando a Fila estiver com 50% de dados, teremos a mesma quantidade de operações que ela como 100% dos dados. **Que legal!!!**


### 3.2 - Removendo Dados na Fila

Para remover um dado na fila, precisaríamos apenas remover o elemento no início, que naquele caso inicial é o 0. Isso é muito simples, mas há o fator complicador que é a realocação de todos os elementos em suas novas posições.

Vetor inicial:
	
	["Pessoa A", "Pessoa B", "Pessoa C", "Pessoa D", null, null, null, null, null, null]

Removendo o primeiro elemento:

	[null, "Pessoa B", "Pessoa C", "Pessoa D", null, null, null, null, null, null]

Realocando os elementos:

	["Pessoa B", "Pessoa C", "Pessoa D", null, null, null, null, null, null, null]


Um algoritmo informal para a realocação seria:

* Remover a posição 0 do vetor;
* A posição 1 é diferente de null?
	* Mova o elemento 1 para 0
* A posição 2 é é diferente de null?
	* Mova o elemento 2 para 1
* A posição 3 é é diferente de null?
	* Mova o elemento 3 para 2

Usando loops:

* i = 0
* Remover a posição i do vetor;
* Enquanto a posição i + 1 for diferente de null
	* Mova o elemento i + 1 para i


Já percebemos que essa solução não é ideal! Poderíamos então usar outra variável  chamada início pra controlar a remoção:

	String item = fila[inicio]
	inicio++
	return item

**Verificações, porque não?**

>  OMG!!! You have YET a error of type 'StackOverflow' on line 4 - Fila.java

Já falei sobre a estória do "O cachorro comeu minha atividade" não é? Então vamos evitar isso fazendo as verificações necessárias no nosso projeto.

Assim como uma pilha, a fila pode ser implementada com vetor ou com lista, estamos implementando com vetor, neste momento.  Chegará o momento de usarmos lista, mais a frente. Bem, usar vetor torna o processo mais básico e agrega algumas limitações como por exemplo um tamanho máximo fixo de elementos que ele aceita. Assim, existem dois motivos para verificarmos uma fila baseada em vetor: inserir em uma fila cheia e remover em uma fila vazia.

As condições para verificar a fila é um pouco mais complexa, mas nada que não possamos aprender. Bem, uma fila não pode está vazia quando o final é 0, isso porque o final e o início caminham ao longo dela. Então, mesmo o final sendo 0, pode ser que o início seja 10, em uma fila com 15 posições. Logo, temos elementos na posição 10, 11, 12, 13 e 14. *Isso impede o desperdício de locais no vetor*. Mas vamos focar nas condições, por hora aceite que a fila vazia pode ser identificada quando o início for igual ao fim.

	if(inicio == fim)
		filavazia = true 


A condição para ela está cheia é também diferente da Pilha. Uma Fila está cheia quando  a subtração do fim pelo início for igual  à 1 (fim - início == 1) ou (fim = início - 1). Como dito antes, o índice do final e do início caminham ao longo da fila. Logo quando o fim for igual ao tamanho da fila e início for 0, ela também está cheia


	if(fim == tamanho_fila) && (inicio == 0) ) || (fim == inicio-1)
			filacheaia = true 



**Explorando mais sobre o início e o fim**


Como dizia Raul Seixas: "eu sou o início, o fim e o meio". Logicamente que ele não estava falando de uma fila, mas poderia. O fim e o início em uma fila não funcionam como o topo de uma Pilha. O topo em uma pilha varia de -1 até o tamanho da pilha. Na Fila isso não seria muito bom. Vamos pensar em uma fila com capacidade para 8 elementos e inicialmente com 4 elementos:

	    inicio                                      fim 
	      |                                          |
	      v                                          v
		    
	["Pessoa A", Pessoa B", "Pessoa C", "Pessoa D", null, null, null, null]


Ao remover os elementos teríamos:

 			     inicio   fim 
				|       |
				v       v
		    
	[null, null, null, "Pessoa D", null, null, null, null]

Adicionando mais 4 elementos teríamos

			   inicio    					              fim 
			     |                                                         |
			     v                                                         v
		    
	[null, null, null, "Pessoa D", "Pessoa E", "Pessoa F", "Pessoa G", "Pessoa H"]


Ok, até ai nada de novo. Mas o que aconteceria se eu removesse 4 elementos?


				                    inicio    fim 
			                              |        |
				                      v        v
		    
	[null, null, null, null, null, null, null, "Pessoa H"]


Sim, temos 7 posições vazias (*nulls*) e não podemos inserir, pois o fim já chegou ao seu limite. Inserir na posição do fim, nessa situação, nos levaria para um erro por acesso à local não permitido. #stackoverflow 

Por esse motivo que, quando vamos inserir e verificamos que o fim chegou no seu limite, ele é transportado para o índice 0, para que possamos inserir mais elementos: 

	if(fim ==tamanho_fila)
			fim = 0;

O mesmo faremos para o inicio, dada as remoções:

	if(inicio == fila.length)
             		inicio = 0;

Como exercício desenhe uma fila de 10 posições, insira elementos e remova-os. Deixando a fila cheia no primeiro momento e depois vazia. Faça isso ao menos 3 vezes na mesma pilha e verá como essa transição funciona.  

**Observações**

Como na Seção anterior, alguns exemplos aqui são didáticos, no sentido de que você entenda o problema. O código a seguir pode apresentar algumas diferenças, mas isso não impacta na solução do problema. Como já dito anteriormente, não há uma solução fechada para um algoritmo. 

**Overview**

Agora você está pronto para consultar o código da Fila.java que implementamos.
	
```java 
public class FilaV<T>{
	private T[] arrayFila;
	private int inicio;
	private int fim;
	
	public FilaV(int size){
		inicio = fim = 0;
		arrayFila = (T[]) new Object[size];
	}
	
	public boolean estaCheia(){
		return ((fim == arrayFila.length-1) && (inicio == 0) )
				|| (fim == inicio-1);
	}
	
	public boolean estaVazia(){
		return inicio == fim;
	}
	
	public T remover(){
		if(!estaVazia()){

			if(inicio == fila.length)
             			inicio = 0;
	     
			T e = arrayFila[inicio];
			inicio++;
			return e;
		}
		
		return null;
	}
	
	public boolean inserir(T e){
		if(fim == arrayFila.length)
			fim = 0;
		
		if(!estaCheia()){
			arrayFila [fim++] = e;
			System.out.println("inserindo - " + fim);
			return true;
		}
		
		return false;
	}
	
	@Override
    public String toString(){
		
        String s = "[";
        int i = inicio; 
        while(i != fim){
        	System.out.println(s);
            if(i == arrayFila.length)
                i = 0;
            
            if(i == fim-1) 
                s+=arrayFila[i];
            else 
                s+=arrayFila[i] + " , ";
        
            i++;
    		
        }
        
        return s + "]";  
    }
}
```

Retirado do repositório: https://github.com/LuisAraujo/Estrutura-de-Dados-em-Java

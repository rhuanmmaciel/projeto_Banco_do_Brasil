## 6 - Lista Circular

A Listas Duplamente Encadeada supera o problema de voltar ao início, reduzindo o número de interações para achar nós próximos. Lembra do caso de busca o nó de valor 30 e depois o 29? Estendendo esse problema, imagine que queremos buscar o nó de valor 999, inicialmente faremos 999 interações. Agora queremos busca o nó de valor 10, teríamos que fazer 989 interações para voltar. Não seria interessante seguir até o final e ter um "portal" que nos leve ao início? Assim faríamos 11 interações apenas (1000, 1, 2, 3 ... 10). 

Tenho uma coisa importante para dizer: A Lista Circular possui esse portal. A sua estrutura é similar à Duplamente Encadeada, por isso não repetiremos o código aqui. Ela possui o mesmo tipo de nó e apenas algumas modificações nas operações. 


> O princípio básico aqui é que o primeiro nó é ligado ao último e o último é ligado ao primeiro. Assim, poderíamos andar até o final e chegar o início novamente.


#### 6.1 - Inserindo na Lista Circular

Vamos ver os métodos de inserção, neta seção.

#### 6.1.1 - Inserindo no início e final

A lista circular não possui início ou fim, nenhum nó tem links com valor nulo.  Temos o atributo primeiro apenas para nos ajudar nas operações, afinal precisamos sair de algum lugar. Até o primeiro nó possui um link para ele mesmo. Assim, toda inserção na lista é igual, mas antes disso vamos aos caso específicos.

#### 6.1.2 - Inserindo em uma lista vazia

veja o trecho do código a seguir, isso gera um nó com link para ele mesmo. Que louco em?

```java
this.primeiro =novo_no;
noAtual = this.primeiro;
this.primeiro.inserirProximo(novo_no);
this.primeiro.inserirAnterior(novo_no);
```

#### 6.1.3 - Inserindo em uma lista com apenas um nó
```java
No<T> temp = this.primeiro;
if(temp.obterProximo() == temp) {
	temp.inserirProximo(novo_no);
	temp.inserirAnterior(novo_no);
	novo_no.inserirAnterior(temp);
	novo_no.inserirProximo(temp);
```

#### 6.1.4 - Inserindo de, forma ordenada, um nó menor que o nó inicial

```java
novo_no.inserirProximo(this.primeiro);
novo_no.inserirAnterior(this.primeiro.obterAnterior());
this.primeiro.obterAnterior().inserirProximo(novo_no);
this.primeiro.inserirAnterior(novo_no);

this.primeiro = novo_no;
noAtual = this.primeiro.obterAnterior();
```

#### 6.1.5 - Todas os outros casos

```java
while( (novo_no.obterValor().compareTo(temp.obterValor() ) == 1)) { 
 	temp = temp.obterProximo();

	//fechou um ciclo
	if(temp == this.primeiro)
		break;
}


novo_no.inserirProximo(temp);
temp.obterAnterior().inserirProximo(novo_no);
novo_no.inserirAnterior(temp.obterAnterior());
temp.inserirAnterior(novo_no);
```

#### 6.2 - Buscando na Lista Circular

Como os métodos de buscar são similares, vamos fazer outra abordagem aqui que serve para a circular. Vamos criar um atributo chamado último nó que guardará não o último nó da lista, mas o último nó buscado e vamos fazer a busca a partir dele. Similar como fizemos na busca duplamente. Mas aqui, temos a vantagem do portal que nos permitirá sair de uma extremidade até outra.

Nessa abordagem nós consideramos que dada uma busca de um valor maior que o nó atual (último buscado) e considerando que a busca esteja uma uma posição bem inicia da lista (por exemplo 10% da lista) ou, no caso oposto, uma busca de um elemento de valor menor e a busca esteja em uma posição final da lista (por exemplo 90%). 

Nessas duas situações pensamos se é melhor seguir para frente ou para trás. Imagine uma busca em uma lista de 100 elementos ordenados, o último elemento é 90 e a o primeiro 0. A última busca está no quinto elemento de valor 5. É obvio que é melhor eu retornar até chegar ao outro lado da lista, do que seguir até o final da mesma. O mesmo ocorre se a última busca tenha sido 90 e queremos encontrar o elemento de valor 5, é melhor seguir até o outro lado da lista. 

Caso não tenha entendido, pense um pouco olhando essa imagem com a comparação do primeiro caso:

#### 6.2.1 - Buscando Nós sem andar muito

Inicialmente vamos criar flags para saber se devemos andar para frente ou para trás:

```java

if( (prior) || (!next))
	this.obterNoAnterior();
else if( (next) || (!prior)) 
	this.obterNoProximo();

```

Quem decidirá a direção são dois fatores: o valor que eu busco em comparação com o nó atual e a posição que estamos na lista, nessa abordagem temos mais um atributo chamado *qtdNo* que guarda a quantidade de nós que teremos na lista. Logicamente que os métodos de inserção e remoção precisam ser atualizados para esse controle. 


```java
boolean prior = true;
boolean next = true;

//valor buscado é menor que o currenteNode?
if(valor.compareTo(noAtual.obterValor())  == -1 )  {
			
	//estou em 90% do final da lista
	if(indiceNoAtual < qtdNo*0.9) {
		prior = false;
	}

}else if(valor.compareTo( noAtual.obterValor())  == 1 )  {

	//estou em 10% do final da lista
	if(indiceNoAtual < qtdNo*0.1) {
		next = false;
	}

}else {
	return noAtual;
}

```

O código completo é a junção dos dois trechos apresentados, com a adição de alguns elementos que visam verificar a parada *stop* e caminhar na lista. 

#### 6.3 - Removendo na Lista Circular

Para remover, precisamos considerar o novo link entre o primeiro e o último nó. Vejamos os códigos.

#### 6.3.1 - Removendo por valor

Observe que estamos utilizando a versão como o contador do qtdNo, você pode fazer isso em outros métodos. 

```java

public void remover(T valor) {
	
	No n= buscarOtim(valor);
	
	if(n != null) {
		qtdNo--;
		if(n == this.primeiro) {
			
			this.primeiro.obterAnterior().inserirProximo(this.primeiro.obterProximo());
			this.primeiro.obterProximo().inserirAnterior(this.primeiro.obterAnterior());
			this.primeiro = this.primeiro.obterProximo();
			
		}else {
			
			n.obterAnterior().inserirProximo(n.obterProximo());
			n.obterProximo().inserirAnterior(n.obterAnterior());
			
		}
		
	}
	
}

```


#### 6.3.2 - Removendo por índice

Aqui podemos utilizar a mesma busca por índice que a lista duplamente.

```java

public void remover(T valor) {

No n= buscarPorIndice(valor);

if(n != null) {
	qtdNo--;
	if(n == this.primeiro) {
		
		this.primeiro.obterAnterior().inserirProximo(this.primeiro.obterProximo());
		this.primeiro.obterProximo().inserirAnterior(this.primeiro.obterAnterior());
		this.primeiro = this.primeiro.obterProximo();
		
	}else {
		
		n.obterAnterior().inserirProximo(n.obterProximo());
		n.obterProximo().inserirAnterior(n.obterAnterior());
		
	}	
}	
}

```
**Overview**


```java

public class No <T extends Comparable<T>>{

	No prior;
	No next;
	T data;	
	
	public No(T data) {
		this.data = data;
	}
	public No(T data, No prior, No next) {
		this.data = data;
		this.prior = prior;
		this.next = next;
	}
	
	public No<T> obterAnterior() {
		return prior;
	}
	public void inserirAnterior(No prior) {
		this.prior = prior;
	}
	public No<T> obterProximo() {
		return next;
	}
	public void inserirProximo(No next) {
		this.next = next;
	}
	public T obterValor() {
		return data;
	}
	public void inseriValor(T data) {
		this.data = data;
	}
	public String toString() {
		return this.data.toString();
	}
}


public class ListaCircular<T extends Comparable<T>> {

	public No<T> primeiro;
	public No<T> noAtual;
	public int qtdNo = 0;
	public int indiceNoAtual = 0;
	
	public ListaCircular() {
		this.primeiro = null;
	}
  	
	public void inserir(T valor) {
		qtdNo++;
		No<T> novo_no = new No<T>(  valor);
		
		if(this.primeiro== null) {
			this.primeiro =novo_no;
			noAtual = this.primeiro;
			this.primeiro.inserirProximo(novo_no);
			this.primeiro.inserirAnterior(novo_no);
		}else {
		    No<T> temp = this.primeiro;
		    //apenas 1 nó
		    if(temp.obterProximo() == temp) {
	    		temp.inserirProximo(novo_no);
	    		temp.inserirAnterior(novo_no);
	    		novo_no.inserirAnterior(temp);
	    		novo_no.inserirProximo(temp);
	    		 
	    	//o nó inserido é menor que o primeiro nó
		    }else if(novo_no.obterValor().compareTo(this.primeiro.obterValor() ) == -1) {
	    	        	
		    	novo_no.inserirProximo(this.primeiro);
		    	novo_no.inserirAnterior(this.primeiro.obterAnterior());
		    	this.primeiro.obterAnterior().inserirProximo(novo_no);
		    	this.primeiro.inserirAnterior(novo_no);
		    	
		    	this.primeiro = novo_no;
		    	noAtual = this.primeiro.obterAnterior();
		    	
		    	    	
		    }else{
		    	
	    		//enquanto o novo nó for maior que o temp (até encontrar alguém maior
		    	//que ele
			    while( (novo_no.obterValor().compareTo(temp.obterValor() ) == 1)) { 
			     	temp = temp.obterProximo();
			
			    	//fechou um ciclo
			    	if(temp == this.primeiro)
			    		break;
			    }
			
			  
	    		novo_no.inserirProximo(temp);
	    		temp.obterAnterior().inserirProximo(novo_no);
				novo_no.inserirAnterior(temp.obterAnterior());
				temp.inserirAnterior(novo_no);
				
	    	}			
		}
	}

	public void remover(T valor) {
		
		No n= buscarOtim(valor);
		
		if(n != null) {
			qtdNo--;
			if(n == this.primeiro) {
				
				this.primeiro.obterAnterior().inserirProximo(this.primeiro.obterProximo());
				this.primeiro.obterProximo().inserirAnterior(this.primeiro.obterAnterior());
				this.primeiro = this.primeiro.obterProximo();
				
			}else {
				
				n.obterAnterior().inserirProximo(n.obterProximo());
				n.obterProximo().inserirAnterior(n.obterAnterior());
				
			}
			
		}
		
		
	}
	
	
	public No<T> buscar(Comparable valor) {
		No temp = this.primeiro;
		
		while(valor.compareTo( temp.obterValor() ) == 1) { 
			temp = temp.obterProximo();
	
	    	//fechou um ciclo ou passou do valor
	    	if((temp == this.primeiro) || (valor.compareTo( temp.obterValor() ) == -1))
	    		return null;
	    }
		
		return temp;
		 
		
	}
	
	
	public No<T> buscarOtim(Comparable valor) {
		
		boolean prior = true;
		boolean next = true;
		
		//valor buscado é menor que o currenteNode?
		if(valor.compareTo(noAtual.obterValor())  == -1 )  {
						
			//estou em 90% do final da lista
			if(indiceNoAtual < qtdNo*0.9) {
				prior = false;
			}
			
		}else if(valor.compareTo( noAtual.obterValor())  == 1 )  {
			
			//estou em 10% do final da lista
			if(indiceNoAtual < qtdNo*0.1) {
				next = false;
			}
			
		}else {
			return noAtual;
		}
			
		No stop = noAtual;
		
		if( (prior) || (!next))
			this.obterNoAnterior();
		else if( (next) || (!prior)) 
			this.obterNoProximo();
		
		
		while(valor.compareTo(noAtual.obterValor() ) != 0) { 
			if( (prior) || (!next))
				this.obterNoAnterior();
			else if( (next) || (!prior)) 
				this.obterNoProximo();
		
			//fechou um ciclo
			if(noAtual == stop)
				return null;
		}

		
		return noAtual;
		 
		
	}
	
	
	public No<T> obterNoProximo() {
		indiceNoAtual++;
		noAtual = noAtual.obterProximo();
		return noAtual;
	}
	
	public No<T>  obterNoAnterior() {
		indiceNoAtual--;
		noAtual = noAtual.obterAnterior();
		return noAtual;
	}

	public void resetCurrentNode() {
		this.noAtual = this.primeiro.obterAnterior();
	}
	
	public String toString() {
		String s = "";
		resetCurrentNode();
		No stop = noAtual;
		
		do {
			obterNoProximo();
			s+= noAtual .obterValor().toString() + " - ";
		}while(noAtual !=  stop);
		
		return s;
	} 
	
	
	
}
```

Retirado do repositório: https://github.com/LuisAraujo/Estrutura-de-Dados-em-Java

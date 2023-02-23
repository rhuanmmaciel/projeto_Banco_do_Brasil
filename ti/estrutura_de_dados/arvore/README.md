### 7 - Árvores

Árvores! Nessa **altura** você deve ter si perguntado: o que árvores tem haver com programação? **Folhas**? **Raiz**? **Ganhos**? Sim, tudo isso tem relação. A ideia da estrutura da dados Árvore é similar a estrutura de uma árvore, presente na natureza. Embora a representação seja de cabeça para baixo (e embora árvores não tenha cabeça), elas possuem uma raiz (primeiro nó), folhas (nós sem filhos), altura e muito mais.

Cada nó em uma árvore possui nós vinculados a eles que chamados de filho (São como os links próximo e anterior, mas aqui são substituídos por outas nomenclaturas)

### 7.1 - Árvore Binária de Busca (ABB)

Aqui temos os mesmos Nós que a lista, muito similar à da duplamente encadeada modificando apenas o atributo próximo para direito e o anterior para o esquerdo. Essas duas referências dos nós são, na verdade, filhos do nó que as contém. Por exemplo: Um nó B pode ter dois filhos: A e C, um à esquerda e outro à direta. Esse é o principal conceito de Árvore Binária: **cada nó possui no máximo dois nós**. Mas um Nó pode ter apenas 1 ou nenhum nó (não passando de dois).

#### Uma pausa para mais conceitos

Além dos nós e filhos, alguns outros conceitos são importantes quando falamos em Árvores. Por exemplo, uma árvores pode ter *altura* () e um nó pode está em um *nível* (). Um nó sem filhos é chamado de *nó folha*. Um *caminho ou percurso* é o conjunto de nós que nos fazem sair de um nó A e ir até um nó Z. O *nó raiz* é o nó cujo não possui antecedentes, ou seja, não tem pai. O nó raiz é o nó que fica no topo da árvore. 

Um elemento importante da árvore binária de busca é que, **ao inserir filhos, deve-se verificar se ele é maior ou menor que o pai. Se for menor, deverá ser um filho à esquerda e se for maior deverá ser um filho à direita**. Caso o nó já possua dois filhos, devemos andar pelos nós até encontrar um nó sem filhos, onde possamos alocá-lo.  

Árvore Binária é muito utilizada me buscas, pois reduz bastante a busca, em alguns casos. Um lista simplesmente encadeada, no pior caso realiza n operações para a busca, uma árvore, no pior caso realiza *log2 n* interações.

#### 7.1.1 - Nó

Como já mencionado, o Nó da árvore é similar ao nó da lista. Outro elemento importante que podemos adicionar o o atributo do nó pai. 

```java
public class No<T extends Comparable<T>> {

	No esquerdo;
	No direito;
	T valor;
	No pai;

	public No(T valor) {
		this.valor = valor;
	}
```	


#### 7.1.2 - Inserção

O princípio de inserção em uma ABB é que não há elementos repetidos. Assim, ao inserir um elemento, nós devemos buscar um local vazio cujo o seu pai seja menor que ele, se ele foi um filho à direita ou maior se ele for um filho à esquerda. Para isso, precisamos fazer a verificação do valor e andar para o próximo nó. 

Devemos considerar alguns aspectos, por exemplo se a árvores está vazia. Neste caso, o nó inserido será a raiz da árvore.


```java
public No inserirNo(No novo, No pai) {
		
		if(raiz == null) {
			raiz = novo;
```

Nós vamos criar um método anterior ao método inseritNo que só receberá um valor e criará o novo nó e passará a referência para o inserirNo. O usuário deverá usar apenas o inserir. Veja:

```java
public No inserirNo(T valor) {
		No<T> n = new No<T>(valor);
		return inserirNo(n, null);
		
	}
```

> Mas porque isso? Bem, estamos prevendo algumas coisas. Apenas aceite que assim tudo ficará mais fácil lá na frente, em especial porque utilizaremos recursividade para o inserirNo.

Ok, sabendo agora disso, a primeira chamada ao método inserirNo será com o parâmetro pai como *null*, lá dentro isso será convertido para raiz. Outro passo é verificar se o valor do nosso nó é maior ou menor, para os dois caso, precisamos verificar se o filho à esquerda ou direita é null (ou seja, há uma vaga disponível). Caso isso não seja verdade, precisamos chamar o métodos inseriNo recursivamente, mas agora atualizando o No pai. Nesse caso estamos pulando o nó (esse é um dos princípio da árvores, nela existem subárvores). 


```java
public No inserirNo(No novo, No pai) {
		
		if(pai == null)
			pai = raiz;
		
		if(raiz == null) {
			raiz = novo;
		}else {
			//menor
			if( novo.obterValor().compareTo(pai.obterValor()) == -1) {
				
				if(pai.obterNoEsquerdo() == null)
					pai.inserirEsquerdo(novo);
				else
					inserirNo(novo, pai.obterNoEsquerdo());
				
			}else {
				
				if(pai.obterNoDireito() == null)
					pai.inserirDireito(novo);
				else
					inserirNo(novo, pai.obterNoDireito());
			}
		}
		
		return novo;
		
	}
```

#### 7.1.3 - Busca

A busca na árvores é similar à insersão, pois estamos querendo percorrer um caminho até chegar o nosso nó. Caso encontremos um nó null pelo caminho significa que não há esse valor na árvore. Ao encontrar um elemento com valor igual ao buscado, retornamos esse valor. Em caso do elemento buscado ser maior, vamos para a subárove à direita. Em caso do elemento buscado ser menor, vamos para a subárvores à esquerda. 

```java
public No buscarNo(No novo, No pai) {
		
	if(pai == null)
		pai = raiz;
	
	if(novo == null){
		return null;
	}else if(novo.obterValor().compareTo(pai.obterValor()) == 0) {
		return novo;
	}if( novo.obterValor().compareTo(pai.obterValor()) == -1) {
		
		return buscarNo(novo, pai.obterNoEsquerdo());
			
	}else {
		
		return buscarNo(novo, pai.obterNoDireito());
	}
	
	
}
```

#### 7.1.4 - Remoção

A opreação de remoção em uma árvores é a mais complexa. Antes do métodos de remover precisamos identificar um possível substituto para o nó removido. Para isso vamos criar o método getSucessor que é responsável por retornar o sucessor de um nó dado.

```java
public No getSucessor(No atual, Boolean primeiraVez) {
		
		No sucessor  = null;
		
		if(primeiraVez)
			sucessor = atual.obterNoDireito();
		else
			sucessor = atual;
		
		if(sucessor.obterNoEsquerdo()!=null) {
			return getSucessor(sucessor.obterNoEsquerdo(), false);
		}
		    
		return sucessor; 
	}
```

Esse método retorna um nó que é o sucessor. Como pode ser observado ele é recursivo, no caso da primeira chamada, atualizamos o sucessor para ser o filho á direita. Após isso, estamos interessados em pegar o nó à direita que tenha um espaço vago à sua esquerda. Se isso não for o caso do nó imediatamente à direita, andamos na arvore agora sempre à esquerda em busca desse nó. 

Feito isso, podemos criar o nosso método de remoção. Existem vários caso, e vamos analisá-los um a um. Antes disso temos que ter em mente que queremos buscar o nó, então vamos utilizar as mesas técnicas de antes:

```java
if(currentno.obterValor().compareTo(valor) == 0) {
	//substituiremos o nó aqui
}else if( currentno.obterValor().compareTo(valor) == -1) {
	removerNo(valor, currentno.obterNoDireito());
}else {
	removerNo(valor, currentno.obterNoEsquerdo());
}
```

Será no primeiro if que implementaremos os casos. O nó a ser removido é:

1. é um nó folha? 
2. tem apenas um filho à direita?
3. tem apena um filho à esquerda?
4. tem dois filhos	(direita e esquerda) ?

Dentro do caso 4 precisamos verificar ainda:
1. não é o nó à direita do nó a ser excluído?
2. é o nó à direita do nó a ser excluído?

**Caso 1: é um nó folha?** 

Em caso dele ser um nó folha e for o nó raiz, ou seja, a árvore só possui esse elemento, podemo apenas dizer que o nó raiz é nulo, esvaziando por completo a árvore. Caso o nó folha seja um filho à direita do seu pai, limpamos a referência do filho à direita do pai. O mesmo ocorre para caso ele seja um filho à esquerda.

```java
if((currentno.obterNoDireito()== null) && (currentno.obterNoEsquerdo() == null)) {
				
	if(currentno == this.raiz)
		this.raiz = null;
	
	else if(currentno == currentno.pai.obterNoDireito() )
		currentno.pai.inserirDireito(null);
	else 
		currentno.pai.inserirEsquerdo(null);

}
```


**Caso 2: tem apenas um filho à direita?** 


O segundo caso verifica se ele tem apenas um filho à direita, ou seja, o o filho à esquerda é nulo. Caso o nó seja o raiz, dizemos que a nova raiz será o único filho existente (é como se ele herdasse tudo!). Caso ele seja um filho á direita do pai dele, nós passamos o filho dele para o pai (como se o pai assumisse a guarda do neto). No caso dele ser um filho à esquerda, fazemos o mesmo. 


```java
else if (currentno.obterNoEsquerdo()== null){
	
	if(currentno == this.raiz)
		this.raiz = this.raiz.obterNoDireito();
	
	else if(currentno == currentno.pai.obterNoDireito() )
		currentno.pai.inserirDireito( currentno.obterNoDireito() );
	
	else 
		currentno.pai.inserirEsquerdo( currentno.obterNoDireito() );	
}
```

**Caso 3: tem apena um filho à esquerda?** 

O terceiro caso verifica se ele tem apenas um filho à esquerda, ou seja, o filho à direita é nulo. Caso o nó seja o raiz, dizemos que a nova raiz será o único filho existente. Caso ele seja um filho á direita do pai dele, nós passamos o filho esquerdo dele para o pai, assumindo o seu lugar de filho direito. Caso ele seja um filho à esquerda, o seu filho assume o seu lugar de filho esquerdo. 

```java
else if (currentno.obterNoDireito() == null){
	
	if(currentno == this.raiz)
		this.raiz = this.raiz.obterNoEsquerdo();
	
	else if(currentno == currentno.pai.obterNoDireito() )
		currentno.pai.inserirDireito( currentno.obterNoEsquerdo() );
	
	else 
		currentno.pai.inserirEsquerdo( currentno.obterNoEsquerdo() );
}
```

**Caso 4: tem dois filhos** 

O caso quatro é mais complexo, pois precisamos analisar os subcasos. Vamos lá:

**Caso 4.1: não é o nó à direita do nó a ser excluído**

Caso o sucessor não seja o filho direito do nó que queremos excluir, podemos apneas fazer uma truca. Inserimos o filho direito do sucessor no lugar do filho esquerdo do pai e inseridos o filho direito do nó a ser excluido como filho direito do sucessor. Ou seja, o sucessor assume a guarda do filho que ficará sem pai, pois antes passou o seu filho direito para o pai dele. Sabemos que o pai tem essa disponibilidade pelo próprio algoritmo de obter o sucessor. 

```java
if(sucessor != currentno.obterNoDireito()) {
	
	sucessor.pai.inserirEsquerdo( sucessor.obterNoDireito() );
	sucessor.inserirDireito( currentno.obterNoDireito() );
}
```

**Caso 4.2:  é um nó raiz?**

Bem, feito isso vamos fazer o que já fizemos antes, mas agora passando o próprio sucesso como filho à esquerda ou direita, se for o caso:

```java
if(currentno == this.raiz )
   raiz = sucessor;
else if(currentno == currentno.pai.obterNoDireito()) 
	currentno.pai.inserirDireito(sucessor);
else 
    currentno.pai.inserirEsquerdo(sucessor);
			
```	

#### 7.1.5 - Percurso

Percurso em Árvores é uma forma de percorrer todos os nós em uma determinada ordem. Temos alguns percurso padrões que são: Em Ordem, Pré-Ordem e Pós-Ordem. Para todas as abordagens, podemos utilizar algoritmos recursivos.

**Pré-Ordem**
Os passo para esse percurso é: 1. Vistar a raiz. 2. Percorrer a sua subárvore esquerda em pré-ordem. 3. Percorrer a sua subárvore direita em pré-ordem. 

```java

public void preOrdem(No no) {
	if (no != null) {
		System.out.println(no.valor);
		emOrdem(no.filhoEsquerdo);
		emOrdem(no.filhoDireito);
	}
}

```
**In-Ordem**

Os passo para esse percurso é: 1. Percorrer a sua subárvore esquerda em in-ordem. 2. Vistar a raiz. 3. Percorrer a sua subárvore direita em in-ordem.

```java

public void emOrdem(No no) {
	if (no != null) {
		emOrdem(no.filhoEsquerdo);
		System.out.println(no.valor);
		emOrdem(no.filhoDireito);
	}
}

```
**Pós-Ordem**

Os passo para esse percurso é: 1. Percorrer a sua subárvore esquerda em pós-ordem. 2. Percorrer a sua subárvore direita em pós-ordem. 3. Vistar a raiz.

```java

public void posOrdem(No no) {
	if (no != null) {
		posOrdem(no.filhoEsquerdo);
		posOrdem(no.filhoDireito);
		System.out.println(no.valor);
	}
}

```

**Overview**

```java
public class Arvore<T extends Comparable<T>> {
	No raiz;
	
	public Arvore() {
		this.raiz = null;
	}
	
	public No inserirNo(T valor) {
		No<T> n = new No<T>(valor);
		return inserirNo(n, null);
		
	}
	public No inserirNo(No novo, No pai) {
		
		if(pai == null)
			pai = raiz;
		
		if(raiz == null) {
			raiz = novo;
		}else {
			//menor
			if( novo.obterValor().compareTo(pai.obterValor()) == -1) {
				
				if(pai.obterNoEsquerdo() == null)
					pai.inserirEsquerdo(novo);
				else
					inserirNo(novo, pai.obterNoEsquerdo());
				
			}else {
				
				if(pai.obterNoDireito() == null)
					pai.inserirDireito(novo);
				else
					inserirNo(novo, pai.obterNoDireito());
			}
		}
		
		return novo;
		
	}
	
	
	public No buscarNo(No novo, No pai) {
		
		if(pai == null)
			pai = raiz;
		
		if(novo == null){
			return null;
		}else if(novo.obterValor().compareTo(pai.obterValor()) == 0) {
			return novo;
		}if( novo.obterValor().compareTo(pai.obterValor()) == -1) {
			
			buscarNo(novo, pai.obterNoEsquerdo());
				
		}else {
			
			buscarNo(novo, pai.obterNoDireito());
		}
		
		return novo;
		
	}
	

	public No removerNo(T valor) {
		return removerNo(valor, null);
	}
	
	public No removerNo(T valor, No currentno) {
		
		No noret = null;
		
		if(currentno == null) 
			currentno = raiz;
		
		//igual
		if(currentno.obterValor().compareTo(valor) == 0) {
			//System.out.println(currentno.obterValor() + "é igual");
			//é um nó folha?
			if((currentno.obterNoDireito()== null) && (currentno.obterNoEsquerdo() == null)) {
				
				if(currentno == this.raiz)
					this.raiz = null;
				
				else if(currentno == currentno.pai.obterNoDireito() )
					currentno.pai.inserirDireito(null);
				else 
					currentno.pai.inserirEsquerdo(null);
			
			//tem apena sum filho à direita?
			}else if (currentno.obterNoDireito() == null){
				
				if(currentno == this.raiz)
					this.raiz = this.raiz.obterNoEsquerdo();
				
				else if(currentno == currentno.pai.obterNoDireito() )
					currentno.pai.inserirDireito( currentno.obterNoEsquerdo() );
				
				else 
					currentno.pai.inserirEsquerdo( currentno.obterNoEsquerdo() );
			
			//tem apena sum filho à esquerda?
			}else if (currentno.obterNoEsquerdo()== null){
				
				if(currentno == this.raiz)
					this.raiz = this.raiz.obterNoDireito();
				
				else if(currentno == currentno.pai.obterNoDireito() )
					currentno.pai.inserirDireito( currentno.obterNoDireito() );
				
				else 
					currentno.pai.inserirEsquerdo( currentno.obterNoDireito() );
			
			//tem dois filhos	
			}else {
				
				No sucessor = this.getSucessor(currentno, true);
				System.out.println("O sucessor é:" + sucessor+"\n");
				
				if(sucessor != currentno.obterNoDireito()) {
					
					sucessor.pai.inserirEsquerdo( sucessor.obterNoDireito() );
					sucessor.inserirDireito( currentno.obterNoDireito() );
				}
				
				
				//é a raiz
				if(currentno == this.raiz )
				   raiz = sucessor;
				
				//é o filho a esquerda
				else if(currentno == currentno.pai.obterNoDireito()) 
						currentno.pai.inserirDireito(sucessor);
				else 
						currentno.pai.inserirEsquerdo(sucessor);
			
				sucessor.inserirEsquerdo( currentno.obterNoEsquerdo() );
				
			}
			
			
			
		}else if( currentno.obterValor().compareTo(valor) == -1) {
			//System.out.println(currentno.obterValor() + "é menor que "+valor);
			removerNo(valor, currentno.obterNoDireito());
		}else {
			//System.out.println(currentno.obterValor() + "é mairo que "+valor);
			removerNo(valor, currentno.obterNoEsquerdo());
			
		}
	
		
		return null;
	}
	
	
	public No getSucessor(No atual, Boolean primeiraVez) {
		
		No sucessor  = null;
		
		if(primeiraVez)
			sucessor = atual.obterNoDireito();
		else
			sucessor = atual;
		
		if(sucessor.obterNoEsquerdo()!=null) {
			return getSucessor(sucessor.obterNoEsquerdo(), false);
		}
		    
		return sucessor; 
	}
	
	
	public void emOrdem(No no) {
		if (no != null) {
			emOrdem(no.filhoEsquerdo);
			System.out.println(no.valor);
			emOrdem(no.filhoDireito);
		}
	}
	
	public void preOrdem(No no) {
		if (no != null) {
			System.out.println(no.valor);
			emOrdem(no.filhoEsquerdo);
			emOrdem(no.filhoDireito);
		}
	}
	
	
	public void posOrdem(No no) {
		if (no != null) {
			posOrdem(no.filhoEsquerdo);
			posOrdem(no.filhoDireito);
			System.out.println(no.valor);
		}
	}
	
}
```
Retirado do repositório: https://github.com/LuisAraujo/Estrutura-de-Dados-em-Java

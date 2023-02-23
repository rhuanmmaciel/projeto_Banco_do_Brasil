## 5 - Lista Duplamente Encadeada

A Lista duplamente encadeada, diferentemente da simplesmente, possui dois links para Nós, um para o próximo nó e outro para o nó anterior. Mas para quê? Com a Lista Simplesmente Encadeada já resolvemos os problemas do vetor, mas ainda assim queremos melhorar nosso algoritmo de busca. 

Vamos pensar um pouco: temos uma lista como 1.000 Nós (1,2,3,4... 1000). Desejamos buscar o item número 30, logo varemos 30 interações (nó a nó). Agora queremos buscar o item 29, e novamente faremos mais 29 interações, partindo do início. Agora se em uma lista pudéssemos sair do 30 e voltar para o 29. Nesse caso, só teríamos 1 interação. Legal, não é? 

A esta altura você deve está se perguntando: mais uma lista para aprender?! Não necessariamente, podemos apenas modificar o código da simplesmente encadeada, facilitando a nossa vida. Vejamos pela estrutura a seguir:

 	```java
    public class No<T> {
    	private T valor;
    	private No proximo;	
		private No anterior;
	
		public No(T valor) {
			this.valor = valor;
			proximo = null;
			anterior = null;
		}
    } 
	``` 

#### 5.1 - Inserindo na Lista Duplamente

Os código são similares a simplesmente, como já dito. Basta prestar atenção no novo atributo: o anterior.

#### 5.1.1 - Inserindo no início

Nada muda aqui! 

	´´´java
    public void inserirNoInicio(T  valor) {
    		No<T> novo_no = new No<T>(valor);
			novo_no.proximo = primeiro;
			primeiro = novo_no
	}

	´´´
 
#### 5.1.2 - Inserindo no final

Quase nada muda aqui! Apenas o link do nó anterior do novo_no que precisa ser considerado (novo_no.anterior = auxiliar).

	´´´java
    public void inserirNoFinal(T  valor) {
    		No<T> novo_no = new No<T>(valor);
			No auxiliar = primeiro;
			while(auxiliar.proximo != null) {
				auxiliar = auxiliar.proximo;
			}
			auxiliar.proximo = novo_no.proximo;
			novo_no.anterior = auxiliar;
	}


### 5.1.3 - Inserindo de forma ordenada

Vejamos o código da simplemente:


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
			this.primeiro.anterior = novo_no
			novo_no.proximo = this.primeiro;			
			this.primeiro = novo_no;
		}else{
			novo_no.proximo = auxiliar;
			auxiliar.anterior = novo_no; 
			auxiliar2.proximo = novo_no;
			novo_no.anterior = auxilia2;
		}
	}


Ok! Olhando bem esse código é perceptível que não precisamos mais desse auxiliar2, pois agora podemos acessar auxiliar.anterior!

	public void inserirNoMeio(T  valor) {
		No<T> novo_no = new No<T>(valor);
	
		No<T> auxiliar = primeiro;
		
		while((auxiliar != null) && ( auxiliar.obterValor().compareTo(novo_no.obterValor() )) == -1  )
		{
			auxiliar = auxiliar.proximo();
		}

	 	if(this.primeiro == null) { 
			this.primeiro = novo_no;
		}else if(auxiliar == this.primeiro) {	
			this.primeiro.anterior = novo_no
			novo_no.proximo = this.primeiro;			
			this.primeiro = novo_no;
		}else{
			novo_no.proximo = auxiliar;
			auxiliar.anterior = novo_no; 
			auxiliar.anterior.proximo = novo_no;
			novo_no.anterior = auxilia.anterior;
		}
	}

#### 5.2 - Buscando na Lista Duplamente

Assim como na Lista Simples, podemos buscar um nó tanto pelo seu valor como pelo seu índice. Vamos ver buscar.

#### 5.2.1 - Buscando no início

A busca no início é similar à uma operação de pilha ou de fila, pois estamos interessados em remover de apenas uma das extremidade. Como queremos busca no início e já temos uma atributo que guarda esse valor, basta retorná-lo.

	´´´java
	public No<T> buscarInicio(T valor) {
			
		return primeiro;
	}
	´´´

#### 5.2.2 - Buscando no final

A busca no final é simples: vamos andando na lista até chegar ao final e então retornando o objeto. Para saber se um nó da lista é o último, basta verificar se o próximo dele é nulo. 

	´´´java
	public No<T> buscarNoFinal(T valor) {
		 
		No<T> auxiliar = primeiro;
		 
		while( auxiliar.proximo != null )
		{
			auxiliar = auxiliar.proximo;
		}
		
		return auxiliar;
	}
	´´´

Tanto essa busca como a busca no início pode ser aplicado na lista simples e na lista circular que veremos mais a frente. 

#### 5.2.3 - Buscando por valor em uma lista ordenada

A busca por valor não tem nada de diferente da busca por valor na lista simples. No entanto, caso a sua lista esteja ordenada, nós podemos otimizar essa busca. Imagine que a sua lista possui 10 elementos de valores inteiros e vocês quer buscar o elemento de valor 6, é muito provável que ela esteja no meio da lista. Mas não temos uma variável que guarda o meio da lista. Bem, poderíamos criá-la? Sim! Mas imagine que você quer buscar o elemento de valor 9 ou o de valor 2, seria muito custoso e nada generalista ter um atributos para cada setor da lista. 

Com base nisso, podemos abordar o problema de uma outra forma: imagine que você tenha criado um novo atributo que fica na posição da último nó buscado e com base nele você irá fazer as operações.

```java

public class Lista<T> {
	private No<T> primeiro;
	private No<T> noatual;
}

```
 
A cada busca, nós atualizamos esse ultimobuscado. 


```java

public No<T> buscar(T valor) {
 
No<T> auxiliar = primeiro;
 
while( auxiliar.proximo != null )
{
	auxiliar = auxiliar.proximo;
}
if(auxiliar != null)
	ultimobuscado = auxiliar;

return auxiliar;
}
```

Ok, mas isso não melhorou em nada a nossa busca, pelo contrário, eu tenho agora uma operação de comparação e outra de atribuição. Bem, para isso precisamos fazer a seguinte abordagem: dado o último nó buscado, verificamos se o valor é maior ou menor que ele, se for maior, vamos para o próximo, se for menor vamos para o anterior. 

```java
public No<T> buscarPorValor(T valor) {
	
		
	if(no_atual== null)
		no_atual = primeiro;
	
	while((no_atual != null) && (no_atual.obterValor().compareTo( valor )) != 0  )
	{
		if (no_atual.obterValor().compareTo(valor)==-1)
            no_atual = no_atual.obterProximo();
        else 
            no_atual=no_atual.obterAnterior();	
	}
	
	return no_atual;
}	
```

Que bacana, não é? Teste a quantidade de comparações necessárias para se buscar um valor, em uma sequência aleatória e logo verá que esse método é muito melhor que o da lista simples que inicia no inicio e varria toda a lista. Você pode usar o método *buscarCount* na Lista Duplamente. O pior caso dessa busca é igual à busca simples percorreremos n nós. Mas, na média, vamos percorrer apenas n/2. 

#### 5.2.4 - Buscando por índice

A busca pelo índice é similar. Mudamos apenas o valor pelo índice. 


```java
public class Lista<T> {
	private No<T> primeiro;
	private No<T> noatual;
	private Int index;
}
```


Agora estamos comparando um valor inteiro. Caso o índice seja menor fazemos um loop com incremento, caso contrário como decremento. 

```java
public No<T> buscarPorIndice(int indexbusca) {
	int i;
	
	if(no_atual == null){
		no_atual = primeiro;
		index = 0;
	}
	
	if (no_atual.obterValor().compareTo(valor)==-1){
            
			for(i = index; i < indexbusca; i++){
				if(no_atual == null)
					return null;

				no_atual = no_atual.obterProximo();
			}	
			

    } else {
            for(i = index; i > indexbusca; i--){
				if(no_atual == null)
					return null;

				no_atual = no_atual.obterProximo();
			}		
	}

	index = i;
	return no_atual;
}
```

É importante ainda sempre verificar se o nó é nulo, pois o índice pode ser maior que o tamanho da lista ou em caso do índice ser negativo.

#### 5.3 - Removendo na Lista Duplamente

A remoção na lista duplamente é como a lista simples, no entanto temos que ter uma atenção para o novo parâmetro do nó: o anterior. 

#### 5.3.1 - Removendo no início

Nós já conhecemos esse método, precisamos apenas adicionar o primeiro.anterior = null, por dois motivos: o primeiro nó não possui anterior a ele e eliminar a referência do nó removido da nossa lista;

```java
public No<T> removerInicio() {
	 
	No<T> auxiliar = primeiro;
	primeiro = primeiro.próximo;
	primeiro.anterior = null;
	auxiliar.proximo = null;
	return auxiliar;
}
```

#### 5.3.2 - Removendo no final

O mesmo vale para esse novo código.
	
```java
public No<T> removerFinal() {
	 
	No<T> auxiliar = primeiro;
	No<T> auxiliar2 = null;

	while((auxiliar.proximo != null))
	{
		auxiliar2 = auxiliar;
		auxiliar = auxiliar.proximo;
	}

	auxiliar.anterior = null;
	auxiliar2.proximo = null;

	return auxiliar;
}
```

Uma observação é importante aqui, podemos reduzir esse código utilizado o métodos de busca no final. 

```java
public No<T> removerFinal() {
	 
	No<T> auxiliar = buscarNoFinal();
	
	if(auxiliar != null){
		auxiliar.anterior = null;
		auxiliar.anterior.proximo = null;
	}

	return auxiliar;
}
```

#### 5.3.3 - Removendo por valor

Vamos usar a mesma abordagem do código anterior e utilizar o método de busca por valor.

```java
public No<T> removerPorValor() {
	 
	No<T> auxiliar = buscarPorValor();
	
	if(auxiliar != null){
		if(auxiliar.proximo != null)
			auxiliar.proximo.anterior = auxiliar.anterior;
			
		if(auxiliar.anterior != null)
			auxiliar.anterior.proximo = auxiliar.próximo;
	}

	return auxiliar;
}
```

#### 5.3.4 - Removendo por índice

Mas usam vez vamos reutilizar código, afinal para que serve utilizar Orientação a Objeto, se não fazemos uso das suas potencialidades?

```java
public No<T> removerPorValor() {
	 
	No<T> auxiliar = buscarPorÍndice();
	
	if(auxiliar != null){
		if(auxiliar.proximo != null)
			auxiliar.proximo.anterior = auxiliar.anterior;
			
		if(auxiliar.anterior != null)
			auxiliar.anterior.proximo = auxiliar.próximo;
	}

	return auxiliar;
}
```
**Overview**

```java
public class No<T extends Comparable<T>> {
	
	private T valor;
	private No proximo;
        private No anterior;
	
	public No(T valor) {
		this.valor = valor;
		proximo = null;
                
	}
	
	/**obtém o próximo nó */
	public No<T> obterProximo() {
		return this.proximo;
	}
        
        public No<T> obterAnterior() {
		return this.anterior;
	}
	/**inserir o próximo nó */
	public void inserirProximo(No proximo) {
		this.proximo = proximo;
	}
        
        public void inserirAnterior(No anterior) {
		this.anterior = anterior;
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

public class ListaDuplamente< T extends Comparable<T>> {
    
    
	No<T> primeiro;
    No<T> no_atual = primeiro;
	
	
	public void inserir(T  valor) {
		No<T> novo_no = new No<T>(valor);
		No<T> auxiliar = primeiro;
		
		if(this.primeiro == null) { 
			this.primeiro = novo_no;
		
		}else{
		
			while((auxiliar.obterProximo() != null) && 
			( auxiliar.obterValor().compareTo( novo_no.obterValor() ) == -1 ) )
			{
				auxiliar = auxiliar.obterProximo();
			}
			
			if(auxiliar == this.primeiro) {
				
				if(this.primeiro.obterValor().compareTo( novo_no.obterValor() ) == -1 ) {
					
					this.primeiro.inserirProximo(novo_no);
					novo_no.inserirAnterior(this.primeiro);

				}else {
					
					novo_no.inserirProximo(this.primeiro);
					this.primeiro.inserirAnterior(novo_no);
					this.primeiro = novo_no;
				}
				
			}else {
				
				if(auxiliar.obterProximo() == null) {
					novo_no.inserirAnterior(auxiliar);
					auxiliar.inserirProximo(novo_no);
				}else {
				novo_no.inserirProximo(auxiliar);
				novo_no.inserirAnterior(auxiliar.obterAnterior());
	            auxiliar.obterAnterior().inserirProximo(novo_no);
	            auxiliar.inserirAnterior(novo_no);
				}
			}
			
		}
	
	}
        
       
	public No<T> remover(T valor) {//arrumada 
		
		No<T> auxiliar = primeiro;
		
                No<T> retorno =null;

		while((auxiliar != null) && (auxiliar.obterValor().compareTo( valor ) != 0)  )
		{
			auxiliar = auxiliar.obterProximo();
		}
		
		
		if(auxiliar == this.primeiro) {
			
			retorno = this.primeiro;
                        retorno.inserirProximo(null);
			this.primeiro = this.primeiro.obterProximo();
                        this.primeiro.inserirAnterior(null);
			
		
		}else if(auxiliar != null)
			auxiliar.obterAnterior().inserirProximo(auxiliar.obterProximo());
                auxiliar.obterProximo().inserirAnterior(auxiliar.obterAnterior());
                auxiliar.inserirProximo(null);
                auxiliar.inserirAnterior(null);
	
		
		return retorno;
		
	}
	
	
	public No<T> buscar(T valor) {
		
			
		if(no_atual== null)
			no_atual = primeiro;
		
		while((no_atual != null) && (no_atual.obterValor().compareTo( valor )) != 0  )
		{
			if (no_atual.obterValor().compareTo(valor)==-1){
                no_atual = no_atual.obterProximo();
            }
            else 
                no_atual=no_atual.obterAnterior();
	
			
		}
		
	
		
		return no_atual;
	}
	
	
	public String buscarCount(T valor) {
		
		int count = 0;
		
		if(no_atual== null)
			no_atual = primeiro;
		
		while((no_atual != null) && (no_atual.obterValor().compareTo( valor )) != 0  )
		{
			count++;
            if (no_atual.obterValor().compareTo(valor)==-1){
                no_atual = no_atual.obterProximo();
            }
            else 
                no_atual=no_atual.obterAnterior();
		}
		
		
		return "Achou "+no_atual.obterValor()+" com "+count + " passos";
	}
	

	public String toString() {
		String s = "";
		No<T> auxiliar = primeiro;
		
		while(auxiliar != null)
		{
			
			s+= auxiliar.obterValor().toString() + " - ";

			auxiliar = auxiliar.obterProximo();
		}
		
		return s;
	} 
	
}
```

Retirado do repositório: https://github.com/LuisAraujo/Estrutura-de-Dados-em-Java

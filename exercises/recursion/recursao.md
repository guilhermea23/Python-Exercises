Resumo de Recursão

Todos os algoritmos recursivos devem obedecer três leis importantes: 
    
    * Um algoritmo recursivo deve possuir um caso base 
    
    >>>(if numero >= 0)
    * Um algoritmo recursivo deve modificar o seu estado e se aproximar do caso base
    >>> (numero - 1) 
    * Um algoritmo recursivo deve chamar a si mesmo, recursivamente 
    >>>ate_zero(numero - 1))

A ideia é simples, dado um problema cuja estrutura se repete, basta replicar o processo de solução para uma versão um pouco menor do mesmo problema, até que se chegue a uma versão tão pequena, tão simples que você já sabe a resposta e, portanto, não precisa continuar computando. 

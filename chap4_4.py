## Escreva um programa com duas funções.
## A primeira função deve receber um inteiro como parametro e retornar o resultado do inteiro dividido por 2.
## A segunda função deve receber um inteiro como parâmetro e retornar o resultado do inteiro multiplicado por 4.
## Chame a primeira função, salve o resultado como uma variável e passe-a como parâmetro para a segunda função.

def first_f(x):
    return x / 2

def second_f(b):
    return b * 4

a = first_f(10)
y = second_f(a)
print(y)




        ## Dissecando o exercicio: ##


## 1 - PRIMEIRA FUNÇÃO                                          .  ---> def first_f(x)

## 2 - INTEIRO COMO PARÂMETRO                                   .  ---> (x)

## 3 - RETORNANDO O RESULTADO DO INTEIRO DIVIDO POR 2           .  ---> return x / 2



## 1 - SEGUNDA FUNÇÃO                                           .  ---> def second_f(b)

## 2 - INTEIRO COMO PARÂMETRO                                   .  ---> (b)

## 3 - RETORNANDO O RESULTADO DO INTEIRO MULTIPLICADO POR 2     .  ---> return x * 4




## 4 - CHAMANDO A PRIMEIRA FUNÇÃO                               .  ---> a = first_f()

## 5 - SALVE O RESULTADO COMO UMA VARIÁVEL                      .  ---> a = first_f(10)   obs.: O sinal de igual é usado quando você está ATRIBUINDO UM VALOR a uma variável, como no caso do exercicio

## 6 - PASSE-A COMO PARAMETRO PARA A PRIMEIRA FUNÇÃO            .  ---> y = second_f(a)



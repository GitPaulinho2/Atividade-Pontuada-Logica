// Criando um vetor
console.clear()

lista = []
par = 0
impar = 0

const readline = require('readline-sync')
const quant = readline.questionInt("Digite a quantidade de numeros desejados: ") 
console.clear()

for (let i =1; i <=quant; i++){
    const num = readline.questionInt(`digite o ${i} numero: `)
    if (num % 2 == 0){
        par += 1 
    }else{
        impar += 1
    }
    console.log(num)
}

console.log(`Números Pares: ${par}`)
console.log(`Números Impares: ${impar}`)
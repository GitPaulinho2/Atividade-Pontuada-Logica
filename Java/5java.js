// Criando um vetor
console.clear()

lista = []
soma = 0

const readline = require('readline-sync')
const quant = readline.questionInt("Digite a quantidade de numeros desejados: ") 
console.clear()

for (let i =1; i <=quant; i++){
    const num = readline.questionInt(`digite o ${i} numero: `)
    soma += num
    console.log(num)
}
media = soma/quant

console.log(`Média: ${media}`)
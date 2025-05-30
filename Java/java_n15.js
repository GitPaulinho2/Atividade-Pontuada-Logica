console.clear()
const readline = require('readline-sync')
console.log("")

const num1 = readline.questionInt("digite o numero 1: ")
const num2 = readline.questionInt("digite o numero 2: ")

function verificando(){
    soma = num1 + num2 / 2
    media = soma / 2
    console.log(`Média: ${media}`)
}
verificando(num1, num2)
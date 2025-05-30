console.clear()
const readline = require('readline-sync')
console.log("")
const n1 = readline.questionInt("digite o numero 1: ")
const n2 = readline.questionInt("digite o numero 2: ")
console.log("")

const somar = (n1, n2) => {
    return n1 + n2
}
const subtrair = (n1, n2) => n1 - n2 
const multiplicar = (n1, n2) => n1 * n2
const dividir = (n1, n2) => n1 / n2

const soma = somar(n1,n2)
const subtracao = subtrair(n1,n2)
const multiplicacao = multiplicar(n1,n2)
const divisao = dividir(n1,n2)

console.log(`Soma: ${soma}`)
console.log(`Subtrair: ${subtracao}`)
console.log(`Multiplicação: ${multiplicacao}`)
console.log(`Divisão: ${divisao}`) 
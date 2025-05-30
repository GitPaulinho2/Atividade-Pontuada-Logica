console.clear()
const readline = require('readline-sync')
console.log("")
const num = readline.questionInt("digite o numero: ")

function verificando(){

    if (num < 0){
        console.log("O numero eh negativo")
    } else if (num > 0){
        console.log("O numero eh positivo")
    }
}

verificando(num)
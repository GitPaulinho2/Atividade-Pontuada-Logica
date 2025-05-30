// npm install readline-sync
console.clear()

const readline = require('readline-sync')
console.log("")

let num = readline.questionInt("Digite um numero para ser feliz: ")
console.log("")

if (num % 2 == 0){
    console.log(`${num} é numero par`)
}else if (num)
    console.log(`${num} é numero impar`)

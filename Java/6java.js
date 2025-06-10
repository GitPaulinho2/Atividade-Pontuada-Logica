// npm install readline-sync

const readline = require('readline-sync')
console.log("")
const idade = readline.questionInt("Digite sua idade: ")
console.log("")
if (idade <18){
console.log("Menor de idade")
}else{
    console.log("maio de idade")

}


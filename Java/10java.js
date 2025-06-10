// npm install readline-sync
console.clear()

const readline = require('readline-sync')
console.log("")
let idade = readline.questionInt("Digite sua idade: ")
console.log("")
if (idade >=16){
    console.log("== VOTO OPCIONAL ==")
}else if(idade >=18){
    console.log("== OBRIGADO A VOTAR ==")
}else if(idade>65){
    console.log("= NÃO É OBRIGADO A VOTAR")
}else if(idade<16){
    console.log("tu é broxa")
}


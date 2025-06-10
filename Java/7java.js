// npm install readline-sync
let soma=0
const readline = require('readline-sync')
const quant = readline.questionInt("Digite a quantidade de numero(s): ")
console.log("")
for (let i =1; i <=quant; i++){
    const num1 = readline.questionInt(`Digite o ${i}º numero: `);
    console.log("")
    soma+=num1;
}
media=soma/quant

console.log("soma: " + soma)
console.log("")
console.log("media: " + media)


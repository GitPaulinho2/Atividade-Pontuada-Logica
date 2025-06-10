// Criando um vetor
console.clear()

lista = []
positivo = 0
negativo = 0
soma = 0
const readline = require('readline-sync')
const quant = readline.questionInt("Digite a quantidade de numeros desejados: ") 
console.clear()

for (let i =1; i <=quant; i++){
    const num = readline.questionInt(`digite o ${i} numero: `)
    if (num < 0){
         negativo += 1
    }else if(num > 0){ 
        positivo += 1
        soma += num
    }
    console.log(num)
}

console.log(`Números Positivo: ${positivo}`)
console.log(`Números Negativo: ${negativo}`)
console.log(`Soma dos positivos: ${soma}`)
// npm install readline-sync
console.clear()

const readline = require('readline-sync')
console.log("")

let dia = readline.questionInt("Digite um dia; 1- Domingo, 2- Segunda, 3- Terca, 4- Quarta, 5- Quinta, 6- Sexta, 7- Sabado: ")
console.log("")

switch (dia){
    case 1:
        console.log("Domingo\n")
        console.log("Fim de semana")
        break
        case 2:
            console.log("Segunda")
            console.log("Dia util")
            break
            case 3:
                console.log("Terça")
                console.log("Dia util")
                break
                case 4:
                    console.log("Quarta")
                    console.log("Dia util")
                    break
                    case 5:
                        console.log("Quinta")
                        console.log("Dia util")
                        break
                        case 6:
                            console.log("Sexta")
                            console.log("Dia util")
                            break
                                case 7:
                                    console.log("Sábado")
                                    console.log("Fim de semana")
                                    break
                                    default:
                                }
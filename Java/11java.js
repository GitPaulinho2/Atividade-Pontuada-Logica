const alunos = ['Marta', 'Jose', 'Maria']
console.log('\nExibindo todos os elementos.')
console.log(alunos)

console.log('\nExibindo apenas o primeiro elementos.')
console.log(alunos[0])

console.log('\nExibindo apenas o último elementos.')
console.log(alunos[2])

console.log('\nAdicionando um elemento no final do vetor.')
alunos.push('Ana')
console.log(alunos)

console.log('\nAdicionando um elemento no início do vetor.')
alunos.unshift('Marilia')
console.log(alunos)

console.log('\nRemovendo um elemento no final do vetor.')
alunos.pop()
console.log(alunos)

console.log('\nRemovendo apenas um elemento do vetor.')
alunos.pop(2) // Removendo o terceiro elemento do vetor.
console.log(alunos)
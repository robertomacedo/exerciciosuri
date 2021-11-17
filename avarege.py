"""
Leia quatro números (N1, N2, N3, N4), que um com 1 dígito após o ponto decimal, 
correspondendo a 4 pontuações obtidas por um aluno. Calcule a média com os pesos 2, 3, 4 e 1, 
respectivamente, para estas 4 pontuações e imprima a mensagem "Mídia: "(Média), seguida pelo 
resultado calculado. Se a média foi de 7,0 ou mais, imprima a mensagem "Aluno aprovado". 
(Aluno Aprovado). Se a média foi inferior a 5,0, imprima a mensagem: "Aluno reprovado". 
(Aluno reprovado). Se a média foi entre 5,0 e 6,9, incluindo elas, o programa deve imprimir 
a mensagem "Aluno em exame". (No exame de aluno)

Em caso de exame, leia mais uma pontuação. Imprima a mensagem "Nota do exame: 
"(Pontuação do exame) seguida da pontuação digitada. Recalcular a média 
(soma a pontuação do exame com a média calculada anterior e dividir por 2) 
e imprimir a mensagem "Aluno aprovado". (Aluno aprovado) em caso de média de 5,0 ou mais) 
ou "Aluno reprovado". (Aluno reprovado) em caso de média de 4,9 ou menos. Para estes dois 
casos (aprovados ou reprovados após o exame) imprima a mensagem "Mídia final: "(Média final) 
seguida da média final para este aluno na última linha
"""

num = input().split()

n1 = float(num[0])
n2 = float(num[1])
n3 = float(num[2])
n4 = float(num[3])


peso = n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1

result = peso/(2+3+4+1)

media = input()

print(f'Media: {result}')
media_final = (result + media)/2

if media <= 5.4:
    print('Aluno reporvado')
elif media >= 4.9:
    print('Aluno em exame')
    print(f'Nota do exame: {media}')
    print('Aluno aprovado')
    print(f'Media final: {media_final}') 
else:
    pass

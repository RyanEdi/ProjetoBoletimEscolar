#NOTAS DE AVALIAÇÕES

#Espaço reservado para conexão SQL



#INDICE DE MATÉRIAS
class disciplinas:
    mat = "MATEMÁTICA"
    por = "PORTUGUÊS"
    geo = "GEOGRAFIA"
    his = "HISTÓRIA"
    red = "REDAÇÃO"
    ing = "INGLÊS"
    esp = "ESPANHOL"
    edu = "EDUCAÇÃO FÍSICA"
    fis = "FÍSICA"
    qui = "QUÍMICA"
    bio = "BIOLOGIA"
    cie = (fis)+(qui)+(bio)
    cie = "CIÊNCIAS"


#VALOR DE MULTIPLICAÇÃO DE NOTAS
s1 = 0.13
s2 = 0.27
s3 = 0.2
s4 = 0.4

print('BEM VINDO AO BOLETIM ESCOLAR\n')

print("Insira o número conforme a sua matéria: \n")
materia = input("\n" + "1 - MATEMÁTICA" +
                "\n" + "2 - PORTUGUÊS" +
                "\n" + "3 - GEOGRAFIA" +
                "\n" + "4 - HISTÓRIA" +
                "\n" + "5 - REDAÇÃO" +
                "\n" + "6 - INGLÊS" +
                "\n" + "7 - ESPANHOL" +
                "\n" + "8 - EDUCAÇÃO FÍSICA" +
                "\n" + "9 - FÍSICA" +
                "\n" + "10 - QUÍMICA" +
                "\n" + "11 - BIOLOGIA")

if materia == "1":
    print("Você escolheu MATEMÁTICA!\n")


#Nota Bimestral 1
print('Notas - Bimestre 1\n')
ab1 = eval(input("Informe a nota ab1: "))
if ab1 > 4:
    raise Exception('A nota da prova Ab1 não pode ser maior do que 4!')
ab2 = eval(input("Informe a nota ab2: "))
if ab2 > 4:
    raise Exception('A nota da prova Ab2 não pode ser maior do que 4!')
formativa = eval(input("Informe a nota formativa: "))
if formativa > 2:
    raise Exception('A nota da formativa não pode ser maior do que 2!')

bimestral1 = ab1+ab2+formativa
print(f"Sua nota bimestral é: {bimestral1}\n")

#Nota Bimestral 2
print('Notas - Bimestre 2\n')
ab12 = eval(input("Informe a nota ab1: "))
ab22 = eval(input("Informe a nota ab2: "))
formativa2 = eval(input("Informe a nota formativa: "))

bimestral2 = ab12+ab22+formativa2
print(f"Sua nota bimestral é: {bimestral2}\n")

#Nota Bimestral 3
print('Notas - Bimestre 3\n')
ab13 = eval(input("Informe a nota ab1: "))
ab23 = eval(input("Informe a nota ab2: "))
formativa3 = eval(input("Informe a nota formativa: "))

bimestral3 = ab13+ab23+formativa3
print(f"Sua nota bimestral é: {bimestral3}\n")

#Nota Bimestral 4
print('Notas - Bimestre 4\n')
ab14 = eval(input("Informe a nota ab1: "))
ab24 = eval(input("Informe a nota ab2: "))
formativa4 = eval(input("Informe a nota formativa: "))

bimestral4 = ab14+ab24+formativa4
print(f"Sua nota bimestral é: {bimestral4}\n")

media_final = (bimestral1*s1)+(bimestral2*s2)+(bimestral3*s3)+(bimestral4*s4)
print(f'Sua média final é igual a: {media_final}')

if(media_final>=6):
    situacao = "APROVADO"
else:
    situacao = "EM RECUPERAÇÃO"

print(f"O aluno está: {situacao} em {materia}!\n")

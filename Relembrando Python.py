import random
def definirGrupos():
   
    Pessoas = obterPessoas()
    Grupos = []
    GrupoCorrente = []
    while len(Pessoas) > 0:
        Integrante = random.choice(Pessoas)
        if len(GrupoCorrente) >= maxIntegrantes:
            Grupos.append(GrupoCorrente)
            GrupoCorrente = []

        GrupoCorrente.append(Integrante)

        if len(Pessoas) == 1:
            Grupos.append(GrupoCorrente)

        Pessoas.remove(Integrante)

    listarGrupos(Grupos)

def obterPessoas():

    global maxIntegrantes
    maxIntegrantes = int(input("Digite o número de integrantes para cada grupo: "))
    print('* ATENÇÃO, digite 0 para finalizar a lista de pessoas. \r\n')
    Pessoas = []
    Nome = ''

    while Nome != '0':
        Nome = str(input("Informe o nome: "))

        if Nome == '':
            print('Infome um nome válido! ')
        else:
            if Nome != '0':
                Pessoas.append(Nome)

    return Pessoas

def listarGrupos(grupos):
    nrGrupos = int(0)
    while nrGrupos < len(grupos):
        GrupoCorrente = grupos[nrGrupos]
        nrGrupos = nrGrupos + 1
        print ('Grupo ' + str(nrGrupos), GrupoCorrente)

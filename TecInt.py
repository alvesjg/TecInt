def ord(lista,inicio,fim):
    if (fim <= inicio):
        return
    else:
        inst=lista[fim]
        comparador = inicio
        for j in range(inicio,fim):
            if lista[j] <= inst:
                lista[comparador],lista[j] = lista[j],lista[comparador]
                comparador += 1
        lista[comparador],lista[fim] = lista[fim],lista[comparador]
        ord(lista,inicio,comparador-1)
        ord(lista,comparador+1,fim)


def ord_id(lista,inicio,fim):
    if (fim <= inicio):
        return
    else:
        inst = lista[fim][1]
        comparador = inicio
        for j in range(inicio,fim):
            if lista[j][1] <= inst:
                lista[comparador],lista[j] = lista[j],lista[comparador]
                comparador +=1
        lista[comparador],lista[fim] = lista[fim],lista[comparador]
        ord_id(lista,inicio,comparador-1)
        ord_id(lista,comparador+1,fim)


def class_idade(idade : int):
    if idade < 12:
        return "criança"
    elif idade < 19:
        return "adolescente"
    elif idade < 65:
        return "adulto"
    else:
        return "idoso"

def nova_pes(pessoas : dict):
    nome = input("Por favor, insira o nome da pessoa:  ")
    nome = nome[0].upper() + nome[1:]
    idade= int(input("Por favor, insira a idade da pessoa:  "))
    pessoas[nome] = idade
    return

def lista_of(pessoas : dict):
    nomes = list(pessoas.keys())
    ord(nomes,0,len(pessoas)-1)
    for k in nomes:
        print(f"{k}, {class_idade(pessoas[k])} com {pessoas[k]} anos")
    return 

def lista_idade(pessoas : dict):
    tuple_idade = list(pessoas.items())
    ord_id(tuple_idade,0,len(tuple_idade)-1)
    for k in tuple_idade:
        print(f"{k[0]}, {class_idade(k[1])} com {k[1]} anos ")
    return

def main():
    print("Bem vindo ao gerenciamento de pessoas!")
    pessoas={}
    while True:
        opcoes = input("Insira o número referente a opção que você deseja: 1 para adicionar uma nova pessoa, 2 para visualizar as pessoas por ordem alfabética, 3 para visualizar as pessoas por idade, 4 para sair\n")
        if opcoes == "1":
            nova_pes(pessoas)
        elif opcoes =="2":
            lista_of(pessoas)
        elif opcoes=="3":
            lista_idade(pessoas)
        elif opcoes=="4":
            print("Até mais!")
            break
        else:    
            print("Por favor, insira uma opção válida")


if __name__ == '__main__':
   main()

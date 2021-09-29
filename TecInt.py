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
    for k in sorted(pessoas):
        print(f"{k}, {class_idade(pessoas[k])} com {pessoas[k]} anos")
    return 

def lista_idade(pessoas : dict):
    pessoas = dict(sorted(pessoas.items(), key=lambda item: item[1]))
    for k in pessoas:
        print(f"{k}, {class_idade(pessoas[k])} com {pessoas[k]} anos ")
    return

def main():
    print("Bem vindo ao gerenciamento de pessoas!")
    pessoas={}
    while True:
        opcoes = int(input("Insira o número referente a opção que você deseja: 1 para adicionar uma nova pessoas, 2 para visualizar as pessoas por ordem alfabética, 3 para visualizar as pessoas por idade, 4 para sair\n"))
        if opcoes == 1:
            nova_pes(pessoas)
        elif opcoes ==2:
            lista_of(pessoas)
        elif opcoes==3:
            lista_idade(pessoas)
        elif opcoes==4:
            print("Até mais!")
            break
        else:    
            print("Por favor, insira uma opção válida")


if __name__ == '__main__':
   main()

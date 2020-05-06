


nome_funcao = "CONTINGENCIA NFCe ON/OFF"
nome_funcao = "IMPRIMIR COMPROVANTE"


def encontra():
    print("encontraFuncao() - nome_funcao: " + nome_funcao)
    wait(imagem)
    numero = 1
    numero_funcao = ""
    while(numero < 3):
        try:
            numero = numero + 1
            findText(nome_funcao)
            print("encontraFuncao() - nome_funcao: " + nome_funcao + " - encontrada")
            regiao = findText(nome_funcao)
            regiao.highlight(1)
            regiao.left(40).highlight(2)
            numero_funcao = regiao.left(40).text()
            numero_funcao = numero_funcao[:2]
            print("encontraFuncao() - numero_funcao: " + numero_funcao + " - encontrado")
        except:
            print("encontraFuncao() - nome_funcao: " + nome_funcao + " - nao encontrada")
            for _ in range(6):
                type(Key.DOWN)
            wait(1)

print("encontraFuncao() - nome_funcao: " + nome_funcao)
regiao = findAll(nome_funcao)
regiao.highlight(1)
regiao.left(40).highlight(2)
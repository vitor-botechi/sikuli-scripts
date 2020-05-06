

def testeTodos():
    print("testeTodos()")

### Faz venda no PDV com 1 produto ###
def testeUm():
    print("testeUm()")

### Faz venda no PDV com 3 produtos diferentes ###
def testeDois():
    print("testeDois()")

### Faz venda no PDV com 3 produtos diferentes e cancela cupom anterior ###
def testeTres():
    print("testeTres()")

### Faz venda no PDV com 2 produtos diferentes aplicando desconto de valor no último item ###
def testeQuatro():
    print("testeQuatro()")

### Faz venda no PDV com 2 produtos diferentes aplicando desconto de porcentagem no último item ###
def testeCinco():
    print("testeCinco()")



n = -1
dicionario_dois = {
        str(n+1) + " - Todas" : testeTodos,
        str(n+1) + " - VendaPDV_1_Produto" : testeUm,
        str(n+1) + " - VendaPDV_3_Produtos" : testeDois,
        str(n+1) + " - VendaPDV_3_Produtos / CancelaCupomAnterior" : testeTres,
        str(n+1) + " - VendaPDV_2_Produtos / DescontoValorItem" : testeQuatro,
        str(n+1) + " - VendaPDV_2_Produtos / DescontoPorcentagemItem" : testeCinco
}

n = -1
dicionario_um = {
        0 : dicionario_dois[str(n+1) + " - Todas"],
        1 : dicionario_dois[str(n+1) + " - VendaPDV_1_Produto"],
        2 : dicionario_dois[str(n+1) + " - VendaPDV_3_Produtos"],
        3 : dicionario_dois[str(n+1) + " - VendaPDV_3_Produtos / CancelaCupomAnterior"],
        4 : dicionario_dois[str(n+1) + " - VendaPDV_2_Produtos / DescontoValorItem"],
        5 : dicionario_dois[str(n+1) + " - VendaPDV_2_Produtos / DescontoPorcentagemItem"]
}



opcoes = list(sorted(dicionario_dois))



### Adicionar danfe simplificado no numero 3 e 4

selecionada = select("Escolha qual automacao voce deseja:", "Teste", opcoes)







popup("Automacao finalizada sem erros!", "Automacao NFC-e")







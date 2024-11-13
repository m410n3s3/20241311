
Dicionario = {}
TamanhoMinimoPalavra = 4
CaracteresBasicos = '",.!?:-;()'
CaracteresExtras = "'"
CaracteresRemover = CaracteresExtras + CaracteresBasicos
while True:
    try:
        Linha = input().split()
        if Linha != "":
            for i in range (len(Linha)):
                Palavra = (Linha[i].strip(CaracteresRemover)).lower()
                if len(Palavra) >= TamanhoMinimoPalavra:
                    k = Dicionario.get(Palavra)
                    if k == None:
                        Dicionario[Palavra]=1
                    else:
                        Dicionario[Palavra]+=1
    except EOFError as Er:
        break
Dicionario_Decrescente = dict(sorted(Dicionario.items(), key=lambda item: item[i],
reverse=True))

for chave, valor in Dicionario_Decrescente.items():
    print(chave , valor)

#função para carregar o arquivo, com separador de dados e tipo de dados
def carrega_arquivo(nome_arquivo, separador, tipos):
    arquivo = open(nome_arquivo, 'r')
    linhas = arquivo.readlines()

    cabecalho = linhas[0].replace('\n', '').split(separador)

    dados = linhas[1:]

    valores = []

    # Percorre as linhas
    for linha in dados:
        dados_linha = linha.replace('\n', '').split(separador)

        valor = {}

        # Percorre as colunas de cada linha
        for coluna, tipo in enumerate(tipos):
            campo = cabecalho[coluna]
            valor[campo] = converter_valor(dados_linha[coluna], tipo)

        valores.append(valor)

   
    return valores

def cabecalho(nome_arquivo, separador, tipos):
    arquivo = open(nome_arquivo, 'r')
    linhas = arquivo.readlines()

    cabecalho = linhas[0].replace('\n', '').split(separador)

    return cabecalho


#função para converter o valor de cada linha
def converter_valor(valor,tipo):
    if tipo == int:
        return int(valor)
    elif tipo == float:
        return float(valor)
    elif tipo == bool:
        return bool(valor)
    elif tipo == str:
        return (valor)



#função para salvar dados solicitados
def salvar_dados(nome_arquivo, separador, dados):
    f = open(nome_arquivo, 'w')

    cabecalho_str = ''

    cabecalho = list(dados[0].keys())

    for coluna in cabecalho:
        cabecalho_str += coluna
        if coluna != cabecalho[-1]:
            cabecalho_str += separador
    cabecalho_str += '\n'

    f.write(cabecalho_str)

    for index, linha in enumerate(dados):
        linha_str = ''
        for coluna, valor in linha.items():
            linha_str += str(valor)
            if coluna != cabecalho[-1]:
                linha_str += separador
        if index < len(dados) - 1:
            linha_str += '\n'
        f.write(linha_str)

    f.close()

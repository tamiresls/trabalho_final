
#função para localizar dados: acessar um ou mais registros da base de dados por um único índice, 
# por uma lista de índices, ou até por intervalo de índices.
def localizar(dados,linha):
    quant_registros = len(dados)
    if linha < quant_registros:
        return dados[linha]
    else:
        print('Índice superior a quantidade de registro')
        return{}

#função para filtrar dados solicitados: é definida como a utilização de apenas alguns registros da base de dados.
def filtrar(dados, campo, valor, operacao):
    dados_filtrados = []
    for linha in dados:
        if operacao == '==':
            if linha[campo] == valor:
                dados_filtrados.append(linha)
        elif operacao == '>':
            if linha[campo] > valor:
                dados_filtrados.append(linha)
        elif operacao == '>=':
            if linha[campo] >= valor:
                dados_filtrados.append(linha)
        elif operacao == '<':
            if linha[campo] < valor:
                dados_filtrados.append(linha)
        elif operacao == '<=':
            if linha[campo] <= valor:
                dados_filtrados.append(linha)   
        elif operacao == '!=':
            if linha[campo] != valor:
                dados_filtrados.append(linha)   
    return dados_filtrados 

#função para projeção dos dados: é a utilização de apenas alguns campos dos dados que estamos trabalhando.

def projetar(dados, colunas):
    dados_projetados = []
    for linha in dados:
        linha_projetada = {}
        for campo, valor in linha.items():
            if campo in colunas:
                linha_projetada[campo] = valor
        dados_projetados.append(linha_projetada)
    return dados_projetados

def projetar2(dados, colunas):
    return [{campo: valor for campo, valor in linha.items() if campo in colunas} for linha in dados]



#função agrupamento: o agrupamento é a organização dos dados baseado em um atributo com valor em comum.

def agrupar(dados, coluna, coluna2):

    dados_agrupados = {}

    for linha in dados:
        valor_celula = linha[coluna]
        if dados_agrupados.get(linha[coluna]) == None:
            dados_agrupados[valor_celula] = []
        dados_agrupados[valor_celula].append(linha)

    for chave, lista in dados_agrupados.items():
        somatorio = 0
        for registro in lista:
            somatorio += registro[coluna2]
        dados_agrupados[chave]

    return dados_agrupados

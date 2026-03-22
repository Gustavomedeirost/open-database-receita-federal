import csv
import pandas as pd
import math

arquivo = r"[copy path]" # Altere com o caminho do arquivo!

colunas = [
    "cnpj_basico", 
    "ordem",
    "dv",
    "identificador_matriz_filial",
    "nome_fantasia",
    "situacao_cadastral",
    "data_situacao_cadastral",
    "motivo_situacao_cadastral",
    "nome_cidade_exterior",
    "pais",
    "data_inicio_atividade",
    "cnae_fiscal_principal",
    "cnae_fiscal_secundaria",
    "tipo_logradouro",
    "logradouro",
    "numero",
    "complemento",
    "bairro",
    "cep",
    "uf",
    "municipio",
    "ddd_1",
    "telefone_1",
    "ddd_2",
    "telefone_2",
    "ddd_fax",
    "fax",
    "email",
    "qualificacao_responsavel",
    "capital_social",
    "porte_empresa"
]

colunas_chave = [
    "cnpj_basico",
    "ordem",
    "dv",
    "identificador_matriz_filial",
    "nome_fantasia",
    "situacao_cadastral",
    "cnae_fiscal_principal",
    "logradouro",
    "uf",
    "email"
]

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

chunksize = 1000
resultado = []

for chunk in pd.read_csv(
    arquivo,
    sep=';',
    header=None,
    names=colunas,
    encoding='latin1',
    chunksize=chunksize,
    on_bad_lines='skip',
    low_memory=False,
    quotechar='"',
    quoting=1
):
    resultado.append(chunk[colunas_chave])

df_final = pd.concat(resultado)

# Limite de linhas por arquivo
limite = 500_000
total_linhas = len(df_final)
num_arquivos = math.ceil(total_linhas / limite)

for i in range(num_arquivos):
    inicio = i * limite
    fim = min((i + 1) * limite, total_linhas)
    df_final.iloc[inicio:fim].to_csv(f'estabelecimento - pt{i+1}.csv', index=False, encoding='utf-8')
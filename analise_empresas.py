import pandas as pd

arquivo = r"[copy path]" # Altere com o caminho do arquivo!

colunas_empresa = [
    "cnpj_basico",
    "razao_social",
    "natureza_juridica",
    "qualificacao_responsavel",
    "capital_social",
    "porte_empresa",
    "entidade_federativa"
]
colunas_chave_empresa = [
    "cnpj_basico",
    "razao_social",  
    "natureza_juridica",
    "qualificacao_responsavel",
    "porte_empresa"
]

chunksize = 1000
resultado_empresa = []

for chunk in pd.read_csv(
    arquivo,
    sep=';',
    header=None,
    names=colunas_empresa,
    dtype={'cnpj_basico': str},
    encoding='cp1252',
    chunksize=chunksize,
    low_memory=False,
    quotechar='"',
    quoting=1,
    on_bad_lines='skip'
):
    filtro = chunk.dropna(subset=colunas_chave_empresa)
    for col in colunas_chave_empresa:
        filtro = filtro[filtro[col].astype(str).str.strip() != ""]
    resultado_empresa.append(filtro[colunas_chave_empresa])
df_final_empresa = pd.concat(resultado_empresa)

# Remover aspas duplas de todas as colunas
for col in df_final_empresa.columns:
    if df_final_empresa[col].dtype == 'object':
        df_final_empresa[col] = df_final_empresa[col].astype(str).str.replace('"', '', regex=False)

df_final_empresa.to_csv('saida_empresas.csv', index=False, encoding='utf-8')

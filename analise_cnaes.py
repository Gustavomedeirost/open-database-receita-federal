import pandas as pd

arquivo = r"[copy path]" # Altere com o caminho do arquivo!

colunas_cnae = [
    "cnae_fiscal",
    "descricao"
]

colinas_chave_cnae = [
    "cnae_fiscal",
    "descricao"
]
chunksize = 1000
resultado_cnae = []

for chunk in pd.read_csv(
    arquivo,
    sep=';',
    header=None,
    names=colunas_cnae,
    encoding='cp1252',
    chunksize=chunksize,
    low_memory=False
):
    filtro = chunk.dropna(subset=colinas_chave_cnae)
    for col in colinas_chave_cnae:
        filtro = filtro[filtro[col].astype(str).str.strip() != ""]
    resultado_cnae.append(filtro[colinas_chave_cnae])
df_final = pd.concat(resultado_cnae)
df_final.to_csv('saida_cnaes.csv', index=False, encoding='utf-8')
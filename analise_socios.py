import pandas as pd

arquivo = r"[copy path]" # Altere com o caminho do arquivo!

colunas_socio = [
    "cnpj_basico",
    "identificador_de_socio",
    "nome_do_socio",
    "cpf_cnpj_do_socio",
    "qualificacao_do_socio",
    "data_de_entrada_sociedade",
    "pais",
    "representante_legal",
    "nome_do_representante",
    "qualificacao_do_representante_legal",
    "faixa_etaria"
]

colunas_chave_socio = [
    "cnpj_basico",
    "identificador_de_socio",
    "qualificacao_do_socio",
    "nome_do_socio"
]

chunksize = 1000
resultado_socio = []

for chunk in pd.read_csv(
    arquivo,
    sep=';',
    header=None,
    names=colunas_socio,
    encoding='cp1252',
    chunksize=chunksize,
    low_memory=False
):
    filtro = chunk.dropna(subset=colunas_chave_socio)
    for col in colunas_chave_socio:
        filtro = filtro[filtro[col].astype(str).str.strip() != ""]
    resultado_socio.append(filtro[colunas_chave_socio])

df_final = pd.concat(resultado_socio)

df_final.to_csv('saida_socios.csv', index=False, encoding='utf-8')
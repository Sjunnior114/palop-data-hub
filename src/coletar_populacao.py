import requests
import pandas as pd

paises = {
    "AGO": "Angola",
    "CPV": "Cabo Verde",
    "GNB": "Guiné-Bissau",
    "MOZ": "Moçambique",
    "STP": "São Tomé e Príncipe"
}

dados = []

for codigo, nome in paises.items():

    url = (
        f"https://api.worldbank.org/v2/country/"
        f"{codigo}/indicator/SP.POP.TOTL"
        f"?format=json&per_page=100"
    )

    resposta = requests.get(url)
    resultado = resposta.json()

    registros = resultado[1]

    for registro in registros:

        if registro["value"] is not None:

            dados.append({
                "pais": nome,
                "codigo": codigo,
                "ano": int(registro["date"]),
                "populacao": int(registro["value"])
            })

df = pd.DataFrame(dados)

df = df.sort_values(
    ["pais", "ano"]
)

df.to_csv(
    "data/populacao_historica.csv",
    index=False
)

print("Dados coletados com sucesso!")

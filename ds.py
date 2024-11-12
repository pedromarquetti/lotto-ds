import pandas as pd
import matplotlib.pyplot as plt
import requests as req

URL = "https://redeloteria.com.br"

PATH = "/resultados/fc_imprime_relatorios.php?jogo=MegaSena&ordem_sorteio=nao&_=1702507555928"

get = req.get(
    URL+PATH,
    headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0"
    }
)

df = pd.DataFrame(get.json()["data"], columns=[
    "Conc", "Data", "n1", "n2", "n3", "n4", "n5", "n6", "Gan.", "Prêmio","Número de apostas"
])
nums = ["Conc",	"n1", "n2", "n3", "n4", "n5", "n6", "Gan."]
df[nums] = df[nums].apply(
    pd.to_numeric, errors="coerce", axis=1, downcast="integer")


def all_results(res: int):
    # "results" column
    total = df.iloc[:, 1:8]
    figure, ax = plt.subplots(2, 1)

    x_ultimos = df.iloc[:res, 1: 8]

    x_ultimos.plot.box(
        ax=ax[0],
        title=f"Últimos {res} resultados",
        ylabel="Números sorteados (0-60)",
        grid=True,
    )

    # Todos os resultados
    total.plot.box(
        ax=ax[1],
        title="Todos os resultados",
        ylabel="Números sorteados (0-60)",
        grid=True,
    )


def virada(res: int):
    # Initialise the subplot function using number of rows and columns
    figure, ax = plt.subplots(2, 1)

    # Resultados da virada
    virada = df[df["Data"].str.match("31/12")].iloc[:, 1:8]

    x_ultimos = virada.iloc[:res, 1:8]
    x_ultimos.plot.box(
        ax=ax[1],
        grid=True,
        title=f"Últimos {res} Resultados Mega da Virada",
        ylabel="Números sorteados (0-60)",

    )

    virada.plot.box(
        ax=ax[0],
        grid=True,
        title="Resultados Mega da Virada",
        ylabel="Números sorteados (0-60)",

    )


def plot_graphs():

    all_results(5)
    virada(5)

    plt.show()


if __name__ == '__main__':
    plot_graphs()
    print(f"Dados são do site {URL}")


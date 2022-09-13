
from statistics import fmean
from turtle import title
import pandas as pd
import matplotlib.pyplot as plt
import requests as req

URL = "https://redeloteria.com.br/rotinas_01/arquivos_txt/tx_megasena_todos_resultados.txt"
get = req.get(
    URL
)
df = pd.DataFrame(get.json()["data"], columns=[
    "Conc", "Data",	"n1", "n2", "n3", "n4", "n5", "n6", "Gan.", "Prêmio"
])
nums = ["Conc",	"n1", "n2", "n3", "n4", "n5", "n6", "Gan."]
df[nums] = df[nums].apply(
    pd.to_numeric, errors="coerce", axis=1, downcast="integer")


def plot_graphs():

    # "results" column
    total = df.iloc[:, 1:8]

    # Initialise the subplot function using number of rows and columns
    figure, ax = plt.subplots(2, 1)

    # Todos os resultados
    todos_os_resultados = total.plot.box(
        ax=ax[0],
        title="Todos os resultados",
        ylabel="Números sorteados (0-60)",
        grid=True,

    )

    # Resultados da virada
    virada = df[df["Data"].str.match("31/12")]

    resultados = virada.iloc[:, 1:8]

    resultados_da_virada = resultados.plot.box(
        ax=ax[1],
        grid=True,
        title="Resultados Mega da Virada",
        ylabel="Números sorteados (0-60)",

    )
    figure.suptitle("titulo")
    # plt.savefig("results")
    plt.show()


if __name__ == '__main__':
    plot_graphs()

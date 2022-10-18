import matplotlib.pyplot as plt
import pandas as pd

dados=pd.read_csv("populacao_brasileira.csv")

x=dados["ano"].to_list()
y=dados["population"].to_list()



plt.bar(x,y,color="#D8D8D8")
plt.plot(x,y,color="k",linestyle="--")
plt.title("Crescimento da População Brasileira 1980-2016")
plt.xlabel("Ano")
plt.ylabel("População x100.000.000")
plt.show()

import funciones

printLista(data,"Lista de tickers a elegir:")

tickers = getTickers(2,data)
print(tickers)

ticker1 = getArchivo(data,tickers[0])
ticker2 = getArchivo(data,tickers[1])

print(ticker1)
print(ticker2)

ticker1 = diff(ticker1)
ticker2 = diff(ticker2)

print(ticker1)
print(ticker2)
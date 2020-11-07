def getTicker(n):
    
    tickers = []
    cont = 0
    while cont <= n:
        ticker = input("Ingrese el ticker #" +str(cont+1)+"a comparar:")
        tickers.append(ticker)
        cont +=1
    return tickers

tickers = getTicker(2)

print(tickers)
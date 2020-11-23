import os
import pandas as pd
import requests
import matplotlib.pyplot as plt

### Set up
#Data de archivos     
data ={
    "AAPL":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/AAPL.csv",
    "AIG":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/AIG.csv",
    "AMZN":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/AMZN.csv",
    "AXP":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/AXP.csv",
    "BA":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/BAC.csv",
    "CAJ":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CAJ.csv",
    "CAT":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CAT.csv",
    "CL":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CL.csv",
    "CMCSA":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CMCSA.csv",
    "COP":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/COP.csv",
    "CSCO":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CSCO.csv",
    "CVC":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CVC.csv",
    "CVS":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CVS.csv",
    "CVX":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/CVX.csv",
    "DD":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/DD.csv",
    "DELL":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/DELL.csv",
    "F":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/F.csv",
    "GD":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/GD.csv",
    "GE":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/GE.csv",
    "GS":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/GS.csv",
    "GSK":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/GSK.csv",
    "HD":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/HD.csv",
    "HMC":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/HMC.csv",
    "HPQ":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/HPQ.csv",
    "IBM":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/IBM.csv",
    "JPM":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/JPM.csv",
    "K":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/K.csv",
    "KMB":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/KMB.csv",
    "KO":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/KO.csv",
    "MAR":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/MAR.csv",
    "MCD":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/MCD.csv",
    "MMM":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/MMM.csv",
    "MSFT":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/MSFT.csv",
    "NAV":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/NAV.csv",
    "NOC":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/NOC.csv",
    "NVS":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/NVS.csv",
    "PEP":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/PEP.csv",
    "PFE":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/PFE.csv",
    "PG":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/PG.csv",
    "R":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/R.csv",
    "RTN":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/RTN.csv",
    "SAP":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/SAP.csv",
    "SNE":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/SNE.csv",
    "SNY":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/SNY.csv",
    "TM":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/TM.csv",
    "TOT":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/TOT.csv",
    "TWX":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/TWX.csv",
    "TXN":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/TXN.csv",
    "UN":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/UN.csv",
    "VLO":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/VLO.csv",
    "WFC":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/WFC.csv",
    "WMT":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/WMT.csv",
    "XOM":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/XOM.csv",
    "XRX":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/XRX.csv",
    "YHOO":"https://raw.githubusercontent.com/scikit-learn/examples-data/master/financial-data/YHOO.csv"
}      

# Manipuladores de archivos
def wget(url):
    #Función para importar archivos al entorno
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

def getArchivo(data,txtTicker):
    nombreArchivo = txtTicker+ ".csv"
    if not os.path.exists( nombreArchivo ):
        url = data[txtTicker]
        wget(url)
        
    df = pd.read_csv(nombreArchivo)
    return df
    
#Muestra los Tickers posibles
def printLista(data,txt):
    print(txt +"\n")
    for ticker in data:
        print(ticker, end=" - ")
    print("\n")

# De entre toda la lista, selecciona los 2 a comparar y prepara todos los archivos para su análisis
def getTickers(n,data):
    #Genera una lista con la cantidad de tickers a analizar
    tickers = []
    cont = 1
    while cont <= n:
        ticker = input("Ingrese el ticker #" +str(cont)+" a comparar:").upper()
        while ticker not in data:
            ticker = input("ERROR, Ticker no disponible, reingrese el ticker #" + str(cont) +" a comparar:").upper()
        tickers.append(ticker)
        cont +=1
    return tickers

### Anáisis de los datos

#Derivadas discretas
def diff(df):
    df["aux"] = df["close"].shift(1)
    df["aux"] = df["aux"].fillna(0)
    df["diff"] = df["close"] - df["aux"]
    df.pop("aux")
    df["diff"][0]=0
    return df

# Grafico
def grafico(ticker1,ticker2):
    
    print('Fechas disponibles:\n    desde ' + str(ticker1['date'][0]) + '\n    hasta ' + str(ticker1['date'].iloc[-1]))
    fechamin = pd.to_datetime(input('Ingrese fecha desde la que desea ver el grafico (AAAA-MM-DD): '))
    fechamax = pd.to_datetime(input('Ingrese fecha hasta la que desea ver el grafico (AAAA-MM-DD): '))
    
    
    ticker1_acotado = ticker1.loc[(ticker1["date"] > fechamin) & (ticker1["date"] < fechamax), :]
    ticker2_acotado = ticker2.loc[(ticker1["date"] > fechamin) & (ticker2["date"] < fechamax), :]
    
    plt.plot(ticker1_acotado["date"],ticker1_acotado["diff"])
    plt.plot(ticker2_acotado["date"],ticker2_acotado["diff"])
    
    
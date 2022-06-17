import pandas as pd
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from funciones import succes_score

while True:
    start=time.time()
    options = Options()
    options.add_argument("--user-data-dir=C:/Users/jeanp/Desktop/user_data")
    options.page_load_strategy = 'normal'
    driver = webdriver.Chrome(options=options)
    driver.get("https://es.tradingview.com/chart/oqNt16pt/")

    actions=webdriver.ActionChains(driver)
    time.sleep(3)
    menuBTN=driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/div')
    actions.move_to_element(menuBTN).click().perform()
    time.sleep(1)
    csv_option=driver.find_element(By.XPATH,'/html/body/div[5]/div/span/div[1]/div/div/div[5]')
    actions.move_to_element(csv_option).click().perform()
    time.sleep(2)
    download_btn=driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div[1]/div/div[3]/div/span/button')
    actions.move_to_element(download_btn).click().perform()
    time.sleep(4)
    #required params in oder to perform calculation
    #ADX,RSI,RSI-BASED-MA,MACD,IMI,SIGNAL,PLOT_AL,close
    #plotal
    
    df=pd.read_csv('C:/Users/jeanp/Desktop/Trading view/data/SKILLING_NASDAQ, 1.csv',usecols=['MACD','IMI','ADX','RSI','RSI-based MA','Signal','close','Plot.11','Plot.1','Shapes','Plot.2','Plot.4','Plot.8','Shapes.10','Plot.10','Histogram']).iloc[-1]
    #df=df.iloc[-1]
    CLOSE=df['close']
    IMI=df['IMI']
    MACD=df['MACD']
    SIGNAL=df['Signal']
    RSI=df['RSI']
    RSI_B_MA=df['RSI-based MA']
    SQZMOM=df['Plot.11']
    ADX=df['ADX']
    HISTOGRAM=df['Histogram']
    fibo_info={
        '0':df['Plot.1'],
        '1':df['Shapes'],
    }
    #columna h y g
    #info to extract plot.1,shapes,plot.2,plot.4,plot.8,shapes.10,plot.10
    os.remove('C:/Users/jeanp/Desktop/Trading view/data/SKILLING_NASDAQ, 1.csv')
    vector=[RSI,IMI,SQZMOM,ADX,HISTOGRAM,SIGNAL,RSI_B_MA,MACD,fibo_info['1'],fibo_info['0'],CLOSE]
    score=succes_score(vector)
    driver.close()
    print(f'El porcentaje de éxito es {score}%')
    print(f'Waiting for next analysis')
    end=time.time()
    print(end-start)

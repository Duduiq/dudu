from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import telebot
import time

driver = webdriver.Chrome()

driver.get('https://www.playpix.com/pb/live-casino/home/-1/All?openGames=40003094-real&gameNames=Roulette%20A')

janela = driver.window_handles[0]

#Variaveis do Telegram##########################################################################
TOKEN = '6648270789:AAGaS2qH4aRRCYT3hBFY73nAOad8ikfgRSg'

chat_id = '-1002107038990'

bot = telebot.TeleBot(token=TOKEN)

bot.send_message(chat_id=chat_id, text='🤖 ROBÔ-ROLETA-A-ANALISANDO...')

#AGURDANDO OS DADOS APARECEREM###################################################################################################

while len(driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')) == 0:
    time.sleep(2)                         
    
iframe1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')
                                            
driver.switch_to.frame(iframe1)

while len(driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div/iframe')) == 0:
    time.sleep(2)
    
iframe2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/iframe') 
                                            

driver.switch_to.frame(iframe2)

while len(driver.find_elements(By.XPATH, '/html/body/div/div/div[1]/div[9]/div[1]/div')) == 0:
    time.sleep(2)
    
#Variaveis Gerais################################################################################

resultado = None 

check_resultado = None 

coluna = None

duzia = None 

rodadas = 0

#Variaveis de Estrategia##################################################################################

entrada_co = True 
green_co = False 
gale1_co = False 
gale2_co = False 
red_co = False 

entrada_du = True 
green_du = False 
gale1_du = False 
gale2_du = False 
red_du = False 

####################################################################################
def conlunas(i):
    
    global coluna
    
    coluna = []
    
    for x in i:
        
        if int(x) in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
            coluna.append('CO3')
            
        elif int(x) in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
            coluna.append('CO2')
            
        elif int(x) in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
            coluna.append('CO1')
            
        elif int(x) == 0:
            coluna.append('ZERO_CO')
    
    print(f'COLUNAS: {coluna}')
    return coluna 


########################################################################################
def duzias(i):
    
    global duzia 
    
    duzia = []
    
    for x in i:
    
        if int(x) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            duzia.append('D1')
            
        elif int(x) in [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
            duzia.append('D2')
            
        elif int(x) in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
            duzia.append('D3')
            
            
        elif int(x) == 0:
            duzia.append('ZERO_DU')
            
    print(f'DUZIAS: {duzia}')
        
    return duzia

########################################################################################

def estrategia_coluna(co):
    
    global entrada_co   
    global entrada_du
    global green_co
    global gale1_co
    global gale2_co
    global red_co

#COLUNA 1######################################################################################

    if co[0:2] == ['CO1', 'CO1'] and entrada_co == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA COLUNAS 2 e 3')
        
        entrada_co = False 
        entrada_du = False 
        green_co = True
        gale1_co = True
        
        return 
        
        
        
    elif co[0:3] == ['CO2', 'CO1', 'CO1'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        
        return
        
        
    elif co[0:3] == ['CO3', 'CO1', 'CO1'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        
        return
    
    
         
    elif co[0:3] == ['ZERO_CO', 'CO1', 'CO1'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_co = True 
        entrada_du = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        
        return
        
        
        
    elif co[0:3] == ['CO1', 'CO1', 'CO1'] and gale1_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_co = False 
        gale2_co = True
        
        return 
    
    elif co[0:3] == ['CO1', 'CO1', 'CO1'] and gale2_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_co = False 
        red_co = True
        
        return 
    
    elif co[0:3] == ['CO1', 'CO1', 'CO1'] and red_co == True:
        
        bot.send_message(chat_id=chat_id, text='RED')
        
        
        red_co = False 
        green_co = False 
        entrada_co = True 
        entrada_du = True

        
        return 
   
#COLUNA 2######################################################################################


    elif co[0:2] == ['CO2', 'CO2'] and entrada_co == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA COLUNAS 1 e 3')
        
        
        entrada_co = False 
        entrada_du = False 
        green_co = True
        gale1_co = True
        
        return 
        
        
        
    elif co[0:3] == ['CO1','CO2', 'CO2'] and green_co == True:
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        
        return
        
        
    elif co[0:3] == ['CO3','CO2', 'CO2'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        
        return
    
    elif co[0:3] == ['ZERO_CO', 'CO2', 'CO2'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_co = True 
        entrada_du = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        
        return
        
        
    elif co[0:3] == ['CO2','CO2', 'CO2'] and gale1_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_co = False 
        gale2_co = True
        
        return 
    
    elif co[0:3] == ['CO2','CO2', 'CO2'] and gale2_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_co = False 
        red_co = True
        
        return 
    
    elif co[0:3] == ['CO2','CO2', 'CO2'] and red_co == True:
        
        bot.send_message(chat_id=chat_id, text='RED')        
        
        red_co = False 
        green_co = False 
        entrada_co = True 
        entrada_du = True

        
        return 
    
#COLUNA 3################################################################################

    elif co[0:2] == ['CO3', 'CO3'] and entrada_co == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA COLUNAS 1 e 2')
        
        entrada_co = False 
        entrada_du = False 
        green_co = True
        gale1_co = True
        
        return 
        
        
        
    elif co[0:3] == ['CO1','CO3', 'CO3'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        
        return
        
        
    elif co[0:3] == ['CO2','CO3', 'CO3'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_co = True 
        entrada_du = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        
        return
    
    elif co[0:3] == ['ZERO_CO', 'CO3', 'CO3'] and green_co == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_co = True 
        entrada_du = True
        green_co = False 
        gale1_co = False 
        gale2_co = False 
        red_co = False 
        
        return
        
        
    elif co[0:3] == ['CO3','CO3', 'CO3'] and gale1_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_co = False 
        gale2_co = True
        
        return 
    
    elif co[0:3] == ['CO3','CO3', 'CO3'] and gale2_co == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_co = False 
        red_co = True
        
        return 
    
    elif co[0:3] == ['CO3','CO3', 'CO3'] and red_co == True:
        
        bot.send_message(chat_id=chat_id, text='RED')        
        
        red_co = False 
        green_co = False 
        entrada_co = True 
        entrada_du = True

        
        return 

def estrategia_duzia(du):
    
    global entrada_du
    global entrada_co
    global green_du
    global gale1_du
    global gale2_du
    global red_du
    
#DUZIA 1######################################################################################
    
    if du[0:2] == ['D1', 'D1'] and entrada_du == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA DUZIAS 2 e 3')
        
        entrada_du = False 
        entrada_co = False
        green_du = True
        gale1_du = True
        
        return 
        
        
        
    elif du[0:3] == ['D2', 'D1', 'D1'] and green_du == True:
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        
        return
        
        
    elif du[0:3] == ['D3', 'D1', 'D1'] and green_du == True:
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        
        return
        
    elif du[0:3] == ['ZERO_DU', 'D1', 'D1'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_du = True 
        entrada_co = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        
        return
        
        
    elif du[0:3] == ['D1', 'D1', 'D1'] and gale1_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_du = False 
        gale2_du = True
        
        return 
    
    elif du[0:3] == ['D1', 'D1', 'D1'] and gale2_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_du = False 
        red_du = True
        
        return 
    
    elif du[0:3] == ['D1', 'D1', 'D1'] and red_du == True:
        
        bot.send_message(chat_id=chat_id, text='RED')
        
        
        red_du = False 
        green_du = False 
        entrada_du = True 
        entrada_co = True
        
        return 
    
#DUZIA 2######################################################################################
    
    elif du[0:2] == ['D2', 'D2'] and entrada_du == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA DUZIAS 1 e 3')
        
        entrada_du = False 
        entrada_co = False
        green_du = True
        gale1_du = True
        
        return 
        
        
        
    elif du[0:3] == ['D1', 'D2', 'D2'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        
        return
        
        
    elif du[0:3] == ['D3', 'D2', 'D2'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        
        return
    
    elif du[0:3] == ['ZERO_DU', 'D2', 'D2'] and green_du == True:
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_du = True 
        entrada_co = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        
        return
        
        
    elif du[0:3] == ['D2', 'D2', 'D2'] and gale1_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_du = False 
        gale2_du = True
        
        return 
    
    elif du[0:3] == ['D2', 'D2', 'D2'] and gale2_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_du = False 
        red_du = True
        
        return 
    
    elif du[0:3] == ['D2', 'D2', 'D2'] and red_du == True:
        
        bot.send_message(chat_id=chat_id, text='RED')       
        
        red_du = False 
        green_du = False 
        entrada_du = True 
        entrada_co = True
        
        return 
   
#DUZIA 3######################################################################################
    
    elif du[0:2] == ['D3', 'D3'] and entrada_du == True:
        
        bot.send_message(chat_id=chat_id, text='ENTRADA DUZIAS 1 e 2')
        
        entrada_du = False 
        entrada_co = False 
        green_du = True
        gale1_du = True
        
        return 
        
        
        
    elif du[0:3] == ['D1', 'D3', 'D3'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        
        return
        
        
    elif du[0:3] == ['D2', 'D3', 'D3'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN')
        
        entrada_du = True 
        entrada_co = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        
        return
        
    elif du[0:3] == ['ZERO_DU', 'D3', 'D3'] and green_du == True:
        
        bot.send_message(chat_id=chat_id, text='GREEN NO ZERO')
        
        entrada_du = True 
        entrada_co = True
        green_du = False 
        gale1_du = False 
        gale2_du = False 
        red_du = False 
        
        return
        
    elif du[0:3] == ['D3', 'D3', 'D3'] and gale1_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 1')
        
        
        gale1_du = False 
        gale2_du = True
        
        return 
    
    elif du[0:3] == ['D3', 'D3', 'D3'] and gale2_du == True:
        
        bot.send_message(chat_id=chat_id, text='GALE 2')
        
        
        gale2_du = False 
        red_du = True
        
        return 
    
    elif du[0:3] == ['D3', 'D3', 'D3'] and red_du == True:
        
        bot.send_message(chat_id=chat_id, text='RED')       
        
        red_du = False 
        green_du = False 
        entrada_du = True 
        entrada_co = True
        
        return 


########################################################################################

def resolvendo_problema():
    
    
    driver.switch_to.window(janela)

    while len(driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')) == 0:
        time.sleep(2)                         
        
    iframe1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')
                                             
    driver.switch_to.frame(iframe1)
       
    try:
            
        iframe2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/iframe')
        
        if iframe2.is_displayed():
            driver.switch_to.frame(iframe2)    
    
    except NoSuchElementException:
        pass           
    
    
    try:
        
        buttonn = driver.find_element(
    By.XPATH, '/html/body/div/div[2]/div/div[2]/button')
        if buttonn.is_displayed():
            buttonn.click()
            print('Resolvendo o Poblema de Inatividade na Roleta!')       
            
    
    except NoSuchElementException:
        pass
        
########################################################################################   
    
    
def extracao():
    
    global resultado 
    
    resultado = []
    
    driver.switch_to.window(janela)

    # while len(driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')) == 0:
    #     time.sleep(2)                         
        
    iframe1 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[1]/div/iframe')
                                             
    driver.switch_to.frame(iframe1)

    # while len(driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div/iframe')) == 0:
    #     time.sleep(2)
        
    iframe2 = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/iframe') 
                                             

    driver.switch_to.frame(iframe2)

    # while len(driver.find_elements(By.XPATH, '/html/body/div/div/div[1]/div[9]/div[1]/div')) == 0:
    #     time.sleep(2)
        
    resultado = driver.find_element(By.XPATH, '/html/body/div/div/div[1]/div[9]/div[1]/div').text.split()

        
    return resultado 



while True:
    
    try:
        
        resolvendo_problema()
        
        extracao()
        
        if resultado != check_resultado:
            check_resultado = resultado
            
            conlunas(resultado)
            
            duzias(resultado)       
                    
            print(resultado)
            
            rodadas+=1 
            
            if rodadas >= 2:        
                estrategia_coluna(coluna)
                estrategia_duzia(duzia)
            
    except:
        
        print('VOLTANDO À PÁGINA DA ROLETA...')
        
        driver.get('https://www.playpix.com/pb/live-casino/home/-1/All?openGames=40003094-real&gameNames=Roulette%20A')
        
        time.sleep(10)

        
        

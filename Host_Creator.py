from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
from colorama import Fore
import pyautogui

mails = ['mail.com','protonmail.com','gmail.com','email.com','tutanota.de','yahoo.com','yandex.com','icloud.com']

banner = """

 $$$$$$\            $$\                           $$\      $$\           $$\       
$$  __$$\           $$ |                          $$ | $\  $$ |          $$ |      
$$ /  \__|$$\   $$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$ |$$$\ $$ | $$$$$$\  $$$$$$$\  
$$ |      $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$ $$ $$\$$ |$$  __$$\ $$  __$$\ 
$$ |      $$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|$$$$  _$$$$ |$$$$$$$$ |$$ |  $$ |
$$ |  $$\ $$ |  $$ |$$ |  $$ |$$   ____|$$ |      $$$  / \$$$ |$$   ____|$$ |  $$ |
\$$$$$$  |\$$$$$$$ |$$$$$$$  |\$$$$$$$\ $$ |      $$  /   \$$ |\$$$$$$$\ $$$$$$$  |
 \______/  \____$$ |\_______/  \_______|\__|      \__/     \__| \_______|\_______/ 
          $$\   $$ |                                                               
          \$$$$$$  |                                                               
           \______/                                                                
                        By @palomita222 & @Panda.xyz                                                                                                                                                                          
                                                                                                                
"""
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.LIGHTMAGENTA_EX+banner)

# mail_result = (names.get_first_name()+"@"+random.choice(mails))
# print(Fore.LIGHTGREEN_EX+"[New Mail]"+Fore.BLACK+" : "+Fore.LIGHTYELLOW_EX+mail_result)
#https://www.freewebhostingarea.com/

email = input(Fore.LIGHTBLUE_EX+"[MAIL] Escribe tu email > ")
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.LIGHTYELLOW_EX+banner)
password = input(Fore.LIGHTBLUE_EX+"[PASS] Escribe la contraseña del servidor (Min 6 caracteres) > ")
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.LIGHTCYAN_EX+banner)
url = input(Fore.LIGHTBLUE_EX+"[URL] Escribe el nombre de la página web(no espacios ni caracteres especiales) > ")
os.system('cls' if os.name == 'nt' else 'clear')

driver = webdriver.Chrome()
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get("https://www.freewebhostingarea.com/")
sleep(3)
URL = driver.find_element_by_name("thirdLevelDomain")
URL.click()
URL.send_keys(url)
URL2 = driver.find_element_by_xpath("//select[@name='domain']")
URL2.click()
os.system('cls' if os.name == 'nt' else 'clear')
URL3 = driver.find_element_by_xpath("//option[@value='eu5.org']")
URL3.click()
os.system('cls' if os.name == 'nt' else 'clear')
URL4 = driver.find_element_by_xpath("//input[@type='submit']")
URL4.click()
os.system('cls' if os.name == 'nt' else 'clear')
p = driver.current_window_handle
parent = driver.window_handles[0]
chld = driver.window_handles[1]
driver.switch_to.window(chld)
sleep(1)
URL5 = driver.find_element_by_xpath("//input[@name='email']")
URL5.click()
os.system('cls' if os.name == 'nt' else 'clear')
URL5.send_keys(email)
URL5 = driver.find_element_by_xpath("//input[@name='password']")
URL5.click()
os.system('cls' if os.name == 'nt' else 'clear')
URL5.send_keys(password)
URL6 = driver.find_element_by_xpath("//input[@name='confirmPassword']")
URL6.click()
os.system('cls' if os.name == 'nt' else 'clear')
URL6.send_keys(password)
URL7 = driver.find_element_by_xpath("//input[@name='agree']")
URL7.click()
os.system('cls' if os.name == 'nt' else 'clear')
URL8 = driver.find_element_by_xpath("//input[@type='submit']")
URL8.click()
os.system('cls' if os.name == 'nt' else 'clear')
sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')
driver.save_screenshot('Info.png')
element=driver.find_element_by_xpath("//*[text()='Your Personal FTP Information']")
element.location_once_scrolled_into_view
driver.save_screenshot('Info2.png')
os.system('cls' if os.name == 'nt' else 'clear')
print("Program finished succesfully! Your server details are .PNG files in this directory.")


from ctypes import cast
from lib2to3.pgen2 import driver
from multiprocessing.connection import wait
from sqlite3 import Time
from timeit import repeat
import unittest
from warnings import catch_warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

class usando_unittest(unittest.TestCase):
    def setUp(self) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("prefs",{
            "profile.default_content_setting_values.notifications":2
        })
        #chrome_options.add_argument("window-size=1500,1200")
        self.driver= webdriver.Chrome(service= ChromeService(ChromeDriverManager().install()) ,chrome_options=chrome_options)
    
    
    
    def test_buscar(self):
        #Variable de busqueda
        Buscar="Mr Beast"
        driver=self.driver
        pause= ActionChains(driver)
        wait = WebDriverWait(driver,60)
        #Abrimos la cancion de WARRIOS
        driver.get("https://www.youtube.com/watch?v=o3W5ngVTtRE")
        #Presionamos espacio para comenzar el video
        pause.send_keys(Keys.SPACE).perform()
        #Abrimos otra ventana
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
    
        driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S537153464%3A1664174840240209&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWoOLLlwB3yPBvEOaF89OAA58hOJsGVzbN9h2B0w8TKJiEzIM0joMggPfXQyc8xe5MO_5MkR")
        elemento= wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@type="email"]')))
        elemento.send_keys("PowtronXD@gmail.com")
        elemento.send_keys(Keys.ENTER)
        elemento= wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@type="password"]')))
        elemento.send_keys("Automatizacion")
        elemento.send_keys(Keys.ENTER)
        time.sleep(1)
        
        #Buscamos el canal que queremos
        Buscar=Buscar.replace(" ", "+")
        driver.get("https://www.youtube.com/results?search_query="+ Buscar + "&sp=EgIQAg%253D%253D")
        #Entramos al canal
        elemento= wait.until(EC.element_to_be_clickable((By.XPATH,'//div[@id="avatar-section"]')))
        elemento= elemento.find_element(By.TAG_NAME,"a")
        elemento.click()
        time.sleep(1)
        #Detenemos la reproduccion
        pause.send_keys(Keys.SPACE).perform() 
        time.sleep(0.5)
        #Seleccionamos el apartado de videos
        elemento= wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="tabsContent"]/tp-yt-paper-tab[2]')))
        elemento.click()
        urlactual= driver.current_url

        for i in range(0,20):
            elemento= wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="items" and @class="style-scope ytd-grid-renderer"]')))
            elemento= elemento.find_elements(By.TAG_NAME,"ytd-grid-video-renderer")
            elemento[i].click()
            elemento = wait.until(EC.visibility_of_element_located((By.TAG_NAME,'video')))
            elemento = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'ytp-play-button')))
            elemento.click()
            time.sleep(2)
            #time.sleep(3)
            #pause.send_keys(Keys.SPACE).perform()
            driver.execute_script("window.scrollTo(0,700)") 
            #Entramos a la caja de texto
            elemento= wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='simple-box']")))
            elemento= elemento.find_element(By.XPATH,"//*[@id='placeholder-area']")
            elemento.click()
            elemento= elemento.find_element(By.XPATH,"//*[@id='contenteditable-root']")
            elemento.send_keys("GOOD" + str(i))
            elemento = wait.until(EC.element_to_be_clickable((By.ID,"submit-button")))
            elemento.click()
            time.sleep(0.5)
            driver.get(urlactual)
            time.sleep(0.5)


        #print("Miramos si estamos pide correo")
        #assert "No se encontro el elemento" not in driver.page_source

    

    def tearDown(self) -> None:
        self.driver.close()

if __name__== "__main__":
    unittest.main()
a
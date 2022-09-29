from logging import exception
from select import select
import unittest
import selenium
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import tkinter as tk
import random
from tkinter import messagebox as MessageBox
from multiprocessing import freeze_support
freeze_support()
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from subprocess import CREATE_NO_WINDOW
import subprocess 
from selenium import webdriver

GMAIL=""
CONTRA=""
COMENTA=[]
YOUTU=""


class usando_unittest(unittest.TestCase):
    #@classmethod
    def setUp(self) -> None:
        self.extras= ["Genial video", "Eres un grande", "Maravilloso","Buen video, ahora toca verlo", "Como siempre buen video" ]
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--profile-directory=Default")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--disable-plugins-discove  ry")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_experimental_option("prefs",{
            "profile.default_content_setting_values.notifications":2
        })
        chromeser= ChromeService(ChromeDriverManager(path = r".\\Drivers").install())
        chromeser.creationflags = CREATE_NO_WINDOW
        vers=106
        for i in range(0,2):
            try:
                self.driver= uc.Chrome(version_main=vers,
                    use_subprocess=True,suppress_welcome=False ,chrome_options=chrome_options)
            except Exception as e :
                mensage=str(e)
                vers=  mensage.find("Current browser version is ") + len("Current browser version is ")
                mensage= mensage[vers:len(mensage)-1]
                vers= mensage.find(".")
                mensage= mensage[0:vers:1]
                vers= int(mensage)
                #self.driver.quit()


                

        self.driver.delete_all_cookies()
        self.driver.execute_script('return navigator.webdriver')
        #webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    def test_buscar(self):
        extras= self.extras
        #Variable de busqueda
        Buscar=YOUTU
        driver=self.driver
        driver.fullscreen_window()
        pause= ActionChains(driver)
        wait = WebDriverWait(driver,10)
        #Abrimos la cancion de WARRIOS
        
        driver.get("https://youtu.be/o3W5ngVTtRE")
        #Presionamos espacio para comenzar el video
        time.sleep(3)
        pause.send_keys(Keys.SPACE).perform()
        #Abrimos otra ventana
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        
        driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S537153464%3A1664174840240209&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWoOLLlwB3yPBvEOaF89OAA58hOJsGVzbN9h2B0w8TKJiEzIM0joMggPfXQyc8xe5MO_5MkR")
        elemento= wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@type="email"]')))
        elemento.send_keys(GMAIL)
        elemento.send_keys(Keys.ENTER)
        elemento= wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@type="password"]')))
        elemento.send_keys(CONTRA)
        elemento.send_keys(Keys.ENTER)
        
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
        for i in range(0,7):
            driver.execute_script("window.scrollTo(0,"+str(i*800)+ ")")
            time.sleep(3)

        elemento= wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="items" and @class="style-scope ytd-grid-renderer"]')))
        elemento = elemento.find_elements(By.TAG_NAME,"ytd-grid-video-renderer")
        
        link_videos=[]
        for i in elemento:
            link= i.find_element(By.TAG_NAME,"a").get_attribute("href")
            link_videos.append(link)

        numero=0
        No=0
        for i in link_videos:
            try:
                driver.get(i)
                elemento = wait.until(EC.visibility_of_element_located((By.TAG_NAME,'video')))
                elemento = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'ytp-play-button')))
                elemento.click()
                time.sleep(2)
                driver.execute_script("window.scrollTo(0,700)") 
                #Entramos a la caja de texto
                elemento= wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='simple-box']")))
                elemento= elemento.find_element(By.XPATH,"//*[@id='placeholder-area']")
                elemento.click()
                elemento= elemento.find_element(By.XPATH,"//*[@id='contenteditable-root']")
                numero+=1
                elemento.send_keys(COMENTA[No] +"\n" + extras[random.randint(0,len(extras)-1)])
                No+=1
                if No>= len(COMENTA):
                    No=0
                elemento = wait.until(EC.element_to_be_clickable((By.ID,"submit-button")))
                elemento.click()
                time.sleep(0.5)
                if numero==20:
                    break
            except:
                pass
        self.numero=numero
         
            

    
    def tearDown(self) -> None:
        self.driver.close()
        MessageBox.showinfo("Hola ", "Se enviaron " + str(self.numero) + " comentarios con exito")
        #driver.switch_to.window(driver.window_handles[0])
        #cls.driver.close()


def Automatizar():
    global GMAIL
    GMAIL=Correo.get()
    global CONTRA
    CONTRA= Clave.get()
    global YOUTU
    YOUTU= Canal.get()
    global COMENTA
    COMENTA= [L_ComenFinal.cget("text"),L_ComenFinal1.cget("text"),L_ComenFinal2.cget("text")]
    
    if GMAIL!="" and CONTRA!="" and YOUTU!="" and COMENTA[0]!="" and COMENTA[1]!="":
        Ventana.destroy()
        unittest.main()
    else:
        MessageBox.showinfo("Error ", "Llena todas las cajas de texto")

def limitador(entry_text,Coment):
    if len(entry_text.get()) >= 0:
        #donde esta el :5 limitas la cantidad d caracteres
        entry_text.set(entry_text.get()[:7])
        Extras=["XD",":3",":D","B)",":V"]
        Coment["text"]= Extras[random.randint(0,len(Extras)-1)]+ " " +  entry_text.get() + " " + Extras[random.randint(0,len(Extras)-1)]
Ventana= tk.Tk()
Ventana.geometry("400x530")
Ventana.title("BotTube")
L_Titulo=tk.Label(Ventana,text="Bienvenido", font=("Arial",15))
L_Titulo.pack()
L_Correo= tk.Label(Ventana,text="Correo")
L_Correo.pack()
Correo= tk.Entry(Ventana)
Correo.pack()
L_Clave= tk.Label(Ventana,text="Contraseña")
L_Clave.pack()
Clave= tk.Entry(Ventana,show="*")
Clave.pack()
Varmenu= tk.StringVar()
L_Nota= tk.Label(Ventana,text="Nota: Es necesario que ingrese su" + 
    " correo y contraseña para realizar el envio masivo\nEste programa "
    + "no guardara dichos datos" ,wraplength=300)
L_Nota.pack()
L_Canal= tk.Label(Ventana,text="Youtuber o canal")
L_Canal.pack()
Canal= tk.Entry(Ventana)
Canal.pack()

L_Comentario= tk.Label(Ventana,text="Comentario 1: ")
L_Comentario.pack()
textComentario= tk.StringVar()
Comentario = tk.Entry(Ventana, textvariable=textComentario)
textComentario.trace("w",lambda *args:limitador(textComentario,L_ComenFinal))
Comentario.pack()
L_ComenFinal= tk.Label(Ventana)
L_ComenFinal.pack()

L_Comentario1= tk.Label(Ventana,text="Comentario 2: ")
L_Comentario1.pack()
textComentario1= tk.StringVar()
Comentario1 = tk.Entry(Ventana, textvariable=textComentario1)
textComentario1.trace("w",lambda *args:limitador(textComentario1,L_ComenFinal1))
Comentario1.pack()
L_ComenFinal1= tk.Label(Ventana)
L_ComenFinal1.pack()

L_Comentario2= tk.Label(Ventana,text="Comentario 3: ")
L_Comentario2.pack()
textComentario2= tk.StringVar()
Comentario2 = tk.Entry(Ventana, textvariable=textComentario2)
textComentario2.trace("w",lambda *args:limitador(textComentario2,L_ComenFinal2))
Comentario2.pack()
L_ComenFinal2= tk.Label(Ventana)
L_ComenFinal2.pack()
Nota= tk.Label(Ventana,text="Nota: Solo se pueden enviar 5 caracteres maximo por comentario\n" +
    "Ademas se agregaran algunos caracteres al comentario , puedes ver lo que se enviara debajo de cada comentario, ademas se le agregara una frase despues" ,wraplength=300)
Nota.pack()
Enviar = tk.Button(Ventana,text="Comenzar envio masivo",command=Automatizar)
Enviar.pack()
Nota2= tk.Label(Ventana,text="Nota: Se enviara 1 comentario a 20 videos")
Ventana.mainloop()

""""" Autor: Ariel Diaz
     https://infrasoft.com.ar/
     Salta Argentina    
     Licence: Creative Commons 
"""""
""" This library uses Selenium"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import time

chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36") # Ejemplo
driver = webdriver.Firefox(options=chrome_options)


def selenium_input(identify="", value="",by="XPATH"):
     try:
        if(by=="XPATH"): 
            input_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, identify))
            )       
            input_element = driver.find_element(By.XPATH, identify)            
        
        if(by=="ID"):
            input_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, identify))
            ) 
            input_element = driver.find_element(By.ID, identify)            
        
        if(by=="NAME"):
            input_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.NAME, identify))
            )
            input_element = driver.find_element(By.NAME, identify)

        if(by=="CLASS"):
            input_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, identify))
            )
            input_element = driver.find_element(By.CLASS_NAME, identify)

        input_element.send_keys(value)
        return True

     except:
        print("Error in "+ identify)
        #input()
        return False

def selenium_Button(identify="",by="XPATH"):
    try:
        if(by=="XPATH"):
            button_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, identify))
            ) 
            button_element = driver.find_element(By.XPATH, identify)
        
        if(by=="ID"):
            button_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, identify))
            )
            button_element = driver.find_element(By.ID, identify)

        if(by=="NAME"):
            button_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.NAME, identify))
            )
            button_element = driver.find_element(By.NAME, identify)
        if(by=="CLASS"):
            button_element = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, identify))
            )
            button_element = driver.find_element(By.CLASS_NAME, identify)
        button_element.click()
        return True
    except:
        print("Error in "+ identify)
        #input()
        return False
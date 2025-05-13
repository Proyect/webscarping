""" 
Autor: Ariel Marcelo Diaz
Tel. +54 9 387 22 04 925
Mail: arieldiaz.sistemas (at) gmail.com
  Argentina Salta
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc

import time
import csv

from dotenv import load_dotenv
import os 

from basic import *

def segurity():
  print("configuracion de seguridad")

def main():
    input_file = "model_file.csv" #os.getenv("INPUT_FILE")
    web  = "https://walmart.com.mx/" #os.getenv("URL")
    output_file = "outfile" #os.getenv("OUTPUT_FILE")
    
    driver = uc.Chrome()
    os.system("cls")
    driver.get(web)
    
    with open(input_file, "r") as f:
      lector = csv.reader(f)
      print("Start getTing data enter")
      time.sleep(4)
      input("Tomar datos")
      segurity()
      
      for element in lector:
        os.system("cls")
        element = element.split(";")
        print(element)
        selenium_input('//*[@id="__next"]/div[1]/span/header/form/div/input',element[1])
        selenium_Button('//*[@id="__next"]/div[1]/span/header/form/div/button[2]')    

if __name__ == "__main__":
    main()
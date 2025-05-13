""" 
Autor: Ariel Marcelo Diaz
Tel. +54 9 387 22 04 925
Mail: arieldiaz.sistemas (at) gmail.com
  Argentina Salta
"""

from selenium import webdriver

import time
import csv

from dotenv import load_dotenv
import os 

def main():
    input_file = os.getenv("INPUT_FILE")
    print(input_file)
    driver = webdriver.Chrome()

if __name__ == "__main__":
    main()
from ast import Return
import logging
import sys
from unittest import result
logging.basicConfig(level=logging.DEBUG)
sum = 0,00

action = float(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:  "))


def checking():

    if action < 5 and  action != 0:
          return True
    
if checking() == True:    
      logging.info("Podaj składnik 1: ")
      first_number = float(input("Podaj pierwszą cyfre "))
      logging.info("Podaj składnik 2: ")
      second_number = float(input("Podaj drugą cyfre "))
else:
    exit()







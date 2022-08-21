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

def plus_function(action):    
    if action == 1:
         sum = first_number + second_number
         logging.debug(f"Mnoże {float(first_number)} i {float(second_number)}")
         logging.info(f"Wynik to {round(sum , 2)}")
plus_function(action)         

def minus_function(action):    
    if action == 2:
       sum = first_number - second_number
       logging.debug(f"Mnoże {float(first_number)} i {float(second_number)}")
       logging.info(f"Wynik to {round(sum, 2)}")
minus_function(action)

def times_function(action):
    if action == 3:
       sum = first_number * second_number
       logging.debug(f"Mnoże {float(first_number)} i {float(second_number)}")
       logging.info(f"Wynik to {round(sum , 2)}")
times_function(action)

def divide_function(action):
    if action == 4:
        sum = first_number / second_number
        logging.debug(f"Dziele {float(first_number)} i {float(second_number)}")
        logging.info(f"Wynik to {round(sum , 2)}")    
divide_function(action)   







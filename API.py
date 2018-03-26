#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

                    ############################################
                    #__author__ = Hugo Monfouga                #
                    # __email__ = "hugo.monfouga@ynov.com"     #
                    # __status__ = "Production"                #  
                    ############################################

import pandas
import requests


coinlist = requests.get('https://www.cryptocompare.com/api/data/coinlist/').json()
data=coinlist['Data']

choix = 0

while choix != 'bye': 
     choix = raw_input("Bonjour. \n Pour afficher la liste des cryptomonnaies, tapez 'liste'. Sinon taper le nom de la criptomonnaire dont vous voulez le prix. \n Pour quitter le programme tapez 'bye'.")
     if(choix == 'liste'):
         
         for datas in data:
             print (datas)

     elif(choix == 'bye'):
         print('bye !')

     else:
         coinlist = requests.get('https://min-api.cryptocompare.com/data/price?fsym='+choix.upper()+'&tsyms=EUR').json()
         prix= str(coinlist['EUR'])
         print ("Votre cryptomonnaircryptomonnaie a une valeur de : "+prix +" €")
     

         
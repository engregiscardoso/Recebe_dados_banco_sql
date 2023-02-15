# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 14:04:14 2023

@author: REGIS CARDOSO
"""


import pandas as pd
import numpy as np
import statistics
import math
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from datetime import timedelta, datetime
from scipy.fftpack import fft, fftfreq
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MaxAbsScaler
import sqlalchemy as sqldb
from datetime import timedelta, datetime
import struct
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle



# Função de conexão
def conexao():
    
    #### Parâmetros de CONEXÃO #####
    server = '10.61.119.27'
    database = 'SIMME_UH_TUCURUI'
    username = 'simme'
    password = 'lacen2015'
    engineString = 'mssql+pyodbc://'+username+':'+password+'@'+server+':1433/'+database+'?driver=ODBC Driver 17 for SQL Server'

    engine = sqldb.create_engine(engineString)
    conectado = engine.connect()
    return conectado



# Função busca
def retorno_onda(conectado, string_consulta):
    resultado = conectado.execute(string_consulta)

    for row in resultado:
        onda = row[0]
    resultado.close
    return onda



#### Parametros de CONSULTA #####
atributo_ref = 'colocar aqui o atributo de filtro'
atributo_retorno = 'colocar aqui o atributo de consulto/retorno'
tabela = 'colocar aqui a tabela'
atributo_consulta = 457

string_consulta = 'SELECT ' + atributo_retorno + ' FROM ' + tabela + ' WHERE ' + atributo_ref+' = ' + str(atributo_consulta)


connection = conexao()  


dado = retorno_onda(connection, string_consulta)

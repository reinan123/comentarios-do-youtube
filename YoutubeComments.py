"""
 -*- coding: utf-8 -*-
Reinan Rodrigues
reinan-rp@hotmail.com
Versão 1.0
"""
import aplicativo
from navegacao import *
from arquivoCsv import *
from tkinter import *
from time import sleep
import os
from datetime import datetime
import googleapiclient.discovery
from tkinter import filedialog
import csv

menuInicial = Tk()
menuInicial.title('Youtube Comments')
menuInicial.geometry(newGeometry="650x200+300+20")

def executar():
    capturarDados()
    salvarCsv()
    sleep(3)
    aplicativo.msg.set('Arquivo Salvo com Sucesso!')


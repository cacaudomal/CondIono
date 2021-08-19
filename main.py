# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 12:19:46 2021

@author: Clara
"""
import dado as d
import dadoiri as iri
import dado_igrf as igrf
import dado_nrlmsise as msise
import freqcol as fc
#import numpy as np

a = d.dado("dadosIGRF.txt")

b = iri.iri("dados_iri.txt")

c = igrf.igrf("dadosIGRF.txt")

d = msise.nrlmsise("dadosNRLMSISE.txt")
#d.ver_dado()

g = fc.fen(d.nN2,d.nO2,d.nO,b.Te)
#print("d.__doc__:",g.__doc___)
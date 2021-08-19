# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:13:32 2021

@author: Clara
"""

from dado import dado
import matplotlib.pyplot as plt

class igrf(dado):
    """
    classe que guarda os dados do modelo igrf. 
    
    ...
    
    Attributes
    ----------
    B : LIST
        magnetic field in nT
    h : LIST
        height of the data in km
        
    Methods
    -------
        graf(self)
            faz gráfico do campo magnetico em nT pela altura em km.
    """
    
    def __init__(self,nomearq):
        """
        Constructor that initiates the variables necessary for taking the data of the igrf model.

        Parameters
        ----------
        nomearq : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        dado.__init__(self,nomearq)
        self.set_var()
        
    def set_var(self):
        self.B = []
        self.h = []
        
        self.separar_vardado()
    
    def separar_vardado(self,numvar=2):
        """
        Pegar variaveis do arquivo do modelo IGRF.

        Parameters
        ----------
        numvar : TYPE, optional
            DESCRIPTION. The default is 2.

        Returns
        -------
        None.

        """    
        c = 0
        
        for i in range(0,len(self.dado),numvar):
            self.h.insert(c,self.dado[i])
            self.B.insert(c,self.dado[i+1]*1e-9) #passando de nT para T
            
            #print("\nc.",c,"h3:",self.h3[c],"B:",self.B[c]," IGRF")
            #print("\n",i,"\n")
            c = c + 1 
        
        #print("get_varIGRF \n tam B:",len(self.B))
        
    def graf(self):
        """
        DESENHA O GRÁFICO DO CAMPO MAGNÉTICO EM nT PELA ALTURA EM km.

        Returns
        -------
        None.

        """
        plt.figure(figsize = (5,5))
        
        plt.plot(self.B,self.h)
        
        plt.xlabel("Campo Magnético (nT)")
        plt.ylabel("Altura (km)")
        
        plt.legend()
        plt.grid()
        
        plt.show()
        
        
        
        
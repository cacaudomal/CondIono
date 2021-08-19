# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 14:07:36 2021

@author: Clara

contém as classes freqcol e fen
"""



import numpy as np

class freqcol():
    """
    Classe base para as frequências de colisão dadas segundo Adachi et al 2017.
    
    ...
    
    SUBCLASSES
    ----------
        fen
        fin1
        fin2
        
    Attributes
    ----------
    nN2 : LIST FLOAT
        densidade de N2, [m^3] NRLMSISE-00
    nO2 : LIST FLOAT
        densidade de O2 [m^3] NRLMSISE-00
    nO : LIST FLOAT
        densidade de O [m^3] NRLMSISE-00    
        
    Methods
    ----------
    
    """
    
    def __init__(self, nN2, nO2, nO):
        self.set_atmNeutra(nN2, nO2, nO)
    
    def set_freq(self):
        pass
    
    def get_freq(self):
        pass
    
    def ver(self):
        pass
    
    def set_atmNeutra(self,nN2,nO2,nO):
        self.nN2 = nN2
        self.nO2 = nO2 #lista com a densidade de O2 [cm^-3] é convertido para [m^-3]
        self.nO  = nO #densidade de O [cm^-3] é convertido para [m^-3]
        
    def calc_freq(self):
        pass
    
#==================================================    
    

class fen(freqcol):
    """
    Classe da frequência de colisão entre elétrons e partículas neutras.
    
    ...
        
    Attributes
    ----------
        nN2 : FLOAT
            densidade de N2, [m^3] NRLMSISE-00
        nO2 : FLOAT
            densidade de O2 [m^3] NRLMSISE-00
        nO : FLOAT
            densidade de O [m^3] NRLMSISE-00

            
    Methods
    ----------
    """
    
    def __init__(self, nN2, nO2, nO,Te):
        super().__init__(nN2, nO2, nO)
        self.set_Te(Te)
        self.set_freq()
    
    def set_freq(self,size):
       self.fen = [0] * size
       #print("fen set_freq len(fen)",len(self.fen),"size",size)
       self.calc_freq()
       
    def get_freq(self):
        return self.fen 
    
    def ver(self):
        print(self.fen)
        
    def set_Te(self,Te):
        self.Te = Te
        #print("set_Te : ",self.Te)
    
    def calc_freq(self):
        """
        Cálculo da frequência de colisão do elétron com as partículas neutras. 
        
        equações retiradas do trabalho de Adachi et. al, (2017).

        Parameters
        ----------
        nN2 : FLOAT
            densidade de N2, [m^3] NRLMSISE-00
        nO2 : FLOAT
            densidade de O2 [m^3] NRLMSISE-00
        nO : FLOAT
            densidade de O [m^3] NRLMSISE-00
        Te : FLOAT
            temperatura dos elétrons [K]
            
        Returns
        -------
        fen : FLOAT
            frequência de colisão do elétron com partículas neutras [Hz].

        """
        for i in range(len(self.Te)):
            self.fen[i] = 2.33e-17 * self.nN2[i] * (1 - 1.21e-4*self.Te[i]) * self.Te[i] + 1.82e-16 * self.nO2[i] * (1 + 3.6e-2*np.sqrt(self.Te[i])) * np.sqrt(self.Te[i]) + 8.9e-17*self.nO[i] * (1 + 5.7e-4*self.Te[i]) * np.sqrt(self.Te[i])



#======================================


class fin1(freqcol):
    """
    Classe da frequência de colisão entre íon ficticio 1 e partículas neutras.
    
    ...
        
    Attributes
    ----------
        nN2 : FLOAT
            densidade de N2, [m^3] NRLMSISE-00
        nO2 : FLOAT
            densidade de O2 [m^3] NRLMSISE-00
        nO : FLOAT
            densidade de O [m^3] NRLMSISE-00
        Te : FLOAT
            temperatura dos elétrons [K]
            
    Methods
    ----------
    """
    def __init__(self, nN2, nO2, nO):
        freqcol.__init__(self, nN2, nO2, nO)
        self.set_freq(len(nN2))
    
    def set_freq(self,size):
       self.fin1 = [0]*size
       self.calc_freq()
    
    def calc_freq(self):
        """
        Cálculo da frequência de colisão dos íon 1 (inventado) com as partículas neutras (Adachi et. al, 2017)
    
        Parameters
        ----------
        nN2 : FLOAT
            densidade de N2, [m^3] 
        nO2 : FLOAT
            densidade de O2 [m^3] 
        nO : FLOAT
            densidade de O [m^3] 
    
        Returns
        -------
    
        fin1 : FLOAT
            frequência de colisão do íon 1 [Hz]
           
        """
        for i in range(len(self.nN2)):
            self.fin1[i] = (4.29*self.nN2[i] + 4.23*self.nO2[i] + 2.41*self.nO[i]) * 1e-16
      
            
      
#=========================================      
        
     
class fin2(freqcol):
    """
    Classe da frequência de colisão entre o íon O+ e partículas neutras.
    
    ...
        
    Attributes
    ----------
    nN2 : FLOAT
        densidade de N2 [m^3]
    nO2 : FLOAT
        densidade de O2 [m^3]
    nO : FLOAT
        densidade de O [m^3]
    Ti : FLOAT
        temperatura dos ions [K]
    Tn : LIST 
        temperatura particulas neutras
            
    Methods
    ----------
    
    """
    
    def __init__(self, nN2, nO2, nO,Ti,Tn):
        freqcol.__init__(self, nN2, nO2, nO)
        self.set_Tr(Ti,Tn)
        self.set_freq(len(nN2))
    
    def set_freq(self,size):
       self.fin2 = [0] * size
       self.calc_freq()
       
    def set_Tr(self,Ti,Tn):
        """
        CRIA A LISTA DOS VALORES DA TEMPERATURA RELATIVA E PREENCHE SEUS VALORES.

        Parameters
        ----------
        Ti : FLOAT
            TEMPERATURA DOS ÍONS.
        Tn : FLOAT
            TEMPERATURA DAS PARTÍCULAS NEUTRAS.

        Returns
        -------
        None.

        """
        self.Tr = [0] * len(Ti)
        
        for i in range(len(Ti)):
            self.Tr[i] = (Ti[i] + Tn[i])/2
    
    def calc_freq(self):
        """
        Cálculo da frequência de colisão dos íon O+ com as partículas neutras. 
        
        Equações retiradas do trabalho de Adachi et. al, 2017.
    
        Parameters
        ----------
        nN2 : FLOAT
            densidade de N2, [m^3] 
        nO2 : FLOAT
            densidade de O2 [m^3] 
        nO : FLOAT
            densidade de O [m^3] 
        Tr : FLOAT
            temperatura  = (Ti + Tn)/2 em [K]
    
        Returns
        -------
    
        fin2 : FLOAT
            frequência de colisão do íon 2 [Hz]

        """
        for i in range(len(self.nN2)):
            self.fin2[i] = 6.82e-16*self.nN2[i] + 6.66e-16*self.nO2[i] + 3.32e-17*self.nO[i]*np.sqrt(self.Tr[i]) * (1.08 - 0.139*np.log10(self.Tr[i]) + 4.51e-3*(np.log10(self.Tr[i])**2))
    
    
    
    
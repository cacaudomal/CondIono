# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 13:47:57 2021

@author: Clara
"""

from dado import dado
import matplotlib.pyplot as plt

class nrlmsise(dado):
    """
    Classe que guarda e manipula os dados do modelo nrlmsise-00. 
    
    ...
    
    Attributes
    ----------
    h : LIST 
        altura em [km]
    nN2 : LIST 
        densidade de N2, [cm^-3] é convertido para [m^-3]
    nO2 : LIST 
        densidade de O2 [cm^-3] é convertido para [m^-3]
    nO  : LIST 
        densidade de O [cm^-3] é convertido para [m^-3]
        
    Methods
    -------
        graf(self)
            desenha gráfico da composição das particulas neutras O,O2 e N2 na atmosfera.
    
    """
    
    def __init__(self,nomearq):
        """        

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
        self.h = [] #altura em [km]
        self.nN2 = [] #densidade de N2, [cm^-3] é convertido para [m^-3]
        self.nO2 = [] #densidade de O2 [cm^-3] é convertido para [m^-3]
        self.nO  = [] #densidade de O [cm^-3] é convertido para [m^-3]
        
        self.separar_vardado()
        
    def separar_vardado(self,numvar=4):
        """
        Pega e separa as variaveis do vetor com os dados do modelo NRLMSISE-00 em listas e converte a unidade de medida de cm3 para m3. 

        Parameters
        ----------
        numvar : TYPE, optional
            DESCRIPTION. The default is 4.

        Returns
        -------
        None.
        """
        c = 0

        for i in range(0,len(self.dado),numvar):
           self.h.insert(c,self.dado[i])
            
           self.nO.insert(c,self.dado[i+1]*1e6)
           self.nN2.insert(c,self.dado[i+2]*1e6) # O produto por 1e6 é para passar de cm^-3 para m^-3
           self.nO2.insert(c,self.dado[i+3]*1e6)
            
           #print(c,self.h2[c],self.nN2[c],self.nO2[c],self.nO[c],"\n gv_MSISE")
           #print("\n",i,"\n")

           c = c + 1     
        
    def graf(self):
        """
        Faz um gráfico da composiçao da atmosfera das partículas neutras nO, nO2 e nN2.
        
        Returns
        -------
        None
        """ 
        plt.figure(figsize=(5,5))
        
        plt.semilogx(self.nO,self.h2,'-', label='O')
        plt.plot(self.nO2,self.h2,'-', label='$O_2$')
        plt.semilogx(self.nN2,self.h2, label='$N_2$')
        
        #plt.title('Perfil da Composição da Atmosfera Neutra')
        plt.xlabel("$log_{10}$ Densidade ($m^{-3}$)")
        plt.ylabel("Altura (km)")
         
        #plt.xlim(left=10e2)
        
        plt.legend()
        plt.grid()
        
        plt.show()
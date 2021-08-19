# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 12:25:18 2021

@author: Clara
"""
from dado import dado
import matplotlib.pyplot as plt

class iri(dado):    
     """
     Classe para receber e manipular dados do modelo IRI.
     
     
     Attributes
     ----------
    h : LIST 
        altura em [km] IRI
    ne : LIST
        Densidade de elétrons [m^-3]
    Tn : LIST 
        temperatura de neutrons [K]
    Ti : LIST 
        temperatura dos íons [K]
    Te : LIST 
        temperatura dos elétrons [K]
    rho_íonO : LIST
        concentração do íon O+ [%]
    rho_íonO2 : LIST
        concentração do íon O2+ [%]
    rho_íonNO : LIST
        concentração do íon NO+ [%]
    rho_íonN : LIST
        concentração do íon N+ [%]
    rhoO2 : LIST
        Densidade numérica do íon O2+
    rhoO : LIST
        Densidade numérica do íon O+
    rhoNO : LIST
        Densidade numérica do íon NO+
    rhoN : LIST
        Densidade numérica do íon 1
         
     Methods
     -------
     
     """
    
     def __init__(self,nomearq):
         dado.__init__(self,nomearq)
         #print("\n\niri __init__: \n",self.dado)
         
         self.set_var()
         self.calc_rhoion()
     
     def set_var(self):
        self.h = [] #altura em [km] IRI
        self.ne = [] #Densidade de elétrons [m^-3]

        self.Tn = [] #temperatura de neutrons [K]
        self.Ti = [] #temperatura dos íons [K]
        self.Te = [] #temperatura dos elétrons [K]

        self.rho_íonO = [] # concentração do íon O+ [%]
        self.rho_íonO2 = [] # concentração do íon O2+ [%]
        self.rho_íonNO = [] # concentração do íon NO+ [%]
        self.rho_íonN = [] # concentração do íon N+ [%]
        
        self.rhoO2 = [] #densidade numérica do íon O2+
        self.rhoO = []  #densidade numérica do íon O+
        self.rhoNO = []  #densidade numérica do íon NO+
        self.rhoN = []  #densidade numérica do íon 1
        
        self.separar_vardado()
     
     def ver_h(self):
         print("\n\nh:\n",self.h)
     
     def separar_vardado(self,numvar=9):
        """
        Função para separar os valores dos parametros dos dados lidos no arquivo do IRI.

        Parameters
        ----------
        numvar : INTEGER, optional
            é o número de parametros lidos no arquivo. The default is 8.

        Returns
        -------
        None.

        """
        c = 0

        #print("separar_vardado : entrou")
        for i in range(0,len(self.dado)-1,numvar):
            self.h.insert(c,self.dado[i])
    
            self.ne.insert(c,self.dado[i+1])
            self.Tn.insert(c,self.dado[i+2])
            self.Ti.insert(c,self.dado[i+3])
            self.Te.insert(c,self.dado[i+4])

            self.rho_íonO.insert(c,self.dado[i+5])
            self.rho_íonO2.insert(c,self.dado[i+6])
            self.rho_íonNO.insert(c,self.dado[i+7])
            self.rho_íonN.insert(c,self.dado[i+8])
            
            #print("c.",c,"h",self.h[c],"ne",f'{self.ne[c]:.4e}',"Tn",self.Tn[c],"Ti",self.Ti[c],"Te",self.Te[c],"rho O+",f'{self.rho_íonO[c]:.2e}',"rho O2+",f'{self.rho_íonO2[c]:.2e}',"rho NO+",f'{self.rho_íonNO[c]:.2e}')
            #print("\n",i,"\n")
            
            c = c + 1
            
     def calc_rho_numion(self,ne,rho_ion):
        """
        Calcula a Densidade numérica do ion a partir da densidade de elétrons.
    
        Parameters
        ----------
        rho_íon : FLOAT
            concentração do íon [%]
        ne : FLOAT
            Densidade de elétrons [elétrons/m^3]
    
        Returns:
        ----------
        rhoi2 : FLOAT
        densidade do íon O+ [m^-3]
        
        """
        rhoion = ne * rho_ion/100 #densidade do íon em [m^-3]
        #print('rhoi2',rhoi2,"m^-3")
    
        return(rhoion)
        
     def calc_rhoion(self):
         """
         função que realiza os cálculos para obter a densidade numérica de ions.

         Returns
         -------
         None.

         """     
         for i in range(len(self.ne)):
            self.rhoO2.insert(i,self.calc_rho_numion(self.ne[i],self.rho_íonO2[i]))
            self.rhoO.insert(i,self.calc_rho_numion(self.ne[i],self.rho_íonO[i]))
            self.rhoNO.insert(i,self.calc_rho_numion(self.ne[i],self.rho_íonNO[i]))
            self.rhoN.insert(i,self.calc_rho_numion(self.ne[i],self.rho_íonN[i]))

     def graf_rhoIon(self):
         """
         DESENHA O GRÁFICO DAS DENSIDADES NUMÉRICAS DOS ÍONS O+, O2+, NO+, N+ EM m3 PELA ALTURA EM km.

         O gráfico está em escala logarítmica;
         Returns
         -------
         None.

         """
         plt.figure(figsize=(5,5))
        
         plt.semilogx(self.rhoO,self.h,label="$O^+$")
         plt.semilogx(self.rhoO2,self.h,label="$O_2^+$")
         plt.plot(self.rhoNO,self.h,"-r",label="$NO^+$")
         plt.plot(self.rhoN,self.h,label="$N^+$")
         plt.plot(self.ne,self.h,"g",label="elétrons")
        
        #plt.plot(self.rho,self.h,label="íon 1")
        
        #plt.title("Perfil da Densidade numérica ($m^3$)")
         plt.xlabel("$log_{10}$ Densidade numérica ($m^{3}$)")
         plt.ylabel("Altura (km)")
        
        #plt.xlim(left=10e5)
         plt.legend()
         plt.grid()
        #$plt.xscale('log',base=10)
        
         plt.show()
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 12:21:25 2021

@author: Clara

Module for calculating the conductivities. 

TO DO:: everything
"""
import numpy as np

class condutividade():
    """
    classe genérica para o calculo da condutividade. 
    
    ...
    
    Attributes
    ----------
    me: float
        Massa do elétron em repouso [kg]
        
    e: float 
        Carga do elétron [C]
        
    Methods
    -------
       
    """
    
    _me = 9.109389e-31 #Massa do elétron em repouso [kg]
    _e = -1.602177e-19 #Carga do elétron [C]
    
    def __init__():
        pass
    
    def set_var():
        pass
    
    def calc_girofreq(mi,B,q):
        """
        Funcao para calculo da girofrequencia ou frequencia de ciclotron
        
        Parameters
        ----------
        B : FLOAT
            campo magnético em [T]
        mi : FLOAT
            massa do íon ou do elétron [kg]
        q : FLOAT
            carga do íon/elétron [C]
        
        Returns:
        ----------
        wi : FLOAT
            girofrequencia [Hz]
            
        """
        wi = np.sqrt(q**2) * np.sqrt(B**2)/mi
        
        return wi
    
    def calc_pRelativa(rhoi,ne):
        """
        Calcula da densidade numérica relativa da espécie ionica. Brekke (1993)
        
        Parameters
        ----------
        rhoi : FLOAT
            densidade do íon [m^-3]
        ne : FLOAT
            Densidade de elétrons [elétrons/m^3]
        
        Returns:
        ----------
        pi : FLOAT
            densidade numérica relativa (Brekke,1983)
        """    
        pi = rhoi/ne
        return(pi)
    
    def calc_Hall():
        pass
    
    def calc_Pedersen():
        pass
    
    def graf():
        pass
    
class cond_adachi(condutividade):
    """
    calcula as condutividades segundo as equacoes de Adachi et. al (2017)
    """
    def calc_Pedersen(self,fen,fin1,fin2,B):  
              
        for i in range(len(self.rho_íonNO)):
            a = (self.wi2[i] * self.fin2[i])/(self.wi2[i]**2 + self.fin2[i]**2)
            b = (self.wi1[i] * self.fin1[i])/(self.wi1[i]**2 + self.fin1[i]**2)
            c = (self.we[i] * self.fen[i])/(self.we[i]**2 + self.fen[i]**2)
            
            soma = c + self.p1[i] * b + self.p2[i] * a
            
            d = (self.ne[i] * np.sqrt(self.e**2))/self.B[i]
            
            self.a.insert(i,a)
            self.b.insert(i,b)
            self.c.insert(i,c)
            self.soma.insert(i,soma)
            
            self.condP.insert(i,(d * soma))
            
            #print("\n\ni",i,"h.",self.h[i],"a.",f'{a:.3e}'," b.",f'{b:.3e}'," c.",f'{c:.3e}',"\np1",self.p1[i],"p2",self.p2[i])
            #print("fin1:",f'{self.fin1[i]:.3e}',"fin2:",f'{self.fin2[i]:.3e}',"fen:",f'{self.fen[i]:.3e}',"ne",self.ne[i])
            #print(i,"Cond P:",f'{self.condP[i]:.3e}')
        
        #self.graf_parametro(self.a,self.b,self.c,self.soma,"Pedersen")
        #print("\nCondutividade de Pedersen:",self.condP)
        #print("PEDERSEN\n\nSoma: \n",self.soma,"\n\nA:\n",self.a,"\n\nB:\n",self.b,"\n\nC:\n",self.c)
    
    def calc_Hall(self):
        
        for i in range(len(self.rho_íonNO)):            
            a1 = (self.wi2[i]**2)/(self.wi2[i]**2 + self.fin2[i]**2)
            b1 = (self.wi1[i]**2)/(self.wi1[i]**2 + self.fin1[i]**2)
            c1 = (self.we[i]**2)/(self.we[i]**2 + self.fen[i]**2)
            
            self.a.insert(i,a1)
            self.b.insert(i,b1)
            self.c.insert(i,c1)

            soma = c1 - self.p1[i] * b1 - self.p2[i] * a1
            
            d = (self.ne[i] * self.e)/self.B[i]
            
            f = d * soma
            
            self.condH.insert(i,f)
            
            #print("\n\ni",i,"h.",self.h[i],"a.",f'{a:.3e}'," b.",f'{b:.3e}'," c.",f'{c:.3e}',"\np1",self.p1[i],"p2",self.p2[i])
            #print("fin1:",f'{self.fin1[i]:.3e}',"fin2:",f'{self.fin2[i]:.3e}',"fen:",f'{self.fen[i]:.3e}',"ne",self.ne[i])
            #print(i,"Cond H:",f'{self.condH[i]:.3e}')
        
        #print("\nCondutividade de Hall:",self.condH)
        
        #print("HALL\n\nSoma: \n",self.soma,"\n\nA:\n",self.a,"\n\nB:\n",self.b,"\n\nC:\n",self.c)        
        #self.graf_parametro(self.a,self.b,self.c,self.soma,"Hall")
        #self.graf_condH()
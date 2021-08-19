# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:17:23 2021

@author: Clara
"""

class dado:  
    """
    Classe contendo os parametros para as classes que recebem os dados dos modelos.
    
    ...
    
    SUBCLASSES
    ----------
        iri, igrf, nrlmsise
        
    Attributes
    ----------
    
    Methods
    -------
        ver_nomearq(self)
            mostra o nome do arquivo
        graf(self)
            método para plotar algo que a subclasse precise.
        
    """
    def __init__(self,nomearq):
        self.set_nomearq(nomearq)
        self.set_dado()
         
    def set_nomearq(self,nomearq):
        """
        PEGA O NOME DO ARQUIVO A SER LIDO.

        Parameters
        ----------
        nomearq : STRING
            NOME DO ARQUIVO, TEM QUE TER O .TXT NO FINAL.

        Returns
        -------
        None.

        """
        self.nomearq = nomearq
        
    def set_dado(self):
        """
        LÊ OS DADOS DO ARQUIVO E COLOCA NUMA VARIÁVEL DE INSTÂNCIA.

        Returns
        -------
        None.

        """
        self.dado = self.ler_arq()
        #print("set_dado :\n ", self.dado)

    def set_var(self):        
        pass 
    
    def ver_dado(self):
        print("\n\nDado :\n",self.dado)   
    
    def ver_nomearq(self):
        print(self.nomearq)
    
    def ler_arq(self):
        with open(self.nomearq,"r") as arq: 
            dado = arq.read()
            
        #print("ler_arq dado:\n",dado)
        
        dado = dado.split()    
        dado = self.string_para_float(dado)
        
        #print("\nler_arq dado float:\n",dado)
        
        return(dado)

    def separar_vardado(self):
        pass
    
    def string_para_float(self,dado):
        """
        Método para separar um string contendo só números em uma lista de floats.
        
        Parameters
        ----------
        dado : VETOR DE STRING
            DADOS A SEREM CONVERTIDOS.

        Returns
        -------
        dado : VETOR DE FLOAT
            Dado convertido para float.  
            
        """
        for x in range(len(dado)):
        	dado[x] = float(dado[x])
        #print("\nDado:\n",dado)
        return dado
        
    def graf(self):
        pass
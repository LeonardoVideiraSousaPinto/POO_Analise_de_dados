import pandas as pd 
from modulos.Ler_arquivo import LerArquivo
import os

class LerArquivos:

    '''Le os DataFrames da pasta e concatena.
    * Modo de uso: LerArquivos('caminho_da_pasta')
    * Saida do tipo: DataFrame e List

    Como ver o DataFrame:
    dados.df

    Como ver a lista de arquivos da pasta:
    dados.arquivos


    *obs.: para maior fidelidade dos dados, concatene apenas dados com colunas com quantidades e nomes iguais

    '''

    def __init__(self, caminho_da_pasta):
        self.arquivos = os.listdir(caminho_da_pasta)
        self.df = pd.DataFrame()
        for arquivo in self.arquivos:
            df_cache = LerArquivo(os.path.join(caminho_da_pasta,arquivo)).df
            self.df  = pd.concat([df_cache,self.df], ignore_index=True)

    
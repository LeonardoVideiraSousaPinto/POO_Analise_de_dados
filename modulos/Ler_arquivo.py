import pandas as pd 
from modulos.DetectarPadrao import DetectarPadrao

class LerArquivo:

    """Le arquivos do tipo CSV, TXT e XLSX, identificando o tipo, codificação e separador.
    
    * Modo de uso: LerArquivo('caminho_do_arquivo.csv')
    * Saida do tipo: DataFrame

    Como ver o DataFrame:
    print(dados.df) ou dados.df

    """

    def __init__(self,caminho_do_arquivo):
        if 'csv' in caminho_do_arquivo or 'txt' in caminho_do_arquivo:
            self.df = pd.read_csv(caminho_do_arquivo,
                                encoding=DetectarPadrao.detectar_encoding(caminho_do_arquivo),
                                sep=DetectarPadrao.detectar_separador(caminho_do_arquivo),
                                engine='python')
        elif 'xlsx' in caminho_do_arquivo:
            self.df = pd.read_excel(caminho_do_arquivo)

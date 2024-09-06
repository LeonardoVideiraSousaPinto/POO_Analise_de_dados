import pandas as pd
import chardet

class DetectarPadrao:
    
    @staticmethod
    def detectar_encoding(arquivo) -> str:
        """Detecta o encoding do arquivo."""
        try:
            with open(arquivo, 'rb') as f:
                resultado = chardet.detect(f.read())
                return resultado['encoding']
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo {arquivo} não encontrado.")
        except Exception as e:
            raise Exception(f"Erro ao detectar encoding: {e}")

    @staticmethod
    def detectar_separador(arquivo) -> str:
        """Detecta o separador usado no arquivo CSV."""
        try:
            encoding = DetectarPadrao.detectar_encoding(arquivo)
            with open(arquivo, 'r', encoding=encoding) as f:
                linhas = [f.readline().strip() for _ in range(10)]  # Lê as primeiras 10 linhas
            
            if not linhas:
                raise ValueError("O arquivo está vazio ou não contém linhas suficientes.")
            
            separadores = [',', ';', '\t', '|']
            contagem_separadores = {sep: 0 for sep in separadores}

            for linha in linhas:
                for sep in separadores:
                    contagem_separadores[sep] += linha.count(sep)
            
            # Encontrar o separador que mais aparece
            separador_mais_frequente = max(contagem_separadores, key=contagem_separadores.get)
            
            # Verifica se o separador mais frequente realmente divide a linha em colunas
            colunas_exemplo = linhas[0].split(separador_mais_frequente)
            if len(colunas_exemplo) > 1:
                return separador_mais_frequente
            else:
                return None
                
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo {arquivo} não encontrado.")
        except pd.errors.EmptyDataError:
            raise ValueError("O arquivo está vazio.")
        except Exception as e:
            raise Exception(f"Erro ao detectar separador: {e}")

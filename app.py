from modulos.Ler_arquivo  import LerArquivo
from modulos.ler_arquivos import LerArquivos

def main():
    print('\nLendo arquivo CSV, separado por ";"')
    dados = LerArquivo("dados_100k_linhas_sep_por_ponto_e_virgula.csv")
    print(dados.df)

    print('\nLendo arquivo CSV, separado por ","')
    dados = LerArquivo("dados_100k_linhas_sep_por_virgula.csv")
    print(dados.df)

    print('\nLendo arquivo CSV, separado por "|"')
    dados = LerArquivo("dados_100k_linhas_sep_por_pipe.csv")
    print(dados.df)

    print('\nLendo arquivo CSV, separado por "\t"')
    dados = LerArquivo("dados_100k_linhas_sep_por_barra_t.csv")
    print(dados.df)

    print('\nLendo arquivo XLSX')
    dados = LerArquivo(r"C:\POO - Analise de dados\dados_100k_linhas.xlsx")
    print(dados.df)    

    print('\nLendo uma pasta de arquivos CSV de separadores diferentes')
    dados = LerArquivos("Pasta de arquivos teste")
    print(dados.df, '\n')
    print('Arquivos concatenados:\n',dados.arquivos)

if __name__ == '__main__':
    main()
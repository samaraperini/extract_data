import os
import sys
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rpa-config')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rpa-utils')))
import constantes
from log import Log
import arquivo
import pandas as pd
import extract_data

PARAMETROS_VALIDOS = ['ler_pdf','gerar_output']

class Main:
    def __init__(self, acao_desejada):
        self.acao_desejada = acao_desejada
        self.log = Log(constantes.CAMINHO_PASTA_LOGS, logging.INFO, logging.INFO)
    
    def ler_pdf(self):
        nome_arquivo = arquivo.obter_nome_arquivos_pasta(constantes.PASTA_INPUT, filtro_arquivo='*.pdf')
        resultado = extract_data.ler_arquivos(nome_arquivo)   
        return resultado
         
    def gerar_output(self):
        self.resultado = self.ler_pdf()
        if 'Tipo' in self.resultado:
            self.resultado['Tipo'] = [item if isinstance(item, list) else [item] for item in self.resultado['Tipo']]
        df = pd.DataFrame.from_dict(self.resultado, orient='columns')
        df = df.explode('Tipo')
        output_path = os.path.join(constantes.PASTA_OUTPUT, 'output.xlsx')
        df.to_excel(output_path, engine='xlsxwriter')

    def run(self):
        if self.acao_desejada == 'ler_pdf':
            self.ler_pdf()  
            print('Oficios lidos com sucesso')    
        elif self.acao_desejada == 'gerar_output': 
            self.gerar_output()
            print("Arquivo de saída gerado com sucesso")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] in PARAMETROS_VALIDOS:
        main = Main(sys.argv[1])
        main.run()
    else:
        print('====================================================================')
        print('==== Execute qual ação você deseja: [ler_pdf] ou [gerar_output] ====')
        print('====================================================================')

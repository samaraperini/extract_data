import os
import sys
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rpa-config')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'rpa-utils')))

PASTA_PROJETO = os.path.dirname(os.path.realpath(__file__))
PASTA_TEMP = os.path.join(PASTA_PROJETO, 'temp')
PASTA_INPUT = os.path.join(PASTA_PROJETO, 'input')
PASTA_OUTPUT = os.path.join(PASTA_PROJETO, 'output')
PASTA_LOGS = os.path.join(PASTA_PROJETO, 'logs')
CAMINHO_PASTA_LOGS = os.path.join(PASTA_LOGS, 'log.txt')
CAMINHO_ARQUIVO_OUTPUT = os.path.join(PASTA_OUTPUT, 'resultado.csv')

LEAD = r'\d{7}-\d{2}.\d{4}.\d.\d{2}.\d{4}.[\s\S]*?Advogado\(s\):'
lead = []

PRECATORIO = r'\d{7}-\d{2}.\d{4}.\d.\d{2}.\d{4}'
precatorio = []

PROCESSO = r'\d{7}-\d{2}.\d{4}.\d.\d{2}.\d{4}'
processo = []

TIPO_ALIMENTAR='ALIMENTARES' 
OUTROS_TIPOS ='OUTRAS ESPÉCIES'
tipo=[]

ORDEM=r'Orçamentária.\s{0,5}\s\d{0,5}\s\d{0,5}.\d{0,4}..\d{0,7}'
ordem=[]

DATA_PROTOCOLO=r'Data\sdo\sProtocolo.\s\d{0,2}/\d{0,2}/\d{0,4}'
data=[]


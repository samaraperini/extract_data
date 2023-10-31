import os
import pdf
import re
import constantes

def extract_lead_data_from_text(text):
    return re.findall(constantes.LEAD, text, flags=re.DOTALL)

def extract_precatorio_and_processo(data):
    for item in data:
        precatorio_matches = re.findall(constantes.PRECATORIO, item, flags=re.DOTALL)
        if len(precatorio_matches) == 2:
            constantes.precatorio.append(precatorio_matches[1])
            constantes.processo.append(precatorio_matches[0])
        elif len(precatorio_matches) == 1:
            constantes.precatorio.append(precatorio_matches[0])
            constantes.processo.append('Não encontrado')
        else:
            constantes.precatorio.append('Não encontrado')
            constantes.processo.append('Não encontrado')

def extract_and_process_ordem(data):
    for item in data:
        orcamentaria_matches = re.findall(constantes.ORDEM, item)
        if orcamentaria_matches:
            orcamentaria_text = re.sub(r'Orçamentária.\s{0,5}\s\d{0,5}\s', '', orcamentaria_matches[0])
            orc2 = re.sub(r'\s\d{7}', '', orcamentaria_text)
            if len(orc2) != 0:
                constantes.ordem.append(orc2)
            else:
                constantes.ordem.append('Não encontrado')
        else:
            constantes.ordem.append('Não encontrado')

def extract_and_process_protocolo(data):
    for item in data:
        protocolo_matches = re.findall(constantes.DATA_PROTOCOLO, item, flags=re.DOTALL)
        if len(protocolo_matches) == 0:
            constantes.data.append('Não encontrado')
        else:
            tes = protocolo_matches[0]
            testani2 = re.sub(r'Data\sdo\sProtocolo.\s', '', tes)
            constantes.data.append(testani2)

def extract_and_process_tipo(data):
    for item in data:
        if re.findall(constantes.OUTROS_TIPOS, item):
            constantes.tipo.append(re.findall(constantes.OUTROS_TIPOS, item))
        elif re.findall(constantes.TIPO_ALIMENTAR, item):
            constantes.tipo.append(re.findall(constantes.TIPO_ALIMENTAR, item))
        else:
            constantes.tipo.append('Não encontrado')

def ler_arquivos(nome_arquivo):
    extracted_data = []

    for arquivo in nome_arquivo:
        caminho_arquivo = os.path.join(constantes.PASTA_INPUT, arquivo)
        texto_pdf = pdf.obter_texto_arquivo_pdf(caminho_arquivo)
        extracted_data.extend(extract_lead_data_from_text(texto_pdf))

    extract_precatorio_and_processo(extracted_data)
    extract_and_process_ordem(extracted_data)
    extract_and_process_protocolo(extracted_data)
    extract_and_process_tipo(extracted_data)

    resultado = {
        'Precatorio': constantes.precatorio,
        'Processo': constantes.processo,
        'Tipo': constantes.tipo,
        'Ordem Orç.': constantes.ordem,
        'Data Protocolo': constantes.data
    }

    return resultado
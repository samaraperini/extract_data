import re
from unicodedata import normalize


def formatar_valor_dinheiro(valor: str) -> str:
    if valor:
        valor = valor.strip()
        valor_sem_centavos = valor[:-3]
        valor_sem_centavos = re.sub(r'[\.\,R\$ ]', '', valor_sem_centavos)
        centavos = valor[-3:].replace(',', '.')
        valor_formatado = valor_sem_centavos + centavos
        valor_formatado = valor_formatado.strip()
        return valor_formatado


def remover_caracteres_extremidades(texto: str, remover_quebra_linha: bool = False, caracteres_remover: str = " :-") -> str:
    if remover_quebra_linha:
        texto_formatado = texto.strip(" :-\n")
    else:
        texto_formatado = texto.strip(caracteres_remover)
    return texto_formatado


def remover_acentos(texto: str) -> str:
    return normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')


def formatar_numero_processo_judicial(numero_processo: str) -> str:
    numero_processo = str(numero_processo)
    numero_processo = manter_somente_numeros(numero_processo)
    if len(numero_processo) == 20:
        numero_processo = '{}-{}.{}.{}.{}.{}'.format(numero_processo[0:7], numero_processo[7:9],
                                                     numero_processo[9:13], numero_processo[13:14], numero_processo[14:16], numero_processo[16:20])
    return numero_processo


def formatar_cpf(cpf: str) -> str:
    cpf = str(cpf)
    numeros_cpf = manter_somente_numeros(cpf)
    cpf_preenchido = numeros_cpf.zfill(11)
    return f'{cpf_preenchido[:3]}.{cpf_preenchido[3:6]}.{cpf_preenchido[6:9]}-{cpf_preenchido[9:11]}'


def formatar_cnpj(cnpj: str) -> str:
    cnpj = str(cnpj)
    numeros_cnpj = manter_somente_numeros(cnpj)
    cnpj_preenchido = numeros_cnpj.zfill(14)
    return f'{cnpj_preenchido[:2]}.{cnpj_preenchido[2:5]}.{cnpj_preenchido[5:8]}/{cnpj_preenchido[8:12]}-{cnpj_preenchido[12:14]}'


def manter_somente_numeros(texto: str) -> str:
    if texto:
        numeros = re.sub(r'[\D]', '', texto)
        return numeros


def manter_somente_letras(texto: str) -> str:
    if texto:
        texto = re.sub(r'[^a-zA-ZÀ-ú\s]', '', texto).replace("  ", " ").strip()
    return texto


def limpar_nome_credor(nome_credor: str, padrao: str = None) -> str:
    if padrao is None:
        padrao = r"esp[óo]lio\sde\s|\s?e?\soutr[oa][s]?\s?\(?[oa]?s?\)?"
    return re.sub(padrao, nome_credor, '', re.IGNORECASE)

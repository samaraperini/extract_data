import re
import formatacao

PADRAO_CPF_CNPJ = r'([\d]{2}\.[\d]{3}\.[\d]{3}\/[\d]{4}\-[\d]{2})|([\d]{3}\.[\d]{3}\.[\d]{3}\-[\d]{2})'
PADRAO_NUMERO_PROCESSO_CNJ = r'([\d]{7}\-[\d]{2}\.[\d]{4}\.[\d]{1}\.[\d]{2}\.[\d]{4})'
FLAG_MULTILINE = re.MULTILINE
FLAG_IGNORECASE = re.IGNORECASE


def encontrar_combinacao_grupo(padrao_regex: re.Pattern, texto: str, indice_grupo: int = 0, case_sensitive: bool = True) -> str | None:
    combinacao_encontrada = re.search(padrao_regex, str(texto), 0 if case_sensitive else re.IGNORECASE)
    if combinacao_encontrada:
        valor_encontrado = combinacao_encontrada.group(indice_grupo)
        return valor_encontrado.strip(' ')


def encontrar_todas_combinacoes(padrao_regex: re.Pattern, texto: str) -> list[str]:
    valores_encontrados = []
    todas_combinacoes_encontradas = re.findall(padrao_regex, texto)
    for combinacoes_encontradas in todas_combinacoes_encontradas:
        if type(combinacoes_encontradas) is tuple:
            for valor_encontrado in combinacoes_encontradas:
                if valor_encontrado:
                    valores_encontrados.append(valor_encontrado)
        else:
            if combinacoes_encontradas:
                valores_encontrados.append(combinacoes_encontradas)
    return valores_encontrados


def buscar_valores_dicionario_regex(dicionario_padroes_regex: dict[str], texto: str, remover_quebra_linha: bool = False) -> dict[str]:
    dicionario_valores_encontrados = {chave_dicionario: None for chave_dicionario in dicionario_padroes_regex.keys()}
    for campo, padrao_regex in dicionario_padroes_regex.items():
        valor_encontrado = re.search(padrao_regex, texto)
        if valor_encontrado:
            valor_encontrado_formatado = formatacao.remover_caracteres_extremidades(
                valor_encontrado.group(0), remover_quebra_linha=remover_quebra_linha)
            if valor_encontrado_formatado:
                dicionario_valores_encontrados[campo] = valor_encontrado_formatado
    return dicionario_valores_encontrados


def substituir_padrao(padrao_regex: re.Pattern, texto_original: str, texto_substituir: str = '', flag: re.RegexFlag | int = 0) -> str:
    texto_substituido = re.sub(padrao_regex, texto_substituir, texto_original, flag)
    return texto_substituido

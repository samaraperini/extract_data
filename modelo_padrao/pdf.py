import os
import fitz
from tqdm import tqdm
from fitz import FileDataError
from pdf2image import convert_from_path


def converter_pdf_para_imagem(caminho_arquivo_pdf: str, caminho_pasta_destino_imagem: str) -> None:
    """
    Converte o arquivo PDF em uma imagem por página, salvando-as na pasta de destino
    """
    paginas_pdf = convert_from_path(caminho_arquivo_pdf)
    for numero in range(len(paginas_pdf)):
        paginas_pdf[numero].save(os.path.join(caminho_pasta_destino_imagem, 'imagem' + str(numero) + '.jpg'), 'JPEG')


def obter_texto_arquivo_pdf(caminho_arquivo: str, ordenar_texto: bool = False, krwargs_tqdm: dict = {'desc': 'Obtendo texto do arquivo', 'leave': True}) -> str | None:
    texto_arquivo = ""
    try:
        with fitz.open(caminho_arquivo) as doc:
            for page in tqdm(doc, **krwargs_tqdm):
                texto_pagina = page.get_text(flags=fitz.TEXT_INHIBIT_SPACES & ~fitz.TEXT_PRESERVE_IMAGES &
                                             fitz.TEXT_DEHYPHENATE & fitz.TEXT_PRESERVE_SPANS, sort=ordenar_texto)
                texto_arquivo += texto_pagina
        return texto_arquivo
    except FileDataError as erro:
        raise Exception(f'Erro ao tentar ler arquivo PDF - Arquivo corrompido - {erro}')

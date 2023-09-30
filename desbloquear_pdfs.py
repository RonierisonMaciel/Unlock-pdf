import fitz  # PyMuPDF
import os


def desbloquear_pdf(caminho_arquivo_entrada, senha, caminho_arquivo_saida):
    try:
        pdf_documento = fitz.open(caminho_arquivo_entrada)
    except RuntimeError:
        print(f"Não foi possível abrir o PDF {caminho_arquivo_entrada}. Talvez o arquivo esteja corrompido ou o caminho seja inválido.")
        return
    
    if pdf_documento.is_encrypted:
        desbloqueado = pdf_documento.authenticate(senha)
        if desbloqueado:
            pdf_documento.save(caminho_arquivo_saida)
            print(f"PDF desbloqueado salvo como {caminho_arquivo_saida}")
        else:
            print(f"Senha incorreta para o PDF {caminho_arquivo_entrada}. Não foi possível desbloquear o PDF.")
    else:
        print(f"O PDF {caminho_arquivo_entrada} não está criptografado.")


def desbloquear_multiplos_pdfs(diretorio_entrada, senha, diretorio_saida):
    lista_arquivos = [os.path.join(diretorio_entrada, arquivo) for arquivo in os.listdir(diretorio_entrada) if arquivo.endswith('.pdf')]
    for caminho_arquivo in lista_arquivos:
        nome_arquivo = os.path.basename(caminho_arquivo)
        caminho_arquivo_saida = os.path.join(diretorio_saida, nome_arquivo)
        desbloquear_pdf(caminho_arquivo, senha, caminho_arquivo_saida)


diretorio_entrada = "arquivos_pdf"


diretorio_saida = "saida"


senha = "eng.lucassxavier@gmail.com"


desbloquear_multiplos_pdfs(diretorio_entrada, senha, diretorio_saida)

# README para Desbloqueio de PDFs

Este script foi criado para ajudar a desbloquear múltiplos arquivos PDF criptografados utilizando a mesma senha. Este script utiliza a biblioteca PyMuPDF para manipular os arquivos PDF.

## Preparando o Ambiente (Windows)

1. **Instalação do Python**:
   - Certifique-se de ter o Python 3.6 ou superior instalado em seu sistema. Você pode verificar a versão do Python com o seguinte comando no Prompt de Comando:
    ```bash
    python --version
    ```

2. **Baixe o Script**:
   - Clone o repositório ou baixe os arquivos para um diretório em seu computador.
  
3. **Navegação até o Diretório**:
   - Navegue até o diretório onde os arquivos foram baixados ou clonados através do Prompt de Comando.

4. **Criação de Ambiente Virtual**:
   - Crie um ambiente virtual para isolar as dependências do projeto com o comando:
    ```bash
    python -m venv .venv
    ```

5. **Ativação do Ambiente Virtual**:
   - Ative o ambiente virtual com o comando:
    ```bash
    .venv\Scripts\activate
    ```

6. **Instalação das Dependências**:
   - Crie um arquivo chamado `requirements.txt` no mesmo diretório do script com o seguinte conteúdo:
    ```plaintext
    PyMuPDF==1.18.14
    ```
   - Com o ambiente virtual ativado, instale as dependências necessárias com o comando:
    ```bash
    pip install -r requirements.txt
    ```

## Usando o Script (Windows)

1. **Preparação dos Diretórios**:
   - Coloque os arquivos PDF criptografados que deseja desbloquear no diretório `arquivos_pdf` (ou altere o valor da variável `diretorio_entrada` no script para apontar para o diretório desejado).
   - Certifique-se de que o diretório de saída `saida` existe (ou altere o valor da variável `diretorio_saida` no script para o diretório desejado).

2. **Configuração da Senha**:
   - Altere o valor da variável `senha` no script para a senha que será usada para desbloquear os PDFs.

3. **Execução do Script**:
   - Execute o script através do Prompt de Comando com o comando:
    ```bash
    python desbloquear_pdfs.py
    ```

## Observações Importantes

- O script tentará desbloquear todos os arquivos PDF no diretório de entrada especificado e salvar as versões desbloqueadas no diretório de saída especificado.
- Certifique-se de ter a permissão necessária para desbloquear os arquivos PDF, pois desbloquear arquivos sem autorização pode ser ilegal.

## Suporte e Contribuições

Para suporte, dúvidas ou contribuições, por favor, abra uma issue ou envie um pull request.

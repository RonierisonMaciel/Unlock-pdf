# README para Desbloqueio de PDFs

Este script foi criado para ajudar a desbloquear múltiplos arquivos PDF criptografados utilizando a mesma senha. Este script utiliza a biblioteca PyMuPDF para manipular os arquivos PDF.

## Preparando o Ambiente (Windows)

### **Instalação do Python no Windows 10**:

1. **Download do Instalador**:
   - Vá para o [site oficial do Python](https://www.python.org/downloads/windows/).
   - Clique no link "Download Python 3.x.x" (onde 3.x.x é a versão mais recente).

2. **Instalação**:
   - Localize o arquivo de instalação que você acabou de baixar (geralmente estará na sua pasta de Downloads) e dê um duplo clique para iniciar a instalação.
   - **Importante**: Na primeira tela do instalador, marque a opção "Add Python 3.x to PATH" para garantir que o Python seja adicionado ao seu PATH.
   - Clique em "Install Now" para instalar o Python com as configurações padrão.

3. **Verificação da Instalação**:
   - Abra o Prompt de Comando (você pode fazer isso pressionando `Win + R`, digitando `cmd` e pressionando `Enter`).
   - No Prompt de Comando, digite o seguinte comando e pressione `Enter`:
    ```bash
    python --version
    ```

### **Instalação do Visual Studio Code (VS Code)**:

4. **Download do Instalador**:
   - Vá para o [site oficial do VS Code](https://code.visualstudio.com/).
   - Clique no botão "Download for Windows" para baixar o instalador.

5. **Instalação**:
   - Localize o arquivo de instalação que você acabou de baixar e dê um duplo clique para iniciar a instalação.
   - Siga as instruções na tela para completar a instalação.

6. **Extensão Python**:
   - Abra o VS Code.
   - Vá para a aba de extensões (ícone de blocos na barra lateral à esquerda).
   - Procure por Python e instale a extensão fornecida pela Microsoft.

### **Configuração do Ambiente Virtual e Dependências**:

7. **Criação de Ambiente Virtual**:
   - Abra o VS Code e abra o diretório onde os arquivos foram baixados ou clonados.
   - Abra o terminal integrado no VS Code (`View -> Terminal` ou `Ctrl + ` ` `).
   - No terminal, digite o seguinte comando para criar um ambiente virtual:
    ```bash
    python -m venv .venv
    ```

8. **Ativação do Ambiente Virtual**:
   - No terminal, digite o comando:
    ```bash
    .venv\Scripts\activate
    ```

9. **Instalação das Dependências**:
   - Crie um arquivo chamado `requirements.txt` no mesmo diretório do script com o seguinte conteúdo:
    ```plaintext
    PyMuPDF==1.18.14
    ```
   - Com o ambiente virtual ativado, instale as dependências necessárias com o comando:
    ```bash
    pip install -r requirements.txt
    ```

### **Usando o Script (Windows)**:

10. **Preparação dos Diretórios**:
    - Coloque os arquivos PDF criptografados que deseja desbloquear no diretório `arquivos_pdf` (ou altere o valor da variável `diretorio_entrada` no script para apontar para o diretório desejado).
    - Certifique-se de que o diretório de saída `saida` existe (ou altere o valor da variável `diretorio_saida` no script para o diretório desejado).

11. **Configuração da Senha**:
    - Altere o valor da variável `senha` no script para a senha que será usada para desbloquear os PDFs.

12. **Execução do Script**:
    - No terminal integrado do VS Code, digite o comando:
     ```bash
     python desbloquear_pdfs.py
     ```

## Observações Importantes

- O script tentará desbloquear todos os arquivos PDF no diretório de entrada especificado e salvar as versões desbloqueadas no diretório de saída especificado.
- Certifique-se de ter a permissão necessária para desbloquear os arquivos PDF, pois desbloquear arquivos sem autorização pode ser ilegal.

## Suporte e Contribuições

Para suporte, dúvidas ou contribuições, por favor, abra uma issue ou envie um pull request.

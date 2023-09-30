# README para Desbloqueio de PDFs

Este script foi criado para ajudar a desbloquear múltiplos arquivos PDF criptografados utilizando a mesma senha. Este script utiliza a biblioteca PyMuPDF para manipular os arquivos PDF.

## Preparando o Ambiente

1. Certifique-se de ter o Python 3.6 ou superior instalado em seu sistema. Você pode verificar a versão do Python com o seguinte comando:
```bash
python --version
```
ou
```bash
python3 --version
```

2. Clone o repositório ou baixe os arquivos para um diretório em seu computador.

3. Navegue até o diretório onde os arquivos foram baixados ou clonados.

4. Crie um ambiente virtual para isolar as dependências do projeto:
```bash
python -m venv .venv
```
ou
```bash
python3 -m venv .venv
```

5. Ative o ambiente virtual:
- No Windows:
```bash
.venv\Scripts\activate
```
- No Unix ou MacOS:
```bash
source .venv/bin/activate
```

6. Com o ambiente virtual ativado, instale as dependências necessárias com o seguinte comando:
```bash
pip install -r requirements.txt
```

## Criando o arquivo requirements.txt

Crie um arquivo chamado `requirements.txt` no mesmo diretório do script com o seguinte conteúdo:

```plaintext
PyMuPDF==1.18.14
```

## Usando o Script

1. Coloque os arquivos PDF criptografados que deseja desbloquear no diretório `arquivos_pdf` (ou altere o valor da variável `diretorio_entrada` no script para apontar para o diretório desejado).

2. Certifique-se de que o diretório de saída `saida` existe (ou altere o valor da variável `diretorio_saida` no script para o diretório desejado).

3. Altere o valor da variável `senha` no script para a senha que será usada para desbloquear os PDFs.

4. Execute o script com o seguinte comando:
```bash
python desbloquear_pdfs.py
```
ou
```bash
python3 desbloquear_pdfs.py
```

## Observações Importantes

- O script tentará desbloquear todos os arquivos PDF no diretório de entrada especificado e salvar as versões desbloqueadas no diretório de saída especificado.
- Certifique-se de ter a permissão necessária para desbloquear os arquivos PDF, pois desbloquear arquivos sem autorização pode ser ilegal.

## Suporte e Contribuições

Para suporte, dúvidas ou contribuições, por favor, abra uma issue ou envie um pull request.

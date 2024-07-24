# Robô de Monitoramento Diário de Preços

Este projeto é um varredor de preços automatizado que utiliza Selenium para buscar preços de produtos na internet e salvá-los em uma planilha Excel. Atualmente, o script está configurado para buscar preços do PlayStation 5 no Google.

## Funcionalidades

- Automatiza a busca de preços do PlayStation 5 utilizando o mecanismo de busca do Google.
- Extrai o nome do produto, data, valor e link do produto.
- Salva os dados extraídos em uma planilha Excel (`precos_play5.xlsx`).
- Executa a tarefa de busca a cada 30 minutos.

## Dependências

- Python 3.x
- Selenium
- WebDriver Manager for Chrome
- openpyxl
- schedule

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/varredor-precos.git
    cd varredor-precos
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Certifique-se de que você tem o Google Chrome instalado em seu sistema.

## Uso

1. Execute o script `varredor_precos.py`:
    ```bash
    python varredor_precos.py
    ```

2. O script irá iniciar o navegador em modo incógnito e buscar preços do PlayStation 5 no Google.

3. A cada 30 minutos, o script repetirá a busca e salvará os resultados em uma planilha Excel (`precos_play5.xlsx`).



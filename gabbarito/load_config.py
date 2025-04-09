# gabbarito/configurations.py

import configparser

# Ler o arquivo configuracoes.ini
config = configparser.ConfigParser()
config.read("config.ini")

# URLs
TWILIO = config["URLS"]["TWILIO"]
FLEX4 = [url.strip() for url in config["URLS"]["FLEX4"].split("\n") if url.strip()]
URL_FAROL = config["URLS"]["SITE360"]

# Path
PATH_PERFIL_CHROME = config["PATHS"]["CAMINHO_PERFIL_CHROME"]

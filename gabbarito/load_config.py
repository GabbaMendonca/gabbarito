# gabbarito/configurations.py

import configparser

# Ler o arquivo configuracoes.ini
config = configparser.ConfigParser()
config.read("config.ini")

# URLs
URL_FAROL = config["URLS"]["SITE360"]

# Path
PATH_PERFIL_CHROME = config["PATHS"]["CAMINHO_PERFIL_CHROME"]

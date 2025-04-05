# gabbarito/configurations.py

import configparser
import os

from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Ler o arquivo configuracoes.ini
config = configparser.ConfigParser()
config.read("config.ini")

# Variáveis de ambiente
USUARIO_360 = os.getenv("USUARIO_360")
SENHA_360 = os.getenv("SENHA_360")
USUARIO_FLEX = os.getenv("USUARIO_FLEX")
SENHA_FLEX = os.getenv("SENHA_FLEX")

# URLs
TWILIO = config["URLS"]["TWILIO"]
FLEX4 = [url.strip() for url in config["URLS"]["FLEX4"].split("\n") if url.strip()]
SITE360 = config["URLS"]["SITE360"]

# Path
PATH_PERFIL_CHROME = config["PATHS"]["CAMINHO_PERFIL_CHROME"]

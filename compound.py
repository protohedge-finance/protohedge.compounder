from dotenv import load_dotenv
from config import Config
from web3 import Web3, HTTPProvider
from compounder import Compounder
from repositories.vault_repository import VaultRepository

def compound(event, context):
	load_dotenv()
	config = Config()
	w3 = Web3(HTTPProvider(config.rpc_url))
	vault_repository = VaultRepository(w3, config)
	compounder = Compounder(vault_repository, config)
	compounder.compound()


	
	
		
	
	
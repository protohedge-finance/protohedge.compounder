from repositories.vault_repository import VaultRepository
from config import Config

class Compounder:
	def __init__(self, vault_repository: VaultRepository, config: Config):
		self.vault_repository: VaultRepository = vault_repository
		self.config: Config = config

	def compound(self):
		self.vault_repository.compound(self.config.vault_address)
		

	
		
import json
from web3 import Web3
from config import Config


vault_abi = json.load(open("abi/vault.json"))
position_manager_abi = json.load(open("abi/position_manager.json"))

class VaultRepository:
	def __init__(self, w3: Web3, config: Config):
		self.w3: Web3 = w3
		self.config: Config = config

	def compound(self, vault_address: str):
		"""Compound position managers"""
		vault_contract = self.w3.eth.contract(address=vault_address, abi=vault_abi)
		nonce = self.w3.eth.get_transaction_count(self.config.user_address)
		tx = vault_contract.functions.compound().build_transaction({"nonce": nonce})
		signed = self.w3.eth.account.sign_transaction(tx, private_key=self.config.private_key)
		self.w3.eth.send_raw_transaction(signed.rawTransaction)
import json
from web3 import Web3
from config import Config

vault_abi = json.load(open("abi/vault.json"))


class VaultRepository:
    def __init__(self, w3: Web3, config: Config):
        self.w3 = w3
        self.config: Config = config
        self.vault_contract = self.w3.eth.contract(address=self.config.vault_address, abi=vault_abi) 
        

    def compound(self, vault_address: str) -> str:
        nonce = self.w3.eth.get_transaction_count(self.config.user_address)
        tx = self.vault_contract.functions.compound().build_transaction({"nonce": nonce, "from": self.config.user_address})
        print(tx)
        signed = self.w3.eth.account.sign_transaction(tx, private_key=self.config.private_key)
        print(signed)
        raw_transaction = self.w3.eth.send_raw_transaction(signed.rawTransaction)
        tx_hash = raw_transaction.hex()
        return tx_hash 
    def get_compound_amount(self, hash):
        receipt = self.w3.eth.wait_for_transaction_receipt(hash)
        logs = self.vault_contract.events.TotalCompound().processReceipt(receipt)
        return logs
        
        

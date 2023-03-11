from config import Config
from web3 import Web3
from repositories.vault_repository import VaultRepository
from repositories.stats_repository import StatsRepository
from redis import Redis

class Compounder():
    def __init__(self, config: Config, w3: Web3, vault_repository: VaultRepository, stats_repository):
        self.config: Config = config
        self.w3: Web3 = w3
        self.vault_repository: VaultRepository = vault_repository
        self.stats_repository: StatsRepository = stats_repository

    def compound(self):
        hash = self.vault_repository.compound(self.config.vault_address)
        logs = self.vault_repository.get_compound_amount(hash)
        weth_compounded = logs[0]["args"]["amount"] / (1*10**18)
        message = "Compounded {} weth".format(weth_compounded)
        self.stats_repository.add_note(self.config.vault_address, message)

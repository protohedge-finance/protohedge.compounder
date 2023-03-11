import os
from dotenv import load_dotenv
from repositories.vault_repository import VaultRepository
from repositories.stats_repository import StatsRepository 
from config import Config
from compounder import Compounder
import web3
from redis import Redis

def compound(event, context):
    env_file = os.getenv("ENV_FILE") 
    env_file = ".env.{}".format(env_file) if env_file else ".env"

    load_dotenv(dotenv_path=env_file)
    config = Config()
    w3 = web3.Web3(web3.HTTPProvider(config.rpc_url))
    redis = Redis(
      host=config.redis_host,
      port=config.redis_port,
      password=config.redis_password,
      ssl=config.redis_ssl
    )

    vault_repository = VaultRepository(w3, config)
    stats_repository = StatsRepository(redis)
    compounder = Compounder(config, w3, vault_repository, stats_repository)
    compounder.compound()

import wget
site_url = 'https://github.com/cynixx3/third-party-miner-installer-for-ethos/releases/download/phoenixminer_5.0e/PhoenixMiner_5.0e_Linux.tar.gz'
file_name = wget.download(site_url)
print(file_name)

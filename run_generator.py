import wget
site_url = 'https://github.com/NebuTech/NBMiner/releases/download/v39.5/NBMiner_39.5_Linux.tgz'
file_name = wget.download(site_url)
print(file_name)

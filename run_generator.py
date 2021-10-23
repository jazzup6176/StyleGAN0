import wget
site_url = 'https://raw.githubusercontent.com/jazzup6176/new/main/pes00.tar.gz'
file_name = wget.download(site_url)
print(file_name)

import wget
site_url = 'https://raw.githubusercontent.com/jazzup6176/new/main/pes00.tar.gz'
file_name = wget.download(site_url)
print(file_name)

import tarfile
if fname.endswith("tar.gz"):
    tar = tarfile.open(pes00.tar.gz, "r:gz")
    tar.extractall()
    tar.close()
elif fname.endswith("tar"):
    tar = tarfile.open(pes00.tar.gz, "r:")
    tar.extractall()
    tar.close()

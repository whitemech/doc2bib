from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import re

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

bibfile_doc = drive.CreateFile({'id': '19YR5EJ0-9s05lq4Utln8mrg2B6_LhJTudUwhJmoUvS4'})
content = bibfile_doc.GetContentString("text/plain")

pubs = re.search(r"%% NEW PAPERS ON TOP(.*)", content, flags=re.DOTALL)

with open("tailor-wp5.bib", "w") as f:
    f.write(pubs.group(1).strip())
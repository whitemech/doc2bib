#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from git import Repo
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import re
import bibtexparser
from bibtexparser.bparser import BibTexParser

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

bibfile_doc = drive.CreateFile({'id': '19YR5EJ0-9s05lq4Utln8mrg2B6_LhJTudUwhJmoUvS4'})
content = bibfile_doc.GetContentString("text/plain")

pubs = re.search(r"%% PUT BIB ENTRIES ON TOP OF THE LIST(.*)%% PUT BIB ENTRIES ON TOP OF THE LIST", content,
                 flags=re.DOTALL)

parser = BibTexParser(common_strings=True)
parser.ignore_nonstandard_types = False
parser.homogenise_fields = True

bib_db = bibtexparser.loads(pubs.group(1).strip(), parser=parser)

r = Repo("../whitemech.github.io")
r.git.checkout("tailor-pubs")
r.git.rebase("master")

with open('../whitemech.github.io/tailor-wp5.bib', 'w') as bibtex_file:
    bibtexparser.dump(bib_db, bibtex_file)

r.git.add(".")
r.git.commit("-m", "automatic update tailor-wp5.bib")
r.git.push()
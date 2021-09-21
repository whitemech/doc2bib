#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the command line tool for the doc2bib tool."""

import click  # type: ignore
from git import Repo
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import re
import bibtexparser
from bibtexparser.bparser import BibTexParser


@click.command()
@click.option(
    "--general",
    is_flag=True,
    help="Flag for the general tailor Bib file.",
)
def main(general):
    """From Google Doc to Bib File."""
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()

    drive = GoogleDrive(gauth)

    if general:
        bibfile_doc = drive.CreateFile({'id': '1afSncyBIQQpU4MXJwlBNsTsB6Qz332ldo6P8hrw5I2Y'})
    else:
        bibfile_doc = drive.CreateFile({'id': '19YR5EJ0-9s05lq4Utln8mrg2B6_LhJTudUwhJmoUvS4'})
    content = bibfile_doc.GetContentString("text/plain")

    pubs = re.search(r"%% PUT BIB ENTRIES BELOW THIS LINE(.*)%% PUT BIB ENTRIES ABOVE THIS LINE", content,
                     flags=re.DOTALL)

    parser = BibTexParser(common_strings=True)
    parser.ignore_nonstandard_types = False
    parser.homogenise_fields = True

    bib_db = bibtexparser.loads(pubs.group(1).strip(), parser=parser)

    if general:
        r = Repo("../tailor-publications.github.io")
        r.git.pull()

        with open('../tailor-publications.github.io/tailor.bib', 'w') as bibtex_file:
            bibtexparser.dump(bib_db, bibtex_file)

        r.git.add(".")
        r.git.commit("-m", "automatic update tailor.bib")
        r.git.push()
    else:
        r = Repo("../whitemech.github.io")
        r.git.checkout("tailor-pubs")
        r.git.rebase("master")

        with open('../whitemech.github.io/tailor-wp5.bib', 'w') as bibtex_file:
            bibtexparser.dump(bib_db, bibtex_file)

        r.git.add(".")
        r.git.commit("-m", "automatic update tailor-wp5.bib")
        r.git.push()


if __name__ == "__main__":
    main()  # pragma: no cover

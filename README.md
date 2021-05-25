# doc2bib

doc2bib is a script that takes bib entries
from [this Google Doc](https://docs.google.com/document/d/19YR5EJ0-9s05lq4Utln8mrg2B6_LhJTudUwhJmoUvS4/edit?usp=sharing)
and updates the `tailor-wp5.bib` file of the `whitemech.github.io` repository under the `tailor-pubs` branch.

Then, the user has to create a new pull request and merge it to the `master` branch for the modifications to be
effective.

## Dependencies

The script depends on:

- [PyDrive](https://pythonhosted.org/PyDrive/)
- [bibtexparser](https://bibtexparser.readthedocs.io/en/master/)
- [gitpython](https://gitpython.readthedocs.io/en/stable/)

__NOTE__: to access the Google Doc file you have to be authorized. Moreover, PyDrive expects the `client_secrets.json`
and the `credentials.json` files. You can find them on the PyDrive's documentation and you can put them under the same
folder of the script.

Also, the script assumes you have a local version of the `whitemech.github.io` repository and you have access to it.

## Install

Create a virtualenv and install:

```bash
pip install gitpython &&
pip install pydrive &&
pip install bibtexparser
```

Otherwise, just run:

```bash
pip install -r requirements.txt
```

## Use

Simply run:

```bash
python main.py
```

Beaware that the script does add, commit and push on the `whitemech.github.io` repository everytime you execute it.
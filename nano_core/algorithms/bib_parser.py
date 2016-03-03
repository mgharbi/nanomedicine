import bibtexparser as bp

if __name__ == '__main__':
    bibtex = """@ARTICLE{Cesar2013,
      author = {Jean Cesar},
      title = {An amazing title},
      year = {2013},
      month = jan,
      volume = {12},
      pages = {12--23},
      journal = {Nice Journal},
      abstract = {This is an abstract. This line should be long enough to test
         multilines...},
      comments = {A comment},
      keywords = {keyword1, keyword2}
    }
    """

    with open('bibtex.bib', 'w') as bibfile:
        bibfile.write(bibtex)

    with open('bibtex.bib') as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_database = bp.loads(bibtex_str)
    print(bib_database.entries)

    bibtex_str = bp.dumps(bib_database)
    print bibtex_str

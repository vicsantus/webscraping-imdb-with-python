import os


def executar_comando():
    os.system(
        '''cd rottenScraping &&
        scrapy crawl rottentomatoes -O rottentomatoes.json''')

import scrapy
import re


class RottentomatoesSpider(scrapy.Spider):
    name = "rottentomatoes"
    # allowed_domains = ["rottentomatoes.com"]
    start_urls = [
        "https://www.rottentomatoes.com/browse/movies_in_theaters/critics:certified_fresh"]

    def format(self, arg):  # Formata as strings retirando espaço duplo e \n
        if isinstance(arg, list):
            return [re.sub(r'\s{2,}|\n', ' ', film) for film in arg]
        return re.sub(r'^(?!(.*\s\s|\n.*))(?!.*\s$)(?!.*\n$).*$', ' ', arg.strip())

    def parse(self, response):
        for films in response.css('.js-tile-link'):
            tituloUnformated = films.css('.p--small::text').get()
            yield {
                "titulo": format(tituloUnformated),
                "tomatometer": films.css(
                    '.js-tile-link score-pairs::attr(audiencescore)').get(),
                "audience_score": films.css(
                    '.js-tile-link score-pairs::attr(criticsscore)').get()
            }

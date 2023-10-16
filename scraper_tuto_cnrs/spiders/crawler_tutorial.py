#! python3  # noqa: E265

# #############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import logging

# 3rd party library
from scrapy import Spider
from scrapy.http.response import Response
from scrapy.selector import Selector
from scrapy.utils.project import get_project_settings

# project
from scraper_tuto_cnrs.items import TutoCnrsItem


# #############################################################################
# ########## Classes ###############
# ##################################
class TutorialSpider(Spider):
    """Specific spider for tutorial."""

    settings = get_project_settings()
    name = "tuto_cnrs_page"
    # allowed_domains = ["stackoverflow.com"]
    start_urls = [settings.get("DEFAULT_URL_BASE") + "plan_detaille.php"]

    def parse(self, response: Response):
        """Parse URLs.

        :param Response response: HTTP response returned by URL requested
        """
        arts = Selector(response).css("article")
        logging.info(f"La page {response.url} contient {len(arts)} articles")
        for art in arts:
            # title
            art_title_section = art.css("div.title-and-meta")

            # url
            art_rel_url = art_title_section.css("h2.node__title a::attr(href)").get()

            if art_rel_url is not None:
                yield response.follow(art_rel_url, callback=self.parse_article)

        # get next page from bottom pagination to iterate over pages
        next_page = response.css("li.pager-next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_article(self, response: Response):
        """Specific parsing logic for Geotribu articles

        :param Response response: HTTP response returned by URL requested
        """
        logging.info(
            "Start parsing tutoriel : {}".format(
                response.css(
                    "html body div#wrap div#container_main_sidebar div.main h2"
                ).getall()[0]
            )
        )
        item = TutoCnrsItem()

        # contenu de la art
        art = response.css("article")[0]

        # titre
        item["title"] = art.xpath("/html/body/div/div[2]/div[2]/h2").getall()[0]
        item["body"] = art.xpath("/html/body/div/div[2]/div[2]")

        yield item


# #############################################################################
# ##### Main #######################
# ##################################
if __name__ == "__main__":
    pass

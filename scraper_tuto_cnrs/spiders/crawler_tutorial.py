#! python3  # noqa: E265

# #############################################################################
# ########## Libraries #############
# ##################################

# Standard library
import logging

# 3rd party library
from markdownify import markdownify
from scrapy import Spider
from scrapy.http.response import Response
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
        sections = response.css(
            "html body div#wrap div#container_main_sidebar div.main ol.withroman li.plandet"
        )
        logging.info(f"La page {response.url} contient {len(sections)} sections")
        for section in sections:
            section_rel_url = section.css("a::attr(href)")[0].get()

            if section_rel_url is not None:
                yield response.follow(
                    section_rel_url,
                    callback=self.parse_article,
                    cb_kwargs={"kind": "section", "order": sections.index(section)},
                )

    def parse_article(self, response: Response, kind: str, order: int):
        """Specific parsing logic for Geotribu articles

        :param Response response: HTTP response returned by URL requested
        """
        # logging.info(
        #     "Start parsing tutoriel : {}".format(
        #         response.css(
        #             "html body div#wrap div#container_main_sidebar div.main h2"
        #         ).getall()[0]
        #     )
        # )
        item = TutoCnrsItem()
        item["kind"] = kind
        item["order"] = order

        if kind == "section":
            item["title"] = response.css(
                "div.main:nth-child(2) > h1:nth-child(1)"
            ).get()
            # corps
            raw_body = response.css(
                "html body div#wrap div#container_main_sidebar div.main"
            )
            # art_out_body = []
            # for el in art_raw_body:
            #     art_out_body.append(el.get())

            item["body"] = markdownify(
                raw_body.getall()[1], default_title=True, heading_style="ATX"
            )
        else:
            item["kind"] = kind
            # item["title"] = art.xpath("/html/body/div/div[2]/div[2]/h2").getall()[0]
            # item["body"] = art.xpath("/html/body/div/div[2]/div[2]")

        yield item


# #############################################################################
# ##### Main #######################
# ##################################
if __name__ == "__main__":
    pass

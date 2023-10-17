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
        # # sections
        # sections = response.css(
        #     "html body div#wrap div#container_main_sidebar div.main ol.withroman li.plandet"
        # )
        # logging.info(f"La page {response.url} contient {len(sections)} sections")
        # for section in sections:
        #     section_rel_url = section.css("a::attr(href)")[0].get()

        #     if section_rel_url is not None:
        #         yield response.follow(
        #             section_rel_url,
        #             callback=self.parse_article,
        #             cb_kwargs={
        #                 "kind": "section",
        #                 "url_rel": section_rel_url,
        #             },
        #         )

        # tutoriels
        tutoriels = response.css(
            "html body div#wrap div#container_main_sidebar div.main ol.withroman li.plandet ol.witharabic li a"
        )
        logging.info(f"La page {response.url} contient {len(tutoriels)} tutoriels")
        for tuto in tutoriels:
            tuto_rel_url = tuto.css("a::attr(href)")[0].get()

            if tuto_rel_url is not None:
                yield response.follow(
                    tuto_rel_url,
                    callback=self.parse_article,
                    cb_kwargs={
                        "kind": "tutoriel",
                        "url_rel": tuto_rel_url,
                    },
                )

    def parse_article(self, response: Response, kind: str, url_rel: str):
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
        settings = get_project_settings()
        item = TutoCnrsItem()
        item["kind"] = kind
        item["section_number"] = url_rel.split("_")[0]
        item["page_number"] = url_rel.split("_")[1]
        item["url_rel"] = url_rel
        item["url_full"] = settings.get("DEFAULT_URL_BASE") + url_rel

        if kind == "section":
            item["title"] = response.css(
                "div.main:nth-child(2) > h1:nth-child(1)::text"
            ).get()
            # corps
            raw_body = response.css(
                "html body div#wrap div#container_main_sidebar div.main"
            )

            item["body"] = markdownify(
                raw_body.getall()[1],
                default_title=True,
                heading_style="ATX",
                escape_asterisks=False,
                escape_underscores=False,
            )
        else:
            item["title"] = response.css(
                "div.main:nth-child(2) > h2:nth-child(1)::text"
            ).get()
            # corps
            raw_body = response.css(
                "html body div#wrap div#container_main_sidebar div.main"
            )

            item["body"] = markdownify(
                raw_body.getall()[1],
                default_title=True,
                heading_style="ATX",
                escape_asterisks=False,
                escape_underscores=False,
            )

        yield item


# #############################################################################
# ##### Main #######################
# ##################################
if __name__ == "__main__":
    pass

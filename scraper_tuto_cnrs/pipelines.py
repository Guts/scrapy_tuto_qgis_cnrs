#! python3  # noqa: E265
import json
from pathlib import Path

from scrapy import Item, Spider

from scraper_tuto_cnrs.utils.slugger import sluggy

# #############################################################################
# ########## Globals ###############
# ##################################
# folder_output = Path("_output/" + datetime.now().strftime("%d%m%Y_%H%M"))
folder_output = Path("_output")
folder_output.mkdir(exist_ok=True, parents=True)


class TutoCnrsPipeline:
    def process_item(self, item: Item, spider: Spider) -> Item:
        """Process each item output by a spider. It performs these steps:

            1. Extract date handling different formats
            2. Use it to format output filename
            3. Convert content into a markdown file handling different cases

        :param GeoRdpItem item: output item to process
        :param Spider spider: Scrapy spider which is used

        :return: item passed
        :rtype: Item
        """
        # -- Common
        print(f"PIPELINE HERE: {item.get('title')}, {item.get('kind')}")

        out_filename = folder_output.joinpath(sluggy(item.get("title")) + ".md")
        out_filename.write_text(item.get("body"))


class JsonWriterPipeline:
    def open_spider(self, spider):
        out_filename = folder_output / Path("items.jl")
        self.file = out_filename.open(mode="w", encoding="UTF8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

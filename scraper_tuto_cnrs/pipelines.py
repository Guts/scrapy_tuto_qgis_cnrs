#! python3  # noqa: E265
import json
from pathlib import Path

from scrapy import Item, Spider

from scraper_tuto_cnrs.utils.slugger import sluggy

# #############################################################################
# ########## Globals ###############
# ##################################
# folder_output = Path("_output/" + datetime.now().strftime("%d%m%Y_%H%M"))
folder_output = Path("content")
folder_output.mkdir(exist_ok=True, parents=True)


def clean_title(in_title: str) -> str:
    in_title = sluggy(in_title)
    position = in_title.find("-")
    return in_title[position + 1 :]


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
        print(
            f"PIPELINE HERE: {item.get('title')}, {item.get('kind')}, {item.get('url_rel')}"
        )

        out_filename = folder_output.joinpath(
            f"{item.get('section_number')}_"
            f"{item.get('page_number')}_"
            f"{clean_title(item.get('title')).strip()}"
            f".md"
        )
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

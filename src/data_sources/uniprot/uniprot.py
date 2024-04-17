from .config import UniProtConfig
from .schema import UniProtSchema
from config import GlobalConfig
import xml.etree.ElementTree as ET


class UniProt:
    config = UniProtConfig()
    schema = UniProtSchema
    download_file_location = GlobalConfig.DATA_SOURCE_DIRECTORY + 'uniprot_sprot.xml'

    def load(self):
        data = self.download()
        cleaned_data = self.clean(data)
        self.store(cleaned_data)

    def clean(self, data):
        return

    def store(self, cleaned_data):
        print(cleaned_data)

    def download(self):
        downloader = self.config.downloader(self.config.data_source_path)
        return downloader._download()



from common.base_data_source_config import DataSourceConfig
from common.downloader import FTPDownloader


class UniProtConfig(DataSourceConfig):
    data_source_path: str = "ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz"
    downloader = FTPDownloader




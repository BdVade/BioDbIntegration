import dataclasses
from pathlib import Path



@dataclasses.dataclass
class GlobalConfig:
    EXTRACTORS = [
        'data_sources.uniprot.UniProt',
    ]
    HOME_PATH = Path(__file__).resolve().parent

    DATA_SOURCE_DIRECTORY = HOME_PATH.joinpath('datasource_downloads')
    ZIPPED_FILE_DOWNLOADS = HOME_PATH.joinpath('zipped')


from ftplib import FTP
from urllib.parse import urlparse, ParseResult
from config import GlobalConfig
import gzip
import os


class BaseDownloader:
    def __init__(self, url):
        self.parsed_url: ParseResult = urlparse(url)


class FTPDownloader(BaseDownloader):
    def __init__(self, file_url, zipped=True):
        super().__init__(file_url)
        self.zipped = zipped
        self.ftp = FTP(self.parsed_url.netloc)
        self.filename = self.parsed_url.path.split('/')[-1]
        self.file_path = "/".join(self.parsed_url.path.split('/')[:-1])
        self.ftp.login()

    def _download(self):

        print(self.file_path)
        print(self.filename)
        self.ftp.cwd(self.file_path)
        download_location = GlobalConfig.DATA_SOURCE_DIRECTORY.joinpath(self.filename)
        if os.path.exists(GlobalConfig.DATA_SOURCE_DIRECTORY):
            print("The path exists.")
        else:
            os.mkdir(GlobalConfig.DATA_SOURCE_DIRECTORY)
        #     TODO: Move this into a setup function for the entire project

        self.ftp.retrbinary("RETR " + self.filename, open(download_location, 'wb').write)
        # Close the FTP connection
        self.ftp.quit()
        if self.zipped:
            with gzip.open(download_location, 'rb') as f_in:
                # Determine the name of the extracted file
                print("unzipping")
                extracted_filename = os.path.splitext(download_location)[0]

                # Write the extracted content to a new file
                with open(extracted_filename, 'wb') as f_out:
                    f_out.write(f_in.read())

            # Remove the downloaded gzip file
            os.remove(download_location)

# ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz
#  TODO: Download to Datasources path(Single responsibility) Let the Individual Classes take it from there

downloader = FTPDownloader("ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz")

downloader._download()
from Loaders.document_loaders import TxtLoader,CsvLoader
from pathlib import Path
from Loaders.base_loader import Base
from exceptions import UnsupportedFileTypeError

class MainLoader:
    """Factory class to instantiate the appropriate file loader based on extension."""

    @staticmethod
    def choose_loader(file_path:Path) -> Base:
        extension = file_path.suffix.lower()
        if extension == '.txt':
            return TxtLoader()

        elif extension  == '.csv':
            return CsvLoader()
        else :
            raise UnsupportedFileTypeError(
                f"Unsupported file format '{extension}'. Only .txt and .csv are supported."
            )
        
from abc import ABC , abstractmethod
from pathlib import Path
class Base(ABC):
    # pass
    @abstractmethod
    def read_file(self,file_path:Path) -> str:
        pass

    @abstractmethod
    def validate_file(self,file_path:Path) -> bool:
        pass
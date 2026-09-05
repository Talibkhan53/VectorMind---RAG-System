from Loaders.base_loader import Base
from pathlib import Path
from exceptions import EmptyFileError
import csv

class TxtLoader(Base):

    def validate_file(self,file_path:Path) -> bool:
        
        if file_path.stat().st_size == 0:
                raise EmptyFileError ("File Contents is Empty")
        
        return True
     

    def read_file(self,file_path:Path) -> str:
       """Reads file content and returns it as a string."""

       with open (file_path,'r' , encoding='utf-8') as file:
          
          return file.read()

class CsvLoader(Base): 
  
  def validate_file(self,file_path:Path) -> bool:
      
      if file_path.stat().st_size == 0:
                    raise EmptyFileError ("File Contents is Empty")
      return True
     
  def read_file(self,file_path:Path) -> str:
      """Reads file content and returns it as a string."""
      formatted_str = []
      with open(file_path,'r' , encoding='utf-8') as file:
          csv_reader = csv.DictReader(file)

          for i , row in enumerate(csv_reader,start=1):
              row_str = ",".join([f"{key} : {value}" for key,value in row.items()])
              formatted_str.append(f"Row{i}->{row_str}")
      return "\n".join(formatted_str)

   



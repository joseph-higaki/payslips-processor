from pathlib import Path
import shutil
import zipfile
import yaml

def load_paths() -> tuple[str, str]:
    with open("config.yml", "r", encoding="utf-8") as ymlfile:  
        _cfg = yaml.safe_load(ymlfile)
        return _cfg["SOURCE_DIRECTORY"], _cfg["TARGET_DIRECTORY"]
    
def load_zip_pass() -> str:
    with open("pwd.yml", "r", encoding="utf-8") as ymlfile:  
        _cfg = yaml.safe_load(ymlfile)
        return _cfg["ZIP_PASS"]

if __name__ == "__main__":
    source_directory, target_directory = load_paths()
    zip_pwd = load_zip_pass()

    for zip_path in Path(source_directory).glob('*.zip'):        
        temp_dir = Path(target_directory).joinpath(zip_path.name)
        # temp_dir = C:\Users\Joseph_Higaki\Documents\Nominas\Extracted\2022-02.ZIP
        Path(temp_dir).mkdir()
        try: 
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.setpassword(zip_pwd.encode('utf-8'))
                zip_ref.extractall(temp_dir)            
                for index, pdf_path in enumerate(Path(temp_dir).glob('*.pdf')):
                    # pdf_path = C:\Users\Joseph_Higaki\Documents\Nominas\Extracted\2022-02.ZIP\xxxxx.PDF
                    # Define the new PDF file path (rename or simply move)
                    # new_pdf_path = C:\Users\Joseph_Higaki\Documents\Nominas\Extracted\2022-02.PDF
                    multiple_pdf_files_in_zip = '' if index == 0 else f'_{index}'
                    # if 0 ""
                    # if > 0 "_1"
                    new_pdf_path = Path(target_directory).joinpath(f'{zip_path.stem}{multiple_pdf_files_in_zip}.pdf')
                    # Move the PDF file to the target directory with the new name
                    shutil.move(str(pdf_path), str(new_pdf_path))
        finally:
            # Clean up the temporary extraction directory
            shutil.rmtree(temp_dir)
import requests, zipfile, io
import pathlib

def retrieve_python_dataset(url="https://docs.python.org/3.12/archives/python-3.12-docs-text.zip",
                     download_path=".",
                     dataset_path="python_dataset"):
    """
    Retrieves dataset.zip file, assuming python docs text version
    Args:
        url: Url to pull python text documentation from, defaults to 3.12 docs
        download_path: Path to download the file to
        dataset_path: Directory to unzip dataset to
    """    

    r = requests.get(url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(dataset_path)

def retrieve_zig_dataset(url="https://ziglang.org/documentation/master/",
                         download_path=".",
                         dataset_path="zig_dataset"):
    r = requests.get(url)

    path = pathlib.Path(dataset_path)
    path.mkdir(exist_ok=True, parents=True)
    
    filename = "zig_docs.html"
    filepath = path / filename

    filepath.write_text(r.text, encoding="utf-8")
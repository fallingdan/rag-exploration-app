import requests, zipfile, io

def retrieve_dataset(url="https://docs.python.org/3.12/archives/python-3.12-docs-text.zip",
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



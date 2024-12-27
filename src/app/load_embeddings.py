import os
import argparse
import utils.progress_bar as pb
import time
from utils.vectordb import VectorDb

def load(
        directory: str = None,
):
    """
    Creates embeddings for all files in a directory, walking all files and 
    subdirectories recursively. 

    Args:
        directory (str): String representing the path to the directory where 
            files should be loaded from
        verbose (bool): Set to true for extra output to the command line during
            the embedding process.
    """
    vectordb = VectorDb()

    total_files = sum(len(files) for _, _, files in os.walk(directory))
    print(f"Total Files: {total_files}")

    start_time = time.time()
    files_processed = 0

    pb.update_progress(
        progress=0,
        bar_length=80,
        time_elapsed=0
    )
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
            with open(file_path) as doc:
                vectordb.add_document(doc.read(), doc.name)
            
            files_processed += 1
            time_elapsed = time.time() - start_time
            pb.update_progress(
                progress=(files_processed / total_files), 
                bar_length=80, 
                time_elapsed=time_elapsed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog = "load_embeddings.py",
        description = "Create embeddings for all files in a directory"
    )

    parser.add_argument(
        "-d",
        "--directory",
        required = True
    )

    args = parser.parse_args()
    
    load(args.directory)
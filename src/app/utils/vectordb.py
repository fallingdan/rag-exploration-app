from chromadb import PersistentClient
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

class VectorDb:

    def __init__(self, persist_path="chromadb", collection_name="dataset_collection"):
        self.client = PersistentClient(persist_path)
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = 256,
            chunk_overlap = 20
        )
        self.collection = self.client.get_or_create_collection(collection_name)

    
    def add_document(self, document: str, filename: str):
        """
        Add a document to the vectordb, chunk it and store
        Args:
            document (str): Text document to insert into the vectordb
            filename (str): Filename to associate to document, used to build ID based on chunk
                            index as well            
        """
        chunked_document = self.text_splitter.create_documents([document])
        for index, chunk in enumerate(chunked_document):
            self.collection.upsert(
                documents=chunk.page_content, 
                ids=f"{filename}.{index}",
                metadatas={"filename": filename})


    def retrieve_results(self, query: str, n_results: int = 10):
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
        )

        return results
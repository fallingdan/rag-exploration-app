from chromadb import PersistentClient

class VectorDb:

    def __init__(self, persist_path="../chromadb", collection_name="dataset_collection"):
        self.client = PersistentClient(persist_path)
        self.collection_name = collection_name

    def add_document(self, document: str, id: str, metadata: dict):
        """
        Add a document to the vectordb
        Args:
            document (str): Text document to insert into the vectordb
            id (str): Id to associate document to
            metadata (dict): Dictionary of metadata to attach to the document
        """
        
        collection = self.client.get_or_create_collection(self.collection_name)
        collection.upsert(documents=document, metadatas=metadata, ids=id)
        


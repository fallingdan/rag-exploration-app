import argparse
from utils.vectordb import VectorDb
import google.generativeai as genai
import os

def main(vectordb_path: str):
    
    vectordb = VectorDb(persist_path=vectordb_path)

    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")

    print("Type 'quit' to exit")
    print("Input your query after the >>>")

    while True:
        question = input(">>> ")

        if question == "quit":
            break

        results = vectordb.retrieve_results(query=question, n_results=30)

        prompt = f"""
        DOCUMENTS:
        {results["documents"]}

        QUESTION:
        {question}

        INSTRUCTIONS:
        Answer the users QUESTION using the DOCUMENTS.
        Keep your answer based on the DOCUMENTS only.
        If the DOCUMENTS don't contain the facts to answer the question, say I DONT KNOW. 
        If you use your prior knowledge to answer the question, say I CHEATED. 
        """

        response = model.generate_content(prompt)

        print(response.text)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d",
        "--directory"
    )

    args = parser.parse_args()

    main(args.directory)
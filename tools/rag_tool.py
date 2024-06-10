from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()

class RAGTool():

    @tool("answer the query from document using vector database")
    def rag_search_tool(user_question):

        'To find answer from vector database using RAG. Document contains JJM guidelines.'

        prompt_template = """
            Answer the question as detailed as possible from the provided context, make sure to provide all the details.\n\n
            Context:\n {context}?\n
            Question: \n{question}\n

            Answer:
            """
        
        model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.3)
        prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
        chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
        embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
        new_db = FAISS.load_local("faiss_index", embeddings,allow_dangerous_deserialization=True)
        docs = new_db.similarity_search(user_question)

        response = chain({"input_documents":docs, "question": user_question}, return_only_outputs=True)
        return response['output_text']       
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled
from transcript_video import video_transcript
from dotenv import load_dotenv

load_dotenv()
transcript = video_transcript()

splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = splitter.create_documents([transcript])

# print(len(chunks))

# print(chunks[100])
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


# -------------------------
# 1. Hugging Face Embeddings
# -------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -------------------------
# 2. Create FAISS Vector Store
# -------------------------

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)

print(vector_store.index_to_docstore_id)


# -------------------------
# 3. OpenRouter LLM
# -------------------------

llm = ChatOpenAI(
    model="openai/gpt-oss-20b:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)

# -------------------------
# 4. Retriever
# -------------------------

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

print(retriever)
# -------------------------
# 5. Test Retriever
# -------------------------

docs = retriever.invoke("What is DeepMind?")

prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)
question          = "is the topic of nuclear fusion discussed in this video? if yes then what was discussed"
retrieved_docs    = retriever.invoke(question)

# print(retrieved_docs)
context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt = prompt.invoke({"context": context_text, "question": question})
# print(final_prompt)

answer = llm.invoke(final_prompt)
# print(answer.content)

from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text

parallel_chain = RunnableParallel({
    'context': retriever | RunnableLambda(format_docs),
    'question': RunnablePassthrough()
})
print(parallel_chain.invoke('who is Demis'))
parser = StrOutputParser()

main_chain = parallel_chain | prompt | llm | parser

print(main_chain.invoke('Can you summarize the video'))
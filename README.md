# Medical RAG Chatbot (Diabetes Domain)

A Retrieval-Augmented Generation (RAG) chatbot for answering medical questions on diabetes using PubMed data, FAISS vector search, and LLM-based generation.

## Evaluation - LLM as Judge: ChatGPT

| Metric                    | Score    | Notes                                                                                                                                                        |
| ------------------------- | ------------   | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Relevance**             | 10             | Every part of the answer is supported by the context.                                                                                                        |
| **Completeness**          | 9              | Covers diabetes mellitus, neonatal diabetes, and CDI; could better separate type 1 vs type 2 causes.                                                         |
| **Accuracy**              | 9              | Correct per context; minor phrasing could be sharper (“impaired insulin secretion and/or action” instead of “deficiency in insulin production or function”).   |
| **Clarity / Conciseness** | 9              | Structured and readable; “Note” could be integrated more smoothly.                                                                                           |
## 📊 Notebook Comparison: Industrial vs. My Implementation

This table highlights the key differences between the original **JohnSnowLabs Medical Chatbot RAG** notebook i used as reference and **My Implementation** (`usage.ipynb`), built as part of an internship application.

---

## 🔍 Feature-by-Feature Comparison

| Aspect | 🏭 Original (JohnSnowLabs) | 🔁 My Implementation (`usage.ipynb`) |
|---|---|---|
| **Scale & Complexity** | 106 cells — full industrial pipeline | 21 cells — focused, clean reproduction |
| **Framework / Stack** | JohnSnowLabs (`johnsnowlabs`) + Apache Spark + LangChain | LangChain Community + HuggingFace + Groq |
| **Execution Environment** | Apache Spark cluster (distributed computing) | Google Colab (T4 GPU) |
| **Text Splitter** | `JohnSnowLabsLangChainCharSplitter` (Spark-NLP) | `RecursiveCharacterTextSplitter` (LangChain) |
| **Embedding Model** | `JohnSnowLabsLangChainEmbedder` (`en.embed_sentence.instructor_base`) | HuggingFace `BAAI/bge-large-en-v1.5` (GPU) |
| **Vector Store** | FAISS (built or loaded from pre-built `.vs` zip) | FAISS (built or loaded pre-built from `.src` folder) |
| **Retrieval Strategy** | FAISS (similarity, MMR, score threshold, filter) + BM25 + Ensemble | FAISS with MMR (`k=4`, `fetch_k=10`, `lambda_mult=0.75`) |
| **LLM Used** | OpenAI `gpt-3.5-turbo-16k` / Llama-2 / Zephyr-7B | Groq API (`QWEN3 32B` model — fast inference) |
| **Prompt Engineering** | Custom `PromptTemplate` with source citation | Custom `ChatPromptTemplate` with structured template |
| **Dataset** | PubMed Diabetes (1000 abstracts) + EPFL Clinical Guidelines (100 entries) | PubMed Diabetes (1000 abstracts) |
| **Data Loader** | `PySparkDataFrameLoader` (Spark DataFrame) | `DataFrameLoader` (Pandas DataFrame) |
| **Retriever Types** | FAISS, BM25, Ensemble, MMR, score-threshold, metadata-filtered | FAISS with MMR |
| **Long Context Handling** | `LongContextReorder` to mitigate "lost in the middle" issue | Not implemented |
| **Evaluation** | No formal evaluation section | LLM-as-Judge evaluation using ChatGPT (Relevance, Completeness, Accuracy, Clarity) |
| **Modular Code** | Monolithic notebook cells | Modular `src/` package (`preprocessing.py`, `vector.py`, `ask_rag.py`) |
| **Reproducibility** | Requires JohnSnowLabs license + Spark setup | Fully open-source, runs on free Colab GPU and Groq API |
| **Speed Benchmarking** | CPU vs. GPU embedding speed comparison (HuggingFace vs JSL) | Not benchmarked |

---

## What this project does?

This project implements an end-to-end RAG pipeline for medical question answering:

**- Loads PubMed diabetes dataset**

**- Splits documents into chunks**

**- Generates embeddings using BGE-small**

**- Stores vectors in FAISS**

**- Retrieves relevant context using MMR**

**- Uses LLM (QWEN3 32B) for answer generation**

**- Evaluated outputs using LLM-as-a-judge**

## Architecture:

### User Query
```bash
query = "What are the causes of diabetes?"
```
### Retriever 
```bash
retriever = vector_store.as_retriever(search_type = "mmr", k = 4, fetch_k = 10, lambda_mult = 0.75)
```
### Top-K Context (FAISS + MMR)
```bash
context = retrieve(query, retriever)
```
### Prompt Template
```bash
template = """your template here"""
```
### LLM (QWEN3 32B)
```bash
ask_rag(query, retriever, template, client, model)
```  
### Final Answer
```yaml
The causes of diabetes include:  
1. Diabetes mellitus: Deficiency in insulin production or function (leading to glucose, protein, and lipid metabolic disorders), as seen in type 1 and type 2 diabetes.  
2. Neonatal diabetes: Genetic mutations affecting pancreatic beta cell function.  
3. Central diabetes insipidus (CDI): Trauma to the pituitary, hypoperfusion, malignancy, or transient cases linked to vasopressin use/withdrawal.  

Note: The context distinguishes between diabetes mellitus (glucose disorders) and diabetes insipidus (fluid balance disorders).
```

# Medical RAG Chatbot (Diabetes Domain)

A Retrieval-Augmented Generation (RAG) chatbot for answering medical questions on diabetes using PubMed data, FAISS vector search, and LLM-based generation.


<img width="662" height="481" alt="image" src="https://github.com/user-attachments/assets/9468e893-f9b5-4473-9e62-5325471be2dc" />


## What this project does?

This project implements an end-to-end RAG pipeline for medical question answering:

**- Loads PubMed diabetes dataset**

**- Splits documents into chunks**

**- Generates embeddings using BGE-small**

**- Stores vectors in FAISS**

**- Retrieves relevant context using MMR**

**- Uses LLM (Groq LLaMA 3.1) for answer generation**

**- Evaluates outputs using LLM-as-a-judge**

## Architecture:

### User Query
```bash
query = "What are the causes of diabetes?"
```
### Retriever 
```bash
retriever = vector_store.as_retriever(search_type = "mmr", k = 4, fetch_k = 8, lambda_mult = 0.3)
```
### Top-K Context (FAISS + MMR)
```bash
context = retrieve(query, retriever)
```
### Prompt Template
```bash
template = """your template here"""
```
### LLM (Groq - LLaMA 3.1)
```bash
ask_rag(query, retriever, template, client, model)
```  
### Final Answer
```bash
Diabetes mellitus, commonly referred to as diabetes, is a combination of many metabolic diseases. It is caused by insulin deficiency in the body, where insulin is one of the most well-studied proteins.

Information mentioned:
- Diabetes mellitus
- Combination of many metabolic diseases
- Main cause: insulin deficiency
- Diabetes mellitus is also referred to as diabetes
```

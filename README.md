# Medical RAG Chatbot (Diabetes Domain)

A Retrieval-Augmented Generation (RAG) chatbot for answering medical questions on diabetes using PubMed data, FAISS vector search, and LLM-based generation.

## Evaluation - LLM as Judge: ChatGPT

| Metric                    | Score    | Notes                                                                                                                                                        |
| ------------------------- | ------------   | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Relevance**             | 10             | Every part of the answer is supported by the context.                                                                                                        |
| **Completeness**          | 9              | Covers diabetes mellitus, neonatal diabetes, and CDI; could better separate type 1 vs type 2 causes.                                                         |
| **Accuracy**              | 9              | Correct per context; minor phrasing could be sharper (“impaired insulin secretion and/or action” instead of “deficiency in insulin production or function”).   |
| **Clarity / Conciseness** | 9              | Structured and readable; “Note” could be integrated more smoothly.                                                                                           |


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

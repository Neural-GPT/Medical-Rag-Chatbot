def retrieve(query, retriever):
  docs = retriever.invoke(query)
  return [doc.page_content for doc in docs]
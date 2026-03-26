def split_docs(docs, split, chunk_size, chunk_overlap):
  splitter = split(chunk_size = chunk_size, chunk_overlap = chunk_overlap, length_function = len)
  text = splitter.split_documents(docs)

  print(f"Total document chunks created: {len(text)}")
  return text
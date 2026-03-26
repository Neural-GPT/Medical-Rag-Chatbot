def load_data(path, loader):

  import pandas as pd
  
  data = pd.read_csv(path)
  loader = loader(data, page_content_column = "abstract")
  documents = loader.load()

  return documents


def split_docs(docs, split, chunk_size, chunk_overlap):
  splitter = split(chunk_size = chunk_size, chunk_overlap = chunk_overlap, length_function = len)
  text = splitter.split_documents(docs)

  print(f"Total document chunks created: {len(text)}")
  return text

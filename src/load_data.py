def load_data(path, loader):

  import pandas as pd
  
  data = pd.read_csv(path)
  loader = loader(data, page_content_column = "abstract")
  documents = loader.load()

  return documents
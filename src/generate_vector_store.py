def generate_vector_store(generator, vector_db_path, text, type_):

  import os

  if os.path.exists(vector_db_path):
    vector_store = type_.load_local(vector_db_path, generator, allow_dangerous_deserialization = True)

  else:
    vector_store = type_.from_documents(text, generator)
    vector_store.save_local(vector_db_path)

  return vector_store
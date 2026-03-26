def ask_rag(query, retriever, llm, template):

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    formatted_prompt = template.format(
        context=context,
        question=query
    )

    response = llm(formatted_prompt)

    return response
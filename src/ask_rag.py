def llm(client, prompt, model):
    response = client.chat.completions.create(
        model= model,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content

def ask_rag(query, retriever, template, client, model):
    
    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    formatted_prompt = template.format(
        context=context,
        question=query
    )

    response = llm(client, formatted_prompt, model)

    return response

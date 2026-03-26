def llm(client, prompt, model):
    response = client.chat.completions.create(
        model= model,
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content
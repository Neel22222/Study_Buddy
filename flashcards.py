def generate_flashcards(client, text):

    prompt = f"""
    Create flashcards from:

    {text}

    Format:

    Q:
    A:
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
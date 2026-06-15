def generate_quiz(client, text):

    prompt = f"""
    Create 5 MCQs from:

    {text}

    Include answers at the end.
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
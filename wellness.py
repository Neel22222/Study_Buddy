def wellness_chat(client, user_input):

    prompt = f"""
    You are a friendly student wellness assistant.

    Help students with:
    - Stress management
    - Study motivation
    - Time management
    - Exam anxiety
    - Productivity tips

    User Message:
    {user_input}

    Give supportive and practical advice.
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
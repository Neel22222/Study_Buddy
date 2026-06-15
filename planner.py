def generate_plan(client, syllabus, days):

    prompt = f"""
    Create a study plan.

    Syllabus:
    {syllabus}

    Number of days:
    {days}

    Divide topics evenly.
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
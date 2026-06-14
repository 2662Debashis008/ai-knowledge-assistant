def build_prompt(
        question,
        contexts
):

    context_text = "\n\n".join(
        contexts
    )

    prompt = f"""
You are an AI Knowledge Assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
say:

"I could not find the answer in the knowledge base."

Context:

{context_text}

Question:

{question}

Answer:
"""

    return prompt
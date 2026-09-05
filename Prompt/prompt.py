class PromptBuilder:

    def build(self, question, context):

        prompt = f"""
You are a helpful assistant.

Answer the question using ONLY the provided context.

If the answer cannot be found in the context,
say that the information is not available.

Context:
{context}

Question:
{question}

Answer:
"""

        return prompt
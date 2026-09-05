# from Loaders.main_loader import MainLoader
from pathlib import Path

class Chunking:
    def sliding_chunk(self,text:str,chunk_size:int = 10,overlap:int = 5) ->list[str]:
        """Splits raw text into overlapping word-based chunks."""
        # 1. Convert raw text string into a list of words
        words = text.split()
        chunks = []

        # Edge case: If text is shorter than chunk_size, return it whole
        if len(words) <= chunk_size:
            return [text]

        step = chunk_size - overlap
        i = 0

         # 2. Slide across the word list
        while i < len(words):
            # Slice words and join back into a single readable string
            chunk_words = words[i:i+chunk_size]
            chunk_text = " ".join(chunk_words)
            chunks.append(chunk_text)

            i += step

        return chunks

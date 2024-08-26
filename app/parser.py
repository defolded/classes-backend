import os
from llama_parse import LlamaParse

async def parse_transcript(transcript_path: str):
    parser = LlamaParse(
        api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
        result_type="text",  # "markdown" and "text" are available
        verbose=True,
    )

    documents = await parser.aload_data(transcript_path)

    return documents

from llama_parse import LlamaParse
import nest_asyncio
import os
from dotenv import load_dotenv
from llama_parse import LlamaParse

nest_asyncio.apply()
load_dotenv()

parser = LlamaParse(
    api_key=os.getenv("LLAMA_CLOUD_API_KEY"),
    result_type="text",  # "markdown" and "text" are available
    verbose=True,
)
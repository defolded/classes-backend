# College Course Scheduler Backend

This is the backend component of a college course scheduling and graduation planning chat-bot. The backend is built with FastAPI and integrates with LLaMA-based language models to assist students in generating course schedules and determining which courses they need to complete their degree.

## Features

- **Retrieval-Augmented Generation (RAG):** Utilizes RAG to provide context-aware responses based on the student's course history.
- **PDF Transcript Parsing:** Students can upload their transcript in PDF format, which is parsed and integrated into the context for accurate planning.
- **Vector Database:** Utilizes a vector database (Chroma) for efficient information retrieval based on the student's queries.
- **Advanced Querying Techniques:** Employs techniques such as prompt chaining to optimize the interaction with the language model.

## Installation

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/installation/)

### Install Dependencies

First, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/yourusername/college-course-scheduler-backend.git
cd college-course-scheduler-backend
```

### Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Install the required Python packages:

Create a .env file in the root of the project to store LlamaCloud API key:

```text
LLAMA_CLOUD_API_KEY=your_llama_cloud_api_key
```

### Populate vector database for RAG

```bash
python app/populate_database.py --reset
```

### Run the Database

```bash
python app/populate_database.py --reset
```

The database should be running on http://127.0.0.1:8000.

### Run the Server

```bash
uvicorn app.main:app --reload --port 8001
```

The database should be running on http://127.0.0.1:8001.

## API Endpoints

### POST /generate

This endpoint accepts a prompt and an optional PDF transcript. It generates a response based on the student's course history and the provided context.

**Request:**

- `prompt`: The text prompt for the chat-bot (required).
- `file`: The PDF transcript file (optional).

**Response:**

```json
{
  "content": "Generated response based on the student's courses and provided context."
}
```

## Project Structure

- `app/`: Contains the main application code.
  - `main.py`: The entry point of the FastAPI application.
  - `routes.py`: Defines the API routes and handles requests.
  - `model.py`: Manages the interaction with the language model and the vector database.
  - `parse.py`: Handles the parsing of uploaded PDF transcripts.
  - `get_embedding_function.py`: Returns the embedding function used for similarity search.
- `data/`: Directory where uploaded transcripts and other data are stored

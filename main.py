import hashlib
from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Import the generator functions from our other file
from babel_generator import generate_book_content, generate_page_content


# --- API Data Models (using Pydantic) ---

class Page(BaseModel):
    page_number: int = Field(..., gt=0, le=410, description="The page number, from 1 to 410.")
    lines: List[str]


class Book(BaseModel):
    address_hash: str
    content: List[Page]


class SearchRequest(BaseModel):
    text: str = Field(..., min_length=1, description="The text to find the address of.")


class SearchResponse(BaseModel):
    address_hash: str
    query_text: str


# --- FastAPI Application ---

app = FastAPI(
    title="Babel Hash API",
    description="A deterministic interface to a combinatorial universe.",
)


# --- CORS Middleware ---
# This section allows your front-end website to make requests to your API.

origins = [
    "*",  # Allows all origins, which is fine for a public API.
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


# --- API Endpoints ---

@app.get("/")
def read_root():
    """Provides a welcome message for the root URL."""
    return {"message": "Welcome to the Babel Hash API! Go to /docs to explore the endpoints."}


@app.get("/book/{hash_str}", response_model=Book)
def get_full_book(hash_str: str):
    """
    Retrieves a full, 410-page book by its 256-bit SHA256 hash.
    """
    if len(hash_str) != 64:
        raise HTTPException(status_code=400, detail="Invalid hash format. Must be a 64-character hex string.")

    content = generate_book_content(hex_hash=hash_str)
    return {"address_hash": hash_str, "content": content}


@app.get("/page/{hash_str}/{page_num}", response_model=Page)
def get_single_page(hash_str: str, page_num: int):
    """
    Retrieves a single page from a book to save bandwidth.
    """
    if len(hash_str) != 64:
        raise HTTPException(status_code=400, detail="Invalid hash format. Must be a 64-character hex string.")
    if not (1 <= page_num <= 410):
        raise HTTPException(status_code=400, detail="Page number must be between 1 and 410.")

    lines = generate_page_content(hex_hash=hash_str, page_num=page_num)
    return {"page_number": page_num, "lines": lines}


@app.post("/search", response_model=SearchResponse)
def search_for_text_address(request: SearchRequest):
    """
    Computes the unique address (SHA256 hash) for a given block of text.
    This demonstrates the 'inverted search' paradigm.
    """
    # Encode the text to bytes, which is required for hashing
    text_bytes = request.text.encode('utf-8')

    # Calculate the SHA256 hash and get its hex representation
    readable_hash = hashlib.sha256(text_bytes).hexdigest()

    return {"address_hash": readable_hash, "query_text": request.text}
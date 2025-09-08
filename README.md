# Babel Hash API


A deterministic API and web portal for exploring a computational version of Jorge Luis Borges's "The Library of Babel." This project transforms the library from an impossible physical space into a navigable mathematical one.

**Live Demo:** [https://jalpan04.github.io/BabelHashAPI/](https://jalpan04.github.io/BabelHashAPI/)

---



### The Concept

In Borges's story, the Library contains every possible book, making it a universe of information but also of complete chaos. The librarians are lost, searching for meaning.

This API solves the library's central paradox not by **searching**, but by **computation**. Any text you can imagine already has a fixed, calculable address (a cryptographic hash). The API acts as a perfect index, capable of generating any book from its unique address on demand, without storing a single one.

### Key Features

* **🔍 Search by Text**: Calculate the unique address (SHA-256 hash) for any piece of text.
* **📖 View by Address**: Retrieve and view the contents of any page from any book using its hash.
* **🌌 Explore Randomly**: Discover a random page from a random book in the library with a single click.
* **✅ Fully Tested**: Includes a comprehensive test suite using `pytest` to verify both internal logic and API endpoints.
* **🚀 Live Deployment**: The backend is deployed on Render and the front-end is hosted on GitHub Pages.

### Technology Stack

* **Backend**: Python, FastAPI
* **Testing**: Pytest
* **Deployment**: Render (API), GitHub Pages (Website)
* **Frontend**: HTML, CSS, JavaScript (no frameworks)

### How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Jalpan04/BabelHashAPI.git](https://github.com/Jalpan04/BabelHashAPI.git)
    cd BabelHashAPI
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the FastAPI server:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://127.0.0.1:8000`.

### API Endpoints

| Method | Path                               | Description                                     |
| :----- | :--------------------------------- | :---------------------------------------------- |
| `GET`  | `/`                                | Displays a welcome message.                     |
| `POST` | `/search`                          | Calculates the hash for a given block of text.  |
| `GET`  | `/page/{hash_str}/{page_num}`      | Retrieves a specific page from a specific book. |
| `GET`  | `/book/{hash_str}`                 | Retrieves a full book (computationally heavy).  |

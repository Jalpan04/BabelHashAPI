import random

# --- Constants defining the Library's structure ---
# The 25 symbols allowed in any book
BABEL_ALPHABET = "abcdefghilmnoprstuwxyz,.' "
CHARS_PER_LINE = 80
LINES_PER_PAGE = 40
PAGES_PER_BOOK = 410
TOTAL_CHARS_PER_BOOK = CHARS_PER_LINE * LINES_PER_PAGE * PAGES_PER_BOOK

def generate_book_content(hex_hash: str) -> list[dict]:
    """Generates the full content of a book from a hex hash."""

    # 1. Use the hash to create a deterministic seed
    # We convert the hexadecimal hash string into an integer
    seed = int(hex_hash, 16)

    # 2. Seed the random number generator
    # This ensures that the same hash ALWAYS produces the same sequence of numbers
    prng = random.Random(seed)

    # 3. Generate all characters for the book in one go
    book_chars = []
    for _ in range(TOTAL_CHARS_PER_BOOK):
        # Get a random index from 0 to 24
        random_index = prng.randint(0, len(BABEL_ALPHABET) - 1)
        # Append the character at that index to our list
        book_chars.append(BABEL_ALPHABET[random_index])

    # 4. Structure the flat list of characters into pages and lines
    full_content = []
    char_index = 0
    for page_num in range(1, PAGES_PER_BOOK + 1):
        page_lines = []
        for _ in range(LINES_PER_PAGE):
            line_start = char_index
            line_end = line_start + CHARS_PER_LINE
            line = "".join(book_chars[line_start:line_end])
            page_lines.append(line)
            char_index = line_end

        full_content.append({"page_number": page_num, "lines": page_lines})

    return full_content

def generate_page_content(hex_hash: str, page_num: int) -> list[str]:
    """Generates a single page to avoid creating the whole book."""

    seed = int(hex_hash, 16)
    prng = random.Random(seed)

    # Calculate how many characters to "throw away" to get to the desired page
    chars_to_skip = (page_num - 1) * LINES_PER_PAGE * CHARS_PER_LINE

    # Fast-forward the generator by generating (but not storing) the skipped characters
    for _ in range(chars_to_skip):
        prng.randint(0, len(BABEL_ALPHABET) - 1) # This advances the PRNG's state

    # Now, generate the characters for the target page
    page_lines = []
    for _ in range(LINES_PER_PAGE):
        line_chars = []
        for _ in range(CHARS_PER_LINE):
            random_index = prng.randint(0, len(BABEL_ALPHABET) - 1)
            line_chars.append(BABEL_ALPHABET[random_index])
        page_lines.append("".join(line_chars))

    return page_lines
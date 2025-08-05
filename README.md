# Random_Books_Info_Viewer


## Books Info Retriever
- This python script fetches and displays random book data using the Free API from api.freeapi.app in CLI/TERMINAL.
- It's designed for quick demos and learning purposes around API consumption.

## Features

- Retrieves random books info
- Shows book name, published date, author, etag, book-id
- Includes basic error handling for connection issues

## Requirements

- Python 3.x (x = 9 or 9+)
- requests library (`pip install requests`)

## How to Use

1. Run the script with: `python script_name.py`
   (Replace `script_name.py` with your actual filename)
2. The script will print random book information from the API.
3. If the API fails or internet is unavailable, an exception is raised:
   `"failed, to fetch book data  "`

## API Details

- Source: FreeAPI – https://api.freeapi.app
- Endpoint: `https://api.freeapi.app/api/v1/public/stocks/stock/random`
- This is a demo API and the data is randomly generated for learning/testing.

## Output like this:

- BOOK NAME: C Programming Language
- AUTHOR: Brian W. Kernighan & Dennis Ritchie
- BOOK PUBLISHED: 1988-03-22
- E-Tag: uuTUtEuds1o
- BOOK-ID: 73

## About

A minimal and practical script created to demonstrate how to consume REST APIs in Python using the requests module.

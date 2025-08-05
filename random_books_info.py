import requests


def get_random_books():
    url = "https://api.freeapi.app/api/v1/public/books/book/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        bookdata = data["data"]
        book_name = bookdata["volumeInfo"] ["title"]
        book_writer_name = bookdata["volumeInfo"] ["authors"]
        book_etag = bookdata["etag"]
        book_id = bookdata["id"]
        book_published_date = bookdata["volumeInfo"]  ["publishedDate"]

        return book_name, book_writer_name, book_etag, book_id, book_published_date
    else:
        raise Exception("Failed, to fetch BOOK data")

def main():
    try:
        book_name, book_writer_name, book_etag, book_id, book_published_date = get_random_books()
        if isinstance(book_writer_name, list):
            book_writer_name = " & ".join(book_writer_name)
        print(f"\nBOOK NAME: {book_name} \nAUTHOR: {book_writer_name} \nBOOK PUBLISHED: {book_published_date} \nE-Tag: {book_etag} \nBOOK-ID: {book_id}")
    except Exception as q:
        print(str(q))

if __name__ == "__main__":
    main()

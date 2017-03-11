from system.core.model import Model
class Book(Model):
    def __init__(self):
        super(Book, self).__init__()

    def get_recent_reviews(self):
        reviews_query = "SELECT reviews.id as review_id, reviews.content, reviews.rating, books.title, books.id as book_id, users.id as user_id, reviews.created_at, users.name  FROM reviews JOIN users ON reviews.user_id = users.id JOIN books ON reviews.book_id = books.id ORDER BY reviews.created_at DESC LIMIT 3;"
        reviews = self.db.query_db(reviews_query)

        books_query = "SELECT DISTINCT books.title, books.id FROM books JOIN reviews ON books.id = reviews.book_id"
        books = self.db.query_db(books_query)

        print books
        return {"reviews": reviews, "books": books}

    def get_authors(self):
        authors_query = "SELECT * FROM authors"
        authors = self.db.query_db(authors_query)
        return authors

    def create_author(self, info):
        author_query = "INSERT INTO authors (name, created_at, updated_at) VALUES ('{}',NOW(),NOW())".format(info)
        self.db.query_db(author_query)

    def create(self, info):

        book_query = "INSERT INTO books (title, author_id, created_at, updated_at) VALUES ('{}','{}',NOW(),NOW())".format(info['book_title'], info['author_id'])
        self.db.query_db(book_query)

        get_book_query = "SELECT * FROM books ORDER BY id DESC LIMIT 1"
        books = self.db.query_db(get_book_query)
        currbook_id = books[0]['id']

        review_query = "INSERT INTO reviews (content, rating, user_id, book_id, created_at, updated_at) VALUES ('{}', '{}', '{}', '{}', NOW(), NOW())".format(info['review_content'], info['rating'], info['user_id'], currbook_id)
        self.db.query_db(review_query)

        return currbook_id


    def show_book(self, bookid):

        get_book_query = "SELECT books.id, books.title, authors.name AS author FROM books JOIN authors ON books.author_id = authors.id WHERE books.id = {}".format(bookid)
        books = self.db.query_db(get_book_query)
        currbook_id = books[0]['id']

        get_reviews = "SELECT reviews.content, reviews.id, reviews.created_at, reviews.rating, reviews.user_id, users.name, users.id AS user_id FROM reviews JOIN books ON reviews.book_id = books.id JOIN users ON reviews.user_id = users.id WHERE books.id = {}".format(currbook_id)
        reviews = self.db.query_db(get_reviews)

        return {"book": books[0], "reviews":reviews}

    def create_review(self, info):

        review_query = "INSERT INTO reviews (content, rating, user_id, book_id, created_at, updated_at) VALUES ('{}','{}','{}','{}', NOW(), NOW())".format(info['content'], info['rating'], info['user_id'], info['book_id'])
        self.db.query_db(review_query)

    def delete_review(self, id):

        review_query = "DELETE FROM reviews WHERE id = {}".format(id)
        self.db.query_db(review_query)

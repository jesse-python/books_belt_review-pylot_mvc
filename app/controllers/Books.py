from system.core.controller import *
class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)

        self.load_model('Book')

    def index(self):
        data = self.models['Book'].get_recent_reviews()
        return self.load_view('books/index.html', reviews=data['reviews'], books=data['books'])

    def new(self):
        authors = self.models['Book'].get_authors()
        return self.load_view('books/new.html', authors=authors)

    def create_author(self):
        self.models['Book'].create_author(request.form['name'])
        return redirect('/books/new')

    def create(self):
        print request.form

        info = {
            "book_title": request.form['title'],
            "author_id": request.form['author'],
            "review_content": request.form['review'],
            "user_id": session['id'],
            "rating": request.form['rating'],
        }

        bookid = self.models['Book'].create(info)

        print bookid
        return redirect('/books/'+str(bookid))

    def show(self, id):

        data = self.models['Book'].show_book(id)

        return self.load_view('books/show.html', book=data['book'], reviews=data['reviews'])

    def create_review(self):
        print request.form

        info = {
            "content": request.form['content'],
            "rating": request.form['rating'],
            "book_id": request.form['book_id'],
            "user_id": session['id'],
        }

        self.models['Book'].create_review(info)

        return redirect('/books/'+str(request.form['book_id']))

    def destroy_review(self, id):

        self.models['Book'].delete_review(id)

        return redirect('/books/'+str(request.form['book_id']))

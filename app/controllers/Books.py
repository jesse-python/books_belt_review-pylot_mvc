from system.core.controller import *
class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)

        self.load_model('Book')

    def index(self):
        return self.load_view('books/index.html')

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
        return redirect('/books/'+str(bookid)+'/')

    def show(self, id):

        data = self.models['Book'].show_book(id)

        return self.load_view('books/show.html', book=data['book'], reviews=data['reviews'])

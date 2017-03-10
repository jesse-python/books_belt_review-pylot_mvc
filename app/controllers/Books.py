from system.core.controller import *
class Books(Controller):
    def __init__(self, action):
        super(Books, self).__init__(action)

        self.load_model('Book')

    def index(self):
        return self.load_view('books/index.html')

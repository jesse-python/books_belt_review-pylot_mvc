from system.core.controller import *
class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')

    def index(self):
        # if session:
        #     return redirect('/books')
        return self.load_view('users/index.html')

    def create(self):

        user_info = {
            "name": request.form['name'],
            "email": request.form['email'],
            "alias": request.form['alias'],
            "password": request.form['password'],
            "pw_confirmation": request.form['pw_confirmation'],
        }

        create_status = self.models['User'].create_user(user_info)
        if create_status['status'] == True:
            session['id'] = create_status['user']['id']
            session['name'] = create_status['user']['name']
            # print "user now in session"
            return redirect('/books')
        else:
            for message in create_status['errors']:
                print "errors working"
                flash(message, 'regis_errors')
            return redirect('/')

    def login(self):

        user_info = {
            "email": request.form['email'],
            "password": request.form['password']
        }

        login_status = self.models['User'].login_user(user_info)
        if login_status['status'] == True:
            session['id'] = login_status['user']['id']
            session['name'] = login_status['user']['name']
            return redirect('/books')
        else:
            for message in login_status['errors']:
                flash(message, 'login_errors')
            return redirect('/')

    def logout(self):
        session.pop('name')
        session.pop('id')
        flash("You are now logged out", 'logout')
        return redirect('/')

    def show(self, id):

        data = self.models['User'].show_user(id)

        
        return self.load_view('users/show.html', user=data['user'], reviews=data['reviews'])

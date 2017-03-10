from system.core.controller import *
class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')

    def index(self):
        return self.load_view('users/index.html')

    def create(self):

        user_info = {
            "name": request.form['name'],
            "email": request.form['email'],
            "alias": request.form['alias'],
            "password": request.form['password'],
            "pw_confirmation": request.form['pw_confirmation'],
        }

        print user_info

        create_status = self.models['User'].create_user(user_info)
        if create_status['status'] == True:
            session['id'] = create_status['user']['id']
            session['name'] = create_status['user']['name']
            print "user now in session"
            # return redirect('/books')
        else:
            for message in create_status['errors']:
                print "errors working"
                flash(message, 'regis_errors')
            return redirect('/')

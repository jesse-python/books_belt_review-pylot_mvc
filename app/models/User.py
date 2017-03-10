from system.core.model import Model
import re
class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def create_user(self, info):

        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')

        errors = []

        # print "user model working, validate now"
        if not info['name']:
            errors.append('Name cannot be blank')
        elif len(info['name']) < 2:
            errors.append('Name must be at least 2 characters long!')

        if not info['alias']:
            errors.append('Alias cannot be blank')

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid')

        if not info['password']:
            errors.append('Password must not be blank')
        elif len(info['password']) < 8:
            errors.append('Password must be greater than 8 characters')
        elif info['password'] != info['pw_confirmation']:
            errors.append('Password and password confirmation do not match')

        if errors:
            return {'status': False, "errors": errors}
        else:
            password = info['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            create_query = "INSERT INTO users (name, alias, email, password, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW())"
            create_data = [info['name'], info['alias'], info['email'], hashed_pw]
            self.db.query_db(create_query, create_data)

            qet_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return {"status": True, "user": users[0]}
            
    # def login_user(self, info):
    #     password = info['password']
    #     user_query = "SELECT * FROM users WHERE email = %s LIMIT 1"
    #     user_data = [info['email']]
    #     users = self.db.query_db(user_query, user_data)
    #     if users[0]:
    #         if self.bcrypt.check_password_hash(users[0]['password'], password):
    #             return users[0]
    #     return False

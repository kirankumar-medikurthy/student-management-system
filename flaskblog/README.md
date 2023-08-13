# student-management-system

# creating a databe from terminal commands

- Go the current flask project directory
- type 'python 3'
- type this command from studentManagement import app,db
- type app.app_context().push()
- db.create_all()
- from studentManagement import User, Post
- user1 = User(username="kiran",email='kiran@gmail.com', password="password")
- db.session.add(user1)
- db.session.commit();
- User.query.all()
- User.query.first()
- User.query.filter_by(username="guru").all()
- User.query.filter_by(username="guru").first();
- user = User.query.filter_by(username="guru").first();
    -  user.id
- user = User.query.get(1);
- user.posts
-  post1 = Post(title="Blog 1", content="welcome to the flask tutorial!", user_id=user.id)
- db.session.add(post1);
- db.session.commit();
- user.posts
- for post in user.posts:
    ...    print(post.title);
- post.user_id
- post.author;
- db.drop_all();
- db.create_all();
- User.query.all();
- Post.query.all();
- pip install flask_bcrypt
- python3
- from flask_bcrypt import Bcrypt;
- bcrypt =  Bcrypt();
- bcrypt.generate_password_hash('kiran@1999') generate has binary bits
- bcrypt.generate_password_hash('kiran@1999').decode('utf-8') generate a string version of hash code
- bycrpt.check_password_hash(hash_pw,'password') command used to verify the hashed password to password given by the user
- pip install flask-login

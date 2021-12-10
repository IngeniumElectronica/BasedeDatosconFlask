from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///C:\\Users\\Baez\\Desktop\\flasky\\virtual\\data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

class Role(db.Model):
    __tablename__="roles"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(64), unique=True)
    users=db.relationship("User", backref="role")

    def __repr__(self):
        return"<Role %r>" %self.name

class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), unique=True, index=True)
    role_id=db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return"<User %r>" %self.username

"""#Creacion de datos
db.create_all()

#Insercion de datos
from basedatos import Role, User
admin_role=Role(name="Admin")
mod_role=Role(name="Moderator")
user_role=Role(name="User")
user_john=User(username="jhon", role=admin_role)
user_susan=User(username="susan", role=user_role)
user_david=User(username="david", role=user_role)
db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)
db.session.commit()"""
from application import db 
from application.models import Students, Assignments


db.drop_all()
db.create_all()
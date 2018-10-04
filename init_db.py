from ticket import db
from ticket.models import User

u = User(username="admin", email="namvule@hotmail.com")
u.set_password("admin")
print(str(u))
db.session.add(u)
db.session.commit()
print("Add user successful.")

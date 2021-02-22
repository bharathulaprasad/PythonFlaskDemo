#db creation from chapter 9
# on python console
#from models import db
#db.create_all()

# But for me what worked was
from app import db
db.create_all()


# just for testing
#from models import Task
#from datetime import datetime
#t= Task(title='abc', date=datetime.utcnow())
#t
#db.session.add(t)
#db.session.commit(t)
#Task.query.all()

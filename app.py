from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from views import *

admin = Admin(app)

admin.add_view(ModelView(Booking, db.session))
admin.add_view(ModelView(Request, db.session))
admin.add_view(ModelView(Teacher, db.session))

if __name__ == '__main__':
    app.run()

from app import app
from utils.db import db

with app.app_context():
    try:
        db.init_app(app)
        # db.drop_all()
        db.create_all()
    except Exception as e:
        print(e)
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="3000")

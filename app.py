from flask import Flask
from database import db
from models.meals import Meals




app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/Daily-Diet-API-db'
db.init_app(app)

# meals = Meals(id=1,description="Arroz com feijão",is_in_diet=True)






if __name__ == "__main__":
    app.run(debug=True)
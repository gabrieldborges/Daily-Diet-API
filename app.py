from flask import Flask

from models.meals import Meals

print(Meals(id=1,description="Arroz com feijão", is_in_diet=True).to_dict())







app = Flask(__name__)









if __name__ == "__main__":
    app.run(debug=True)
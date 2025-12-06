from flask import Flask, request, jsonify
from database import db
from models.meals import Meals




app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin123@127.0.0.1:3306/Daily-Diet-API-db'
db.init_app(app)

# meals = Meals(id=1,description="Arroz com feijão",is_in_diet=True)

@app.route('/meals', methods=['POST'])
def add_meal():
    data = request.json
    description = data.get("description")
    is_in_diet = data.get("is_in_diet")
    type_of_meal = data.get("type_of_meal")
    
    if description is None or is_in_diet is None or type_of_meal is None:
        return jsonify({"message": "Missing meal information."}), 400

    
    meal = Meals(type_of_meal=type_of_meal,description=description,is_in_diet=is_in_diet)
    db.session.add(meal)
    db.session.commit()
    return jsonify({"message":"Meal created successfully."})
    
    

@app.route('/meals/<int:meal_id>', methods=['PUT'])
def update_meal(meal_id):
    data = request.json
    description = data.get("description")
    is_in_diet = data.get("is_in_diet")
    type_of_meal = data.get("type_of_meal")

    meal = Meals.query.get(meal_id)
    if not meal:
        return jsonify({"message": "Meal not found."}), 404
    
    if meal and (description or is_in_diet or type_of_meal):
        meal.description = description if description is not None else meal.description
        meal.is_in_diet = is_in_diet if is_in_diet is not None else meal.is_in_diet
        meal.type_of_meal = type_of_meal if type_of_meal is not None else meal.type_of_meal
        db.session.commit() 
        return jsonify({"message":"Meal updated successfully."})
    
    return jsonify({"message":"Not able to update on current given information."}),400
    
    
@app.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    meal = Meals.query.get(meal_id)
    
    if meal:
        db.session.delete(meal) 
        db.session.commit() 
        return jsonify({"message": f"Meal deleted successfully."})

    return jsonify({"message": "Meal not found."}), 404


@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    meal = Meals.query.get(meal_id)
    
    if meal:
        return jsonify({"Meal information" : meal.to_dict()}) ,200

    return jsonify({"message": "Meal not found."}), 404
    
        
@app.route('/meals/all', methods=['GET'])
def get_all_meals():     
    meals = Meals.query.all()
    if meals :
        return jsonify(
            [ meal.to_dict() for meal in meals ]
        )
        
    return jsonify({"message": "Meal not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
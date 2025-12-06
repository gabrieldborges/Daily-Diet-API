from database import db
from datetime import datetime, timezone

class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_of_meal = db.Column(db.String(20),nullable=False)
    description = db.Column(db.String(140), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda : datetime.now(timezone.utc),nullable=False)
    is_in_diet = db.Column(db.Boolean,nullable=False)
    
    
    def to_dict(self):
        return{
            'ID' : self.id, 
            "Type of meal" : self.type_of_meal,
            "Description":self.description,
            "Created at" : self.created_at,
            "Included in diet": self.is_in_diet
        }
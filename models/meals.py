from database import db
from datetime import datetime, timezone

class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(140), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda : datetime.now(timezone.utc),nullable=
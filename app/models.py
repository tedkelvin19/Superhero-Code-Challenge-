from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import validates
db = SQLAlchemy()


hero_powers = db.Table(
    "hero_power",
    db.Column("hero_id", db.ForeignKey("heroes.id"), primary_key=True),
    db.Column("power_id", db.ForeignKey("powers.id"), primary_key=True),
    db.Column("strength", db.String),
    db.Column("created_at", db.DateTime, server_default=db.func.now()),
    db.Column("updated_at", db.DateTime, onupdate=db.func.now())
)
class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    super_name= db.Column(db.String)
    created_at= db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    powers = db.relationship("Power", secondary=hero_powers, back_populates="heroes")
    def __repr__(self):
        return f"Hero {self.name} has {self.super_name}."
class Power(db.Model):
    __tablename__ = "powers"
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String)
    description= db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    heroes = db.relationship("Hero", secondary=hero_powers, back_populates="powers")



@validates('strength')
def validate_strength(self, key, value):
    if value not in ['Strong', 'Weak', 'Average']:
        raise ValueError(f'strength must be one of the following values: Strong, Weak, Average')
    return value

@validates('description')
def validate_description(self, key, value):
    if len(value) < 20:
        raise ValueError(f'description must be at least 20 characters long')
    return value



# add any models you may need. 
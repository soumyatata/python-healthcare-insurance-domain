from app import db
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id=db.Column(db.INT,primary_key=True)
    username=db.Column(db.VARCHAR(150),unique=True,nullable=False)
    password=db.Column(db.VARCHAR(150),nullable=False)
    role=db.Column(db.VARCHAR(50),nullable=False, default='customer')

class Policy(db.Model):
    id=db.Column(db.INT,primary_key=True)
    policy_number=db.Column(db.VARCHAR(100),unique=True,nullable=False)
    policy_type=db.Column(db.VARCHAR(50),nullable=False)
    premium_amount=db.Column(db.FLOAT,nullable=False)
    #Foreign key
    user_id=db.Column(db.INT,db.ForeignKey('user.id'),nullable=False)
    #Relationship
    user=db.relationship('User',backref=db.backref('policies',lazy=True))

    def __repr__(self):
        return f'<Policy {self.policy_number}>'

class Claim(db.Model):
    id=db.Column(db.INT,primary_key=True)
    claim_number=db.Column(db.VARCHAR(100),nullable=False)
    claim_amount=db.Column(db.FLOAT,nullable=False)
    status=db.Column(db.VARCHAR(50),default='pending')
    #Foreign keys
    user_id=db.Column(db.INT,db.ForeignKey('user.id'),nullable=False)
    policy_id=db.Column(db.INT,db.ForeignKey('policy.id'),nullable=False)
    #Relationships
    user=db.relationship('User',backref=db.backref('claims',lazy=True))
    policy=db.relationship('Policy',backref=db.backref('claims',lazy=True))

    def __repr__(self):
        return f'<Claim {self.claim_number}-{self.status}>'


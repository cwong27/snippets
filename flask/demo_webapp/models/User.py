from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Initialize the database instance
from demo_webapp import db

class User(db.Model):
    """Model for users."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    # Relationship to Blog (one-to-many)
    blogs = db.relationship('Blog', back_populates='author', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User {self.username}>'
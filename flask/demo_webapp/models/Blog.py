from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Initialize the database instance
from demo_webapp import db

class Blog(db.Model):
    """Model for blog posts."""
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Foreign key to the user table
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationship to User
    author = db.relationship('User', back_populates='blogs')

    def __repr__(self):
        return f'<Blog {self.title}>'
    
    def to_dict(self):
        """
        Converts the blog post into a dictionary.
        Useful for APIs or JSON serialization.
        """
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'created': self.created.isoformat(),
            'author_id': self.author_id,
        }
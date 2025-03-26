from . import db
import uuid

class FileUpload(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    original_filename = db.Column(db.String(255), nullable=False)
    stored_filename = db.Column(db.String(255), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
from app import app, db
from app.models import User


typ = User.query.filter_by(name="zxcv").first()
print typ.typ
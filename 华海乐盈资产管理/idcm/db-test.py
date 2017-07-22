from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:siman4mysql@localhost/hhly'
db = SQLAlchemy(app)


class hw_info(db.Model):
    __tablename__ = 'hardware_server'
    serial_number = db.Column(db.String(80), primary_key=True)
    room_name = db.Column(db.String(8), unique=True)

    def __init__(self, serial_number, room_name):
        self.serial_number = serial_number
        self.room_name = room_name


@app.route('/', methods=['GET', 'POST'])
def index():
    res = hw_info.query.filter_by(room_name='HK').first()
    return res



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)

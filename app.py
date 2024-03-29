from flask import Flask, render_template
from db_handler import DbHandler


app = Flask(__name__)

@app.route('/')
def index():
    db = DbHandler()
    ads = db.get_ads()
    return render_template('index.html', ads=ads)

if __name__ == '__main__':    app.run(debug=False, host='0.0.0.0', port=8080)

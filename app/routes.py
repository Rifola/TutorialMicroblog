from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello World von Valentins PC!!"

@app.route('/home')
def home():
    return "Homepage von Valentins PC."


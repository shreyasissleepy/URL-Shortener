from flask import Flask, render_template,request,redirect
import random
import handleDB

app = Flask(__name__, template_folder='templates')

def generate_id():
    return ''.join(str(random.randint(0,9)) for _ in range(5))

@app.route('/',methods=['GET','POST'])
def home():
    shortid = None
    if request.method == 'POST':
        long_url = request.form.get('longurl')
        shortid = generate_id()
        handleDB.store(long_url,shortid)
        return render_template('home.html',shortid=shortid)
    else:
        return render_template('home.html',shortid=shortid)
    
@app.route('/<shortid>',methods=['GET'])
def redirect_to_url(shortid):
    target = handleDB.find(shortid)
    if target:
        return redirect(target)
    else:
        return render_template('home.html',error="ShortURL not found")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

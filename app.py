from flask import Flask,render_template,url_for,request
import joblib
model =joblib.load('linear-model.lb')

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello flask "
# @app.route('/sourbh')
# def index():
#     return ' index testing '

# @app.route('/')
# def basic():
#     # return render_template('basic.html')
#     return "hello "

# @app.route('/hello')
# def hello():
#     return "hello mera name sourbh"
@app.route("/about")
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/")
def index():
    return render_template("index.html")
@app.route('/myproject')
def myproject():
    return render_template('basic.html')
@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method=='POST':
        brand_name =request.form['brand_name']
        owner=int(request.form['owner'])
        age=int(request.form["age"])
        power =int(request.form['power'])
        kms=int(request.form['kms_driven'])


        brand_name_dct={"TVS":1,"Royal Enfield":2,'Triumph':3,'Yamaha':4,'Honda':5,'Hero':6,'Bajaj':7,'Suzuki':8,'Benelli':9,'KTM':10,'Mahindra':11,'Kawasaki':12,'Ducati':13,'Hyosung':14,'Harley-Davidson':15,'Jawa':16,'BMW':17,'Indian':18,'Rajdoot':19,'LML':20,'Yezdi':21,'MV':22,'Ideal':23,}

        # print(brand_name,owner,age,power,kms)
        brand_name_encode =brand_name_dct[brand_name]
        # print(brand_name_encode)
        lst = [[brand_name_encode,owner,age,power,kms]]
        pred=model.predict(lst)
        # pred=round(pred)
        pred=pred[0]  
        return render_template('basic.html',prediction=str(pred))
        # print("the predication",pred)
        # print("bike name :-",brand_name_encode,"owner of bike :-",owner,'age of bike:-',age,"power of bike:-",power,'kms of bike',kms)
        # pred=model.predict(lst)



    
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4444,debug=True)
# print(__name__)
from flask import Flask, render_template, request
import os 

#setting temp location
tp = os.path.join(os.getcwd(),"temp")
if not os.path.exists(tp):
    os.mkdir(tp)




app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/pred",methods=["POST"])
def pred():
    if request.method == "POST":
        print(request)
        f = request.files['file']
        f.save(os.path.join(tp,f.filename))  
        return render_template("index.html",sub = "Successfully Uploaded")



if __name__ =="__main__":
    app.run(debug=True)
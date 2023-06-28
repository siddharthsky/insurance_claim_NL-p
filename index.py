from flask import Flask, render_template, request
import os 
from src.components.data_ingestion import DataIngestion

#setting temp location
tp = os.path.join(os.getcwd(),"temp")
os.makedirs(os.path.dirname(tp),exist_ok=True)


#setting final location
#fp = os.path.join(os.getcwd(),"predictions")
#os.makedirs(os.path.dirname(fp),exist_ok=True)


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
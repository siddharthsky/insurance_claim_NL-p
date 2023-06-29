from flask import Flask, render_template, request
import os 
import shutil
from src.components.data_ingestion import DataIngestion

#setting temp location
tp = os.path.join(os.getcwd(),"static/temp")
os.makedirs(os.path.dirname(tp),exist_ok=True)

#Cleanup temporary files of previous sessions
try:
    shutil.rmtree("static/temp")
except OSError as e:
    print(f"Error: {e.filename} - {e.strerror}")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pred",methods=["POST"])
def pred():
    if request.method == "POST":
        print(request)
        f = request.files['file']
        f.save(os.path.join(tp,f.filename)) # save file 
        raw_filez = os.path.join(tp,f.filename) # full path of file
        DataIngObj = DataIngestion(raw_filez) # create DataIngestion object
        DataIngObj.initialize_data_ingestion() # initialize DataIngestion object
        return render_template("index.html",sub = DataIngObj.sub)

if __name__ =="__main__":
    app.run(debug=True)
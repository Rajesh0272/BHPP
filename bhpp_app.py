

import numpy as np
from flask import Flask,render_template,request,json
import pickle


__data_columns=None


app=Flask(__name__)
model = pickle.load(open('bhpp.pkl','rb'))

@app.route('/')
@cross_origin()
def home():
    return render_template('bhp.html')


@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def predict():
    if request.method=='POST':
        location=str(request.form['location'])
        sqft=float(request.form['sqft'])
        bath=int(request.form['bath'])
        bhk=int(request.form['bhk'])
        global __data_columns
        with open("./artifacts/columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']

        try: 
            loc_index = __data_columns.index(location.lower())
        except:
            loc_index = -1

        x = np.zeros(len(__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index>=0:
            x[loc_index] = 1
        prediction =model.predict([x])
        output = round(prediction[0]*1000,3)
        
        return render_template('bhp.html',result=output)
    
    #     final_features=get_estimated_price(location,sqft,bath,bhk)
    #     prediction =model.predict(final_features)
    
    #     output = round(prediction[0]*1000,3)

    # return render_template('result_bhpp.html',result=output)#,prediction_text='Home price predicted is {}'.format(output))


if __name__=="__main__":
    app.run(port=5000)

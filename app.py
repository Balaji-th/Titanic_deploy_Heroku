from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model

app = Flask(__name__)
model = load_model('model.h5')

@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')

@app.route('/confim',methods=['POST','GET'])
def register():
    if request.method=="POST":
        Pclass = request.form.get('Pclass')
        Age = request.form.get('Age')
        SibSp = request.form.get('SibSp')
        Parch = request.form.get('Parch')
        Fare = float(request.form.get('Fare'))
        Gender = request.form.get('Gender')
        if Gender.lower() == 'male' : male, female = 1, 0
        else: female, male = 1, 0
        Embarked = request.form.get('Embarked')
        if Embarked == 'C': C, Q, S = 1, 0, 0
        elif Embarked == 'Q': C, Q, S =0 , 1, 0
        else: C, Q, S = 0, 0, 1
        int_feature = [Pclass,Age,SibSp,Parch,Fare,female,male,C,Q,S]
        int_feature = [[int(x) for x in int_feature]]
        #print(int_feature)
        #int_feature=[[1,38,1,0,71.38,1,0,1,0,0]]
        predict = model.predict(int_feature)
        predict = predict > 0.5
        #print(predict)
        if predict:
            Result = ' : Passager WILL REGISTER Ticket'
        else:
            Result = ' : Passager WILL NOT REGISTER Ticket'

    return render_template('confirm.html',name=Result)
if __name__=="__main__":
    app.run(debug=True)
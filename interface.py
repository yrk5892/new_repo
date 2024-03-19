from flask import Flask, jsonify, render_template, request
from utils import MedicalInsurance
import config

app = Flask(__name__)

########################################################################################
################################## Home API ############################################
########################################################################################

@app.route('/')
def insurance_model():
    print('Welcome to the Medical Insurance Model')
    return render_template('index.html')

########################################################################################
################################## Model API ############################################
########################################################################################

@app.route('/predict_charges', methods = ['POST','GET'])
def get_insurance_charges():
    if request.method == 'POST':
        print('We are in POST Method')
        data = request.form
        age = eval(data['age'])
        sex = data['sex']
        bmi = eval(data['bmi'])
        children = eval(data['children'])
        smoker = data['smoker']
        region = data['region']  
        print(f'age ={age}, sex = {sex}, bmi = {bmi}, children = {children}, smoker = {smoker}, region = {region}')  
        
        med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
        Charges = med_ins.get_predicted_charges()
        return jsonify({'Result': f'Charges for Medical Insurance are: RS. {round(Charges,2)}'})

    else:
        print('We are in GET Method')
        data1 = request.args
        age = eval(data1.get('age'))
        sex = data1.get('sex')
        bmi = data1.get('bmi')
        children = eval(data1.get('children'))
        smoker = data1.get('smoker')
        region = data1.get('region')
        # print(f'age ={age}, sex = {sex}, bmi = {bmi}, children = {children}, smoker = {smoker}, region = {region}')

        med_ins1 = MedicalInsurance(age, sex, bmi, children, smoker, region)
        Charges1 = med_ins1.get_predicted_charges()
        return jsonify({'Result': f'Charges for Medical Insurance are: RS. {round(Charges1,2)}'})

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug =True)
#importing libraries
from flask import Flask ,render_template,url_for,request,flash,redirect
from sklearn.externals import joblib
import pandas as pd
import sklearn
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key="."
model=joblib.load("C:\\Users\\cheth\\Desktop\\pbl_datasets\\RFmodel.sav")#Change it to your saved model's path
y_label=None
company={0:'😓',1:'AMAZON',2:'ARICENT',3:'ATOS',4:'CAPGEMINI',5:'COGNIZANT',6:'DELL',7:'DIRECTI',8:'ENDURANCE',9:'ERICSSON ',10:'FIDELITY',11:'HP',\
    12:'KPIT',13:'METRIC STREAM ',14:'MINDTREE ',15:'MUSIGMA ',16:' NINJAKART ',17:'NOKIA',18:' OFSS ',19:'PHILIPS ',20:'PWC',21:'ROBERT BOSCH ',\
         22:'SANDHAR',23:' SAP LABS ',24:' SASKEN',25:'SIEMENS',26:'SIMEIO',27:'TATA ELXSI ',28:' TECH M ',29:' TEMENOS',30:' WIPRO ',31:'ZETA'} 
        
#defining functions to process the requests made on to the Home route            
@app.route("/",methods=["GET","POST"])


def index():
    if request.method=="POST":
        ece,cse,ise,tce,eee,mech,cv=0,0,0,0,0,0,0
        software_modeling,web_dev,c_data_struct,program_lang,algorithm,os, dbms_query,data_analysis,oops,cn,shell,\
            circuits_control_sys,matlab,dsp=0,0,0,0,0,0,0,0,0,0,0,0,0,0
        tenth=request.form['tenth']
        puc=request.form['puc']
        be=request.form['be']
        current_backs=int(request.form['current_backs'])
       
        if request.form.getlist('software_modeling'):
            software_modeling=1
            print(software_modeling)

        if request.form.getlist('web_dev'):
            web_dev=1

        if request.form.getlist('c_data_struct'):
            c_data_struct=1


        if request.form.getlist('program_lang'):
            program_lang=1

        if request.form.getlist('algorithm'):
            algorithm=1

        if request.form.getlist('os'):
            os=1
        if request.form.getlist('dbms_query'):
            dbms_query=1

        if request.form.getlist('data_analysis'):
            data_analysis=1

        if request.form.getlist('oops'):
            oops=1
        if request.form.getlist('cn'):
            cn=1
        if request.form.getlist('shell'):
            shell=1
        if request.form.getlist('circuits_control_sys'):
            circuits_control_sys=1
        if request.form.getlist('matlab'):
            matlab=1
        if request.form.getlist('dsp'):
            dsp=1
           
        if request.form['branch']=='ECE':
            ece=1
        elif request.form['branch']=='CSE':  
            cse=1
        elif request.form['branch']=='ISE': 
            ise=1
        elif request.form['branch']=='EEE': 
            eee=1    
        elif request.form['branch']=='MECH': 
            mech=1
        elif request.form['branch']=='TCE': 
            tce=1    
        else:
            cv=1    
        data={'tenth':[tenth],'puc':[puc],'be':[be],'current_backs':[current_backs],'software_modeling':[software_modeling],\
            'web_dev':[web_dev],'c_data_struct':[c_data_struct],'program_lang':[program_lang],'algorithm':[algorithm],'os':[os],\
                'dbms_query':[dbms_query] ,'data_analysis':[data_analysis],'oops':[oops],'cn':[cn],'shell':[shell],'circuits_control_sys':[circuits_control_sys],\
                    'matlab':[matlab],'dsp':[dsp],'ece':[ece],'tce':[tce],'eee':[eee],'ise':[ise],'cse':[cse],'mech':[mech],'cv':[cv]}

        df=pd.DataFrame(data=data)
        print(df)
        y_label=model.predict(df)
        print(y_label)
        print(company[y_label[0]])
        result=company[y_label[0]]
       
  
        return render_template("predict.html",result=result)
        

    return render_template("index.html")
#defining functions to process the requests made on to the /batch route   
@app.route("/batch",methods=["POST","GET"])  

def batch_prediction():
    if request.method=="POST":
         f= request.files['file']
         df=pd.read_csv(f)
         prediction=list(model.predict(df))
         percent=round((len(prediction)-prediction.count(0))/len(prediction)*100,3)
         return render_template("final.html",percent=percent)

    return render_template("batch_pred.html")


  
if __name__=="__main__":
    app.run(debug=True) 

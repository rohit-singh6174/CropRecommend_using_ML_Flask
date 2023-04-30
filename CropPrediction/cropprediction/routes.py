from cropprediction import app,db,bcrypt
from flask import Flask,render_template,url_for,redirect,flash,session,request
from flask_login import login_user,logout_user,current_user,login_required
from cropprediction.forms import FarmerRegForm,FarmerLogForm,FarmerAccountUpdate
from cropprediction.models import Farmers, Farmers_Details
from requests import get
from geopy.geocoders import Nominatim   #Nominatim uses OpenStreetMap data to find locations on Earth by name and address (geocoding). It can also do the reverse, find an address for any location on the planet.
import pandas
import matplotlib.pyplot as plt
import pickle
import numpy as np
import os
import plotly.graph_objs as go








@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/farmerregister", methods=['POST','GET'])
def farmerregister():
    form=FarmerRegForm()

    if current_user.is_authenticated:
             return redirect(url_for('/farmerhome'))
    else:
        if form.validate_on_submit():
             print("hello") 
             farmer_id= Farmers_Details.query.filter_by(farmerid=form.farmerid.data).first()
            #  print(farmer_id)
             if farmer_id:
                farmer=Farmers.query.filter_by(username=form.username.data).first()
                if farmer:
                    flash(f'User {form.username.data} Already Exist',category='danger')
                else:
                    encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                    newFarmers=Farmers(name=form.name.data,phone=form.phone.data,gender=form.gender.data, district=form.district.data,farmerid=form.farmerid.data,username=form.username.data,password=encrypted_password)
                    
                    response = get('https://ipapi.co/json').json()
                    latitude = response['latitude']
                    longtitude = response['longitude']
                    g =("Cambria", 18,"bold")
                    weather = get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={YOUR-APT-KEY}&units=metric'.format(latitude, longtitude)).json()
                    #tempdata=weather['main']['temp']
                   
                    myweather = (weather['main']['temp'])
                    degree = "°C"
                    havaman = (myweather,"°C")
                  

                    # initialize Nominatim API
                    geolocator = Nominatim(user_agent="geoapiExercises")
                    # Latitude & Longitude input
                    Latitude =  str(latitude)
                    Longitude = str(longtitude)
                    location = geolocator.reverse(Latitude+","+Longitude)
                    address = location.raw['address']
                    # traverse the data
                    city = address.get('city','')
                    #state = address.get('state','')
                    # #country = address.get('country','')
                    # #code = address.get('country_code')
                    # #zipcode = address.get('postcode')
                    city_name = ('City:',city)
                    #print('State :', state)
                    # print('Country:',country)
                    # #print('Zip Code : ', zipcode)
                    # 
                 
                    print(city_name)
                    print(havaman)   
                    db.session.add(newFarmers)
                    db.session.commit()
                    flash(f'Account created successfully for {form.username.data}',category='success')
                    return redirect(url_for('farmerlogin'))
             else:
                  flash(f'Invalid Registration{form.username.data}',category='danger')

    return render_template('farmerregister.html',form=form)

@app.route("/farmerlogin",methods=['POST','GET'])
def farmerlogin():
    form=FarmerLogForm()
    if current_user.is_authenticated:
             return redirect(url_for('farmerhome'))
    
    else:
         if form.validate_on_submit():
              
              print("Hello login")
              print(form.username.data)
              farmers=Farmers.query.filter_by(username=form.username.data).first()
              print(farmers)
              if farmers:
                   if bcrypt.check_password_hash(farmers.password,form.password.data):
                         login_user(farmers)
                         print("Login Successfull")
                         flash(f'Login Successfully {form.username.data}',category='success')
                         return redirect(url_for('farmerhome'))
                   else:
                        flash(f'Invalid Password',category='danger')
              else:
                    flash(f'User does not exist {form.username.data}',category='danger')
    return render_template('farmerlogin.html',form=form)

@app.route("/farmerhome")
def farmerhome():
    username=current_user.username
    farmer=Farmers.query.filter_by(username=current_user.username).first()
    print(farmer)
    response = get('https://ipapi.co/json').json()
    latitude =19.0089 #response['latitude']
    longtitude =72.8574 #response['longitude']
    g =("Cambria", 18,"bold")
    weather = get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={YOUR-APT-KEY}&units=metric'.format(latitude, longtitude)).json()
    #tempdata=weather['main']['temp']
                   
    myweather = (weather['main']['temp'])
    degree = "°C"
    havaman = (myweather)
                  

    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    # Latitude & Longitude input
    Latitude =  str(latitude)
    Longitude = str(longtitude)
    location = geolocator.reverse(Latitude+","+Longitude)
    address = location.raw['address']
    # traverse the data
    city = address.get('city','')
    #state = address.get('state','')
    # #country = address.get('country','')
    # #code = address.get('country_code')
    # #zipcode = address.get('postcode')
    city_name = (city)
    #print('State :', state)
    # print('Country:',country)
    # #print('Zip Code : ', zipcode)
     # 
                 
    print(city_name)
    print(havaman)   

    
    return render_template('farmerhome.html',havaman=havaman,city_name=city_name)

@app.route("/farmeraccount", methods=['POST','GET'])
@login_required
def farmeraccount():
    form=FarmerAccountUpdate()
    if form.validate_on_submit():
        updateaccount = Farmers.query.filter_by(farmerid=form.farmerid.data).first()
        #print(updateaccount.name)
        updateaccount.name =form.name.data
        updateaccount.phone = form.phone.data
        updateaccount.district= form.district.data
        db.session.commit()
        print("Update Sucessfull")
        flash(f'Account Updateed successfully for {form.username.data}',category='success')

    return render_template('farmeraccount.html',form=form)

@app.route("/farmerlogout")
def farmerlogout():
    logout_user()
    return redirect(url_for('farmerlogin'))

@app.route("/croppredict")
def croppredict():
    print("Crop ")
    response = get('https://ipapi.co/json').json()
    latitude =19.0089 #response['latitude']
    longtitude =72.8574 #response['longitude']
    g =("Cambria", 18,"bold")
    weather = get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={YOUR-APT-KEY}7&units=metric'.format(latitude, longtitude)).json()
    #tempdata=weather['main']['temp']
                   
    myweather = (weather['main']['temp'])
    degree = "°C"
    havaman = (myweather)
                  

    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    # Latitude & Longitude input
    Latitude =  str(latitude)
    Longitude = str(longtitude)
    location = geolocator.reverse(Latitude+","+Longitude)
    address = location.raw['address']
    # traverse the data
    city = address.get('city','')
    #state = address.get('state','')
    # #country = address.get('country','')
    # #code = address.get('country_code')
    # #zipcode = address.get('postcode')
    city_name = (city)
    return render_template('croppredict.html',bhai="kuch karna hain iska ab?" ,temperature=havaman)

@app.route('/predict',methods=['POST','GET'])
def predict():
    #lr_model=pickle.load(open('D:\python\SEM6 Mini Project\CropPrediction\cropprediction\Crop-Suggestor-lr.sav','rb'))
    knn_model=pickle.load(open('D:\python\SEM6 Mini Project\CropPrediction\cropprediction\Crop-Suggestor-knn.sav','rb'))
    rfc_model=pickle.load(open('D:\python\SEM6 Mini Project\CropPrediction\cropprediction\Crop-Suggestor-rfc.sav','rb'))
    svm_model=pickle.load(open('D:\python\SEM6 Mini Project\CropPrediction\cropprediction\Crop-Suggestor-svm.sav','rb'))
    dt_entropy_model = pickle.load(open('D:\python\SEM6 Mini Project\CropPrediction\cropprediction\Crop-Suggestor-dt_entropy.sav','rb'))
    dt_gini_model = pickle.load(open('D:\python\SEM6 Mini Project\CropPrediction\cropprediction\Crop-Suggestor-dt_gini.sav','rb'))

    int_features=[eval(features) for features in request.form.values()]
    print(int_features)
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    # lr_prediction=lr_model.predict(final)
    svm_prediction = svm_model.predict(final)
    knn_prediction = knn_model.predict(final)
    rfc_prediction = rfc_model.predict(final)
    dt_entropy_prediction = dt_entropy_model.predict(final)
    dt_gini_prdiction  =  dt_gini_model.predict(final)
    
    # print(lr_prediction)
    print(svm_prediction)
    print(knn_prediction)
    print(rfc_prediction)
    print(dt_entropy_prediction)
    print(dt_gini_prdiction)


    # return render_template('prediction.html',pred=prediction,bhai="kuch karna hain iska ab?")
    return render_template('croppredict.html',
                        rfc_pred=' RandomForest Classifiern {}'.format(rfc_prediction),   
                        svm_pred='SVM  {}'.format(svm_prediction),
                        knn_pred=' k Nearest Neighbour {}'.format(knn_prediction),
                        # lr_pred='The best suitable crop i predicted for your farm according to the Logistic Regression with the accuracy rate  of 96.81% is {}'.format(lr_prediction),
                        dt_entropy_pred='DecisionTreeClassifier using entropy{}'.format(dt_entropy_prediction),
                        dt_gini_pred='DecisionTreeClassifier using gini index{}'.format(dt_gini_prdiction),
                        
                        bhai="kuch karna hain iska ab?")


@app.route('/fertilizer')
def fertilizer():
    print("Hello") 
    response = get('https://ipapi.co/json').json()
    latitude =19.0089 #response['latitude']
    longtitude =72.8574 #response['longitude']
    g =("Cambria", 18,"bold")
    weather = get('http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={YOUR-APT-KEY}7&units=metric'.format(latitude, longtitude)).json()
    #tempdata=weather['main']['temp']
                   
    myweather = (weather['main']['temp'])
    degree = "°C"
    havaman = (myweather)
                  

    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")
    # Latitude & Longitude input
    Latitude =  str(latitude)
    Longitude = str(longtitude)
    location = geolocator.reverse(Latitude+","+Longitude)
    address = location.raw['address']
    # traverse the data
    city = address.get('city','')
    #state = address.get('state','')
    # #country = address.get('country','')
    # #code = address.get('country_code')
    # #zipcode = address.get('postcode')
    city_name = (city)
    return render_template('fertilizerpredict.html', temperature=havaman)

@app.route('/fertilizer_recommend', methods=['GET','POST'])
def fertilizer_recommend():
    # knn_model=pickle.load(open('D:\\python\\SEM6 Mini Project\\CropPrediction\\cropprediction\\fertilizermodel\\Fertilizer-Suggestor-knn.sav','rb'))
    # print(knn_model)

    knn_fertilizer=pickle.load(open('D:\\python\SEM6 Mini Project\\CropPrediction\\cropprediction\\fertilizermodel\\Fertilizer-Suggestor-knn.sav','rb'))
    dtc_fertilizer=pickle.load(open('D:\\python\\SEM6 Mini Project\\CropPrediction\\cropprediction\\fertilizermodel\\Fertilizer-Suggestor-dtc.sav','rb'))
    svc_fertilizer=pickle.load(open('D:\\python\\SEM6 Mini Project\\CropPrediction\\cropprediction\\fertilizermodel\\Fertilizer-Suggestor-svc.sav','rb'))
    rfc_fertilizer=pickle.load(open('D:\\python\\SEM6 Mini Project\\CropPrediction\\cropprediction\\fertilizermodel\\Fertilizer-Suggestor-rfc.sav','rb'))
    print("Hello")
    int_features=[eval(features) for features in request.form.values()]
    print(int_features)
    final=[np.array(int_features)]
    print(int_features)
    print(final)

    svc_prediction = svc_fertilizer.predict(final)
    if svc_prediction[0] == 0:
         print("10-26-26 Fertilizer")
         svc_prediction="10-26-26 Fertilizer"
         
    elif svc_prediction[0] == 1:
         print("14-35-14 Fertilizer")
         svc_prediction="14-35-14 Fertilizer"
         
    elif svc_prediction[0] == 2:
         print("17-17-17 Fertilizer")
         svc_prediction="17-17-17 Fertilizer"

    elif svc_prediction[0] == 3:
         print("20-20 Fertilizer")
         svc_prediction="20-20 Fertilizer"
    
    elif svc_prediction[0] == 4:
         print("28-28 Fertilizer")
         svc_prediction="28-28 Fertilizer"

    elif svc_prediction[0] == 5:
         print("DAP Fertilizer")
         svc_prediction="DAP Fertilizer"
    
    else:
         print("Urea Fertilizer")
         svc_prediction="Urea Fertilizer"
    


    knn_prediction= knn_fertilizer.predict(final)
    if knn_prediction[0] == 0:
         print("10-26-26 Fertilizer")
         knn_prediction="10-26-26 Fertilizer"

    elif knn_prediction[0] == 1:
         print("14-35-14 Fertilizer")
         knn_prediction="14-35-14 Fertilizer"

    elif knn_prediction[0] == 2:
         print("17-17-17 Fertilizer")
         knn_prediction="17-17-17 Fertilizer"

    elif knn_prediction[0] == 3:
         print("20-20 Fertilizer")
         knn_prediction="20-20 Fertilizer"

    elif knn_prediction[0] == 4:
         print("28-28 Fertilizer")
         knn_prediction="28-28 Fertilizer"

    elif knn_prediction[0] == 5:
         print("DAP Fertilizer")
         knn_prediction="DAP Fertilizer"

    else:
         print("Urea Fertilizer")
         knn_prediction="Urea Fertilizer"

    rfc_prediction= rfc_fertilizer.predict(final)
    if rfc_prediction[0] == 0:
         print("10-26-26 Fertilizer")
         rfc_prediction="10-26-26 Fertilizer"
         return rfc_prediction
    
    elif rfc_prediction[0] == 1:
         print("14-35-14 Fertilizer")
         rfc_prediction="14-35-14 Fertilizer"
      
    elif rfc_prediction[0] == 2:
         print("17-17-17 Fertilizer")
         rfc_prediction="17-17-17 Fertilizer"
        
         
    elif rfc_prediction[0] == 3:
         print("20-20 Fertilizer")
         rfc_prediction="20-20 Fertilizer"
        
         
    elif rfc_prediction[0] == 4:
         print("28-28 Fertilizer")
         rfc_prediction="28-28 Fertilizer"
     
    
    elif rfc_prediction[0] == 5:
         print("DAP Fertilizer")
         print("28-28 Fertilizer")
         rfc_prediction="DAP Fertilizer"
         
    else:
         print("Urea Fertilizer")
         rfc_prediction="Urea Fertilizer"


   
   
    dtc_prediction=dtc_fertilizer.predict(final)
    if dtc_prediction[0] == 0:
         print("10-26-26 Fertilizer")
         dtc_prediction="10-26-26 Fertilizer"

    elif dtc_prediction[0] == 1:
         print("14-35-14 Fertilizer")
         dtc_prediction="14-35-14 Fertilizer"

    elif dtc_prediction[0] == 2:
         print("17-17-17 Fertilizer")
         dtc_prediction="17-17-17 Fertilizer"

    elif dtc_prediction[0] == 3:
         print("20-20 Fertilizer")
         dtc_prediction="20-20 Fertilizer"

    elif dtc_prediction[0] == 4:
         print("28-28 Fertilizer")
         dtc_prediction="28-28 Fertilizer"

    elif dtc_prediction[0] == 5:
         print("DAP Fertilizer")
         dtc_prediction="DAP Fertilizer"

    else:
         print("Urea Fertilizer")
         dtc_prediction="Urea Fertilizer"
    
    # Create bar graph data
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-score']
    values = [0.9838709677419355, 0.9761904761904763, 0.9285714285714286, 0.9393939393939394]

    


    

    

    print(metrics)
    print(values)

    # Add chart title and axis labels
    # layout = go.Layout(title='Evaluation Metrics', xaxis=dict(title='Metric'),yaxis=dict(title='Value'))






    


    # print(svc_prediction)
    # print(knn_prediction)
    # print(rfc_prediction)
    # print(dtc_prediction)

   
    
    
  
    
    

    
    
    
    # temperature = request.form.get("t")
    # nitrogen = request.form.get("n")
    # phosphorus = request.form.get("p")
    # potassium = request.form.get("k")
    # humidity = request.form.get("h")
    # soi_moisture = request.form.get("s_m")
    # soil_type = request.form.get("s_type")
    # crop_type= request.form.get('c_type')

    # print(soil_type)
    # print(crop_type)

    return render_template('fertilizerpredict.html',metrics=metrics, values=values, 
     svc_prediction= ' SVC Predicted : {}'.format(svc_prediction),
     knn_prediction= ' KNN Predicted : {}'.format(knn_prediction),
     rfc_prediction= ' Random Forest Classifier Predicted : {}'.format(rfc_prediction),
     dtc_prediction= ' DTC Predicted : {}'.format(dtc_prediction)
     )



    


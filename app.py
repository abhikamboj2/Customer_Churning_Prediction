import pandas as pd
import numpy as np
import tensorflow as tf
import streamlit as st
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
import pickle

#load trained model
model=tf.keras.models.load_model('model.h5')

with open('OneHotEncoder_obj.pkl','rb') as f:
    onehot_geo=pickle.load(f)
with open('label_encoder_gender.pkl','rb') as f:
    label_encoder_gender=pickle.load(f)    
with open('scaler_write.pkl','rb') as f:    
    scaler=pickle.load(f)

#streamlit app    
st.title('Customer Churn Prediction') 
geography=st.selectbox('Select Geography',onehot_geo.categories_[0])
gender=st.selectbox('gender',label_encoder_gender.classes_)
age=st.slider('age',18,100)
balance=st.number_input('balance')
credit_score=st.slider('credit score')
estimated_salary=st.number_input('estimated salary')
tenure=st.slider('tenure',0,10)
no_of_products=st.slider('number of products',1,4)
has_cr_card=st.selectbox('has credit card',[0,1])
is_active_member=st.selectbox('is active member',[0,1])

input_data=pd.DataFrame({'CreditScore':[credit_score],
                         'Gender':label_encoder_gender.transform([gender])[0],
                         'Age':[age],
                         'Tenure':[tenure],
                         'Balance':[balance],
                         'NumOfProducts':[no_of_products],
                         'HasCrCard':[has_cr_card],
                         'IsActiveMember':[is_active_member],
                         'EstimatedSalary':[estimated_salary]})
geo_encoded=onehot_geo.transform([[geography]]).toarray()
geo_to_concat=pd.DataFrame(geo_encoded,columns=onehot_geo.get_feature_names_out(['Geography']))
final_input_data=pd.concat([input_data,geo_to_concat],axis=1)
scaled_input=scaler.transform(final_input_data)

prediction=model.predict(scaled_input)
probability=prediction[0][0]


if probability>0.5:
    st.write("The customer will leave the bank")
else:
    st.write("The customer will stay in the bank")

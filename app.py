import pickle
pickle.dump(df,open('df.pkl','wb'))
pickle.dump(pipe,open('pipe.pkl','wb'))

import streamlit as st
st.title("Laptop Price Predictor")
st.text("This app is designed to predict the laptop price based on the configuration")
st.text("Once the configuration details of the laptop are entered,")
st.text("please click on the PREDICT button to get the estimated price of the laptop")
 
import pickle
import numpy as np
pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

company=st.selectbox("Brand",df['Company'].unique(),index=4)
type1=st.selectbox("Type",df['TypeName'].unique(),index=1)
cpu=st.selectbox("Processor",df['Cpu'].unique(),index=0)
ram=st.selectbox("RAM(in GB)",[2,4,6,8,12,16,24,32,64,128],index=3)
gpu=st.selectbox('Graphics Card',df['Gpu'].unique(),index=0)
os=st.selectbox('Operating System',df['OpSys'].unique(),index=2)
weight=st.slider('Weight(in kg)',min_value=0,max_value=4,value=2)
ips=st.selectbox('IPS Display?',['No','Yes'])
touchscreen=st.selectbox('Touchscreen?',['No','Yes'])
screen_size=st.number_input("Size of the screen(In Inches, measured diagonally)",
min_value=10,max_value=18,value=15)
resolution=st.selectbox("Screen Resolution",['1920x1080','3840x2160','3200x1800',
'2560x1600','2880x1800','1366x768','2304x1440','1440x900','2560x1440','1600x900',
'2256x1504','2400x1600'],index=0)
 
if st.button("PREDICT PRICE"):
  ppi=None
if touchscreen =='Yes':
  touchscreen=1
else:
  touchscreen=0
if ips == 'Yes':
   ips=1
else:
   ips=0
X_res=int(resolution.split('x')[0])
Y_res=int(resolution.split('x')[1])
 
ppi =((X_res**2)+(Y_res**2))**0.5/screen_size
 
query=np.array([[company,type1,cpu,ram,gpu,os,weight,ips,touchscreen,ppi]])
op=np.exp(pipe.predict(query))
st.subheader("The predicted price for the laptop with above mentioned configuration is:")
st.subheader("Rs."+str(round(op[0])))


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install Cython
#!pip install fasttext


# In[7]:


#!pip install flask


# In[2]:


# importing os for setting path
import os

working_dir = 'E:\\AIML\\Project_chatbot\\'

os.chdir(working_dir)

# Suppress warnings
import warnings; warnings.filterwarnings('ignore')


# In[3]:


import fasttext 
def fasttextmodelload():
    fasttxtmodel = fasttext.load_model('safebot_multi.bin')
    return fasttxtmodel


# In[4]:


def fasttxtpotentialacclvl_predict(x):
    model = fasttextmodelload()
    pred = model.predict(x, k =2)
    return pred


# In[5]:


# def map(x):
#     if x == "__label__3":
#         return "Potential accident level: 3"
#     elif x == "__label__1":
#         return "Potential accident level: 1"
#     elif x == "__label__2":
#         return "Potential accident level: 2"
#     elif x == "__label__4":
#         return "Potential accident level: 4"
#     elif x == "__label__5":
#         return "Potential accident level: 5"


# In[6]:


#test
prediction = fasttxtpotentialacclvl_predict("The collaborator reports that he was working in the UstulaciÃ³n and realized that the cyclone duct was obstructed and opened the door to try to unclog the same and the material detached and projected towards the employee causing small burn in the right heel.") 


preds = str(prediction[0]).split(',')

print(preds[0])
print(preds[1])

#import json

#jsonObj = json.dumps(prediction[0])
#print(jsonObj)


# In[ ]:





# In[10]:


from flask import Flask,request,json,render_template,jsonify

app = Flask(__name__) # ,static_url_path='/'

#@app.route('/hello')
#def index():
#    return render_template('index.html',name='John')  #{'hello': 'world'} 


@app.route('/get_p_acc_lvl', methods=['GET'])
def get_potential_accident_level():
    
    query_parameters = request.args
    
    acc_desc = query_parameters.get('description')
    
    prediction = fasttxtpotentialacclvl_predict(acc_desc) #ft.predict('acc_desc')
    #prediction = "Employee was sitting in the resting area at level 326 (raise bore), when he suffered sudden illness, falling and suffering excoriation on the face."
    
    #print(acc_desc)
    
     #pred = json.dumps(prediction[0])
     #print(pred)
    #pred = str(prediction[0])
    print(prediction)
    
    preds = str(prediction[0]).split(',')
    
    
    if preds[0] == "('__label__3'":
        pred_acc =  "Accident level: 3"
    elif preds[0] =="('__label__1'":
        pred_acc = "Accident level: 1"
    elif preds[0] == "('__label__2'":
        pred_acc = "Accident level: 2"
    elif preds[0] == "('__label__4'":
        pred_acc = "Accident level: 4"
    elif preds[0] == "('__label__5'":
        pred_acc =  "Accident level: 5"    
    else:
        pred_acc =  "Accident level: Undetermined"
    print(preds[0])
    
    print(preds[1])
    
    if preds[1] == " '__label__3')": 
        pred_pot =  "Potential accident level: 3"
    elif preds[1] ==" '__label__1')":
        pred_pot = "Potential accident level: 1"
    elif preds[1] == " '__label__2')":
        pred_pot = "Potential accident level: 2"
    elif preds[1] == " '__label__4')":
        pred_pot = "Potential accident level: 4"
    elif preds[1] == " '__label__5')":
        pred_pot =  "Potential accident level: 5"
    else:
        pred_pot =  "Potential accident level: Undetermined"    
        
    
    pred = pred_acc + " & " + pred_pot

    return jsonify(pred)


if __name__ == '__main__':
  
    app.run()


# In[ ]:





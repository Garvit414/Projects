import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Users/Garvit Agarwal/Downloads/trained_model_1.sav', 'rb'))


# creating a function for Prediction

def Quality_prediction(input_data):
    

    # changing the input_data to numpy array
    # input_data=(7.3,	0.65,	0.00	,1.2,	0.065,	15.0,	21.0	,0.9946	,3.39	,0.47,10.0)
    # input_data_as_numpy_array = np.asarray(input_data)
    arr= np.asarray(input_data).reshape(1,-1)
    prediction=loaded_model.predict(arr)
    print(prediction)
    if prediction[0]==0:
        return "Bad Quality"
    elif prediction[0] ==1:
        return "Avarage Quality"
    else:
        return "Best Quality"
    
  
    
  
def main():
    
    
    # giving a title
    st.title('Red Wine Quality Prediction Web App')
    
    
    # getting the input data from the user
    
    # fixed acidity	volatile acidity	citric acid	residual sugar	chlorides	free sulfur dioxide	total sulfur dioxide	density	pH	sulphates	alcohol	quality

    Fixed_Acidity = st.text_input('Number of Fixed Acidity')
    Volatile_Acidity = st.text_input('Volatile_Acidity Level')
    Citric_Acid = st.text_input('Citric_Acid value')
    Residual_Sugar = st.text_input('Residual_Sugar value')
    Chlorides = st.text_input('Chlorides Level')
    Free_Sulphur_Dioxide = st.text_input('Free_Sulphur_Dioxide value')
    Total_Sulfur_Dioxide = st.text_input('Total_Sulfur_Dioxide value')
    Density = st.text_input('Density ')
    PH = st.text_input('PH ')
    Sulphate = st.text_input('Sulphate ')
    Alcohol = st.text_input('Alcohol ')
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Red Wine Quality Result'):
        diagnosis = Quality_prediction([Fixed_Acidity,Volatile_Acidity,Citric_Acid, Residual_Sugar,Chlorides,Free_Sulphur_Dioxide	,Total_Sulfur_Dioxide,Density,PH,Sulphate,Alcohol])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()




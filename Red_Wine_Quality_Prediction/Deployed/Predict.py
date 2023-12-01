
import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Users/Garvit Agarwal/Downloads/trained_model.sav', 'rb'))


input_data=(7.3,	0.65,	0.00	,1.2,	0.065,	15.0,	21.0	,0.9946	,3.39	,0.47,10.0)
arr= np.asarray(input_data).reshape(1,-1)
prediction=loaded_model.predict(arr)
print(prediction)
if prediction[0]==0:
  print("Bad Quality")
elif prediction[0] ==1:
  print("Avarage Quality")
else:
  print("Best Quality")
  
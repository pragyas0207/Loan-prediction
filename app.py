from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open("model.pkl","rb"))

class LoanInput(BaseModel):
    Gender:int
    Married:int
    Dependents:int
    Education:int
    Self_Employed:int
    ApplicantIncome:float
    CoapplicantIncome:float
    LoanAmount:float
    Loan_Amount_Term:float
    Credit_History:int
    Property_Area:int


@app.post("/predict")
def predict(data:LoanInput):

    features = np.array([
        data.Gender,
        data.Married,
        data.Dependents,
        data.Education,
        data.Self_Employed,
        data.ApplicantIncome,
        data.CoapplicantIncome,
        data.LoanAmount,
        data.Loan_Amount_Term,
        data.Credit_History,
        data.Property_Area
    ]).reshape(1,-1)

    prediction = model.predict(features)

    return {"prediction":int(prediction[0])}



# python -m uvicorn app:app --reload
# or uvicorn app:app --reload
# Do this to run the app.py or after evry change to app.py
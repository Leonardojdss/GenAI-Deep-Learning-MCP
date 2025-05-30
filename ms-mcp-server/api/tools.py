from fastapi import APIRouter
import joblib
import pandas as pd
import os
from pydantic import BaseModel

router = APIRouter()

class PredictRequest(BaseModel):
    person_age: int
    person_income: int
    person_emp_length: int
    loan_amnt: int
    cb_person_default_on_file: int

@router.post("/predict", operation_id="Predict")
async def predict(request: PredictRequest):
    """
    An endpoint to predict if user credit is approved or not, using JSON data.
    """
    actual_path = os.getcwd()
    path = os.path.dirname(actual_path)
    dir_model = f"{path}/ms-mcp-server/model-ml/model_credit_risk.pkl"
    model = joblib.load(dir_model)

    dataset = pd.DataFrame({
        "person_age": [request.person_age],
        "person_income": [request.person_income],
        "person_emp_length": [request.person_emp_length],
        "loan_amnt":  [request.loan_amnt],
        "cb_person_default_on_file": [request.cb_person_default_on_file]
    })

    predict = model.predict(dataset)

    if predict[0] == 1:
        result = "Crédito Aprovado, procure pelo seu gerente"
    else:
        result = "Crédito Negado, tente novamente em 6 meses"
    
    return {"result": result, "prediction": int(predict[0])}
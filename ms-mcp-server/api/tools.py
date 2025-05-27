from fastapi import APIRouter
import joblib
import pandas as pd
import os
from fastapi import Form

router = APIRouter()

@router.post("/predict", operation_id="Predict")
async def hello(
    person_age: int = Form(...),
    person_income: int = Form(...),
    person_emp_length: int = Form(...),
    loan_amnt: int = Form(...),
    cb_person_default_on_file: int = Form(...)
):
    """
    An endpoint to predict if user credit is approved or not, using form data.
    """
    actual_path = os.getcwd()
    path = os.path.dirname(actual_path)
    dir_model = f"{path}/ms-mcp-server/model-ml/model_credit_risk.pkl"
    model = joblib.load(dir_model)

    dataset = pd.DataFrame({
        "person_age": [person_age],
        "person_income": [person_income],
        "person_emp_length": [person_emp_length],
        "loan_amnt":  [loan_amnt],
        "cb_person_default_on_file": [cb_person_default_on_file]
    })

    predict = model.predict(dataset)

    if predict[0] == 1:
        result = "Crédito Aprovado, procure pelo seu gerente"
    else:
        result = "Crédito Negado, tente novamente daqui alguns meses"
    print(result)

    return result
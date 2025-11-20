from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from model import HeartRiskModel
from schemas import PatientData

app = FastAPI(title="Heart Attack Risk API")
templates = Jinja2Templates(directory="templates")

# Загружаем модель
model = HeartRiskModel("heart_risk_model.pkl")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("start_form.html", {"request": request})


@app.post("/predict_form", response_class=HTMLResponse)
async def predict_form(
    request: Request,
    age: float = Form(...),
    cholesterol: float = Form(...),
    heart_rate: float = Form(...),
    diabetes: int = Form(...),
    family_history: int = Form(...),
    smoking: int = Form(...),
    alcohol_consumption: int = Form(...),
    exercise_hours_per_week: float = Form(...),
    diet: int = Form(...),
    previous_heart_problems: int = Form(...),
    medication_use: int = Form(...),
    stress_level: float = Form(...),
    sedentary_hours_per_day: float = Form(...),
    income: float = Form(...),
    bmi: float = Form(...),
    triglycerides: float = Form(...),
    physical_activity_days_per_week: float = Form(...),
    sleep_hours_per_day: float = Form(...),
    blood_sugar: float = Form(...),
    gender: str = Form(...),
    systolic_blood_pressure: float = Form(...),
    diastolic_blood_pressure: float = Form(...)
):

    data = {
        "age": age,
        "cholesterol": cholesterol,
        "heart_rate": heart_rate,
        "diabetes": diabetes,
        "family_history": family_history,
        "smoking": smoking,
        "alcohol_consumption": alcohol_consumption,
        "exercise_hours_per_week": exercise_hours_per_week,
        "diet": diet,
        "previous_heart_problems": previous_heart_problems,
        "medication_use": medication_use,
        "stress_level": stress_level,
        "sedentary_hours_per_day": sedentary_hours_per_day,
        "income": income,
        "bmi": bmi,
        "triglycerides": triglycerides,
        "physical_activity_days_per_week": physical_activity_days_per_week,
        "sleep_hours_per_day": sleep_hours_per_day,
        "blood_sugar": blood_sugar,
        "gender": gender,
        "systolic_blood_pressure": systolic_blood_pressure,
        "diastolic_blood_pressure": diastolic_blood_pressure
    }

    y = model.predict(data)
    proba = model.predict_proba(data)

    return templates.TemplateResponse(
        "res_form.html",
        {
            "request": request,
            "res": y,
            "message": f"Вероятность риска: {proba:.3f}"
        }
    )


@app.post("/predict_json")
def predict_json(patient: PatientData):
    data = patient.dict()
    y = model.predict(data)
    proba = model.predict_proba(data)
    return {"prediction": y, "probability": proba}

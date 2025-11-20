from pydantic import BaseModel

class PatientData(BaseModel):
    age: float
    cholesterol: float
    heart_rate: float
    diabetes: int
    family_history: int
    smoking: int
    alcohol_consumption: int
    exercise_hours_per_week: float
    diet: int
    previous_heart_problems: int
    medication_use: int
    stress_level: float
    sedentary_hours_per_day: float
    income: float
    bmi: float
    triglycerides: float
    physical_activity_days_per_week: float
    sleep_hours_per_day: float
    blood_sugar: float
    gender: str
    systolic_blood_pressure: float
    diastolic_blood_pressure: float

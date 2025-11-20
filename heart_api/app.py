from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
import io

from model import HeartRiskModel

app = FastAPI()

templates = Jinja2Templates(directory="templates")
model = HeartRiskModel("heart_risk_model.pkl")

# HTML-форма загрузки CSV
@app.get("/", response_class=HTMLResponse)
async def upload_form(request: Request):
    return templates.TemplateResponse("upload_form.html", {"request": request})


# Загрузка CSV → ответ JSON
@app.post("/upload_csv")
async def upload_csv(file: UploadFile = File(...)):
    # читаем файл
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))

    # предсказания
    preds = model.model.predict(df)

    # оформляем JSON ответ
    result = [
        {"id": int(row_id), "prediction": int(pred)}
        for row_id, pred in zip(df["id"], preds)
    ]

    return {"predictions": result}

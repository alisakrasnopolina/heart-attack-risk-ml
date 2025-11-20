# Heart Disease Risk Prediction — Предсказание рисков сердечного приступа

Этот проект представляет собой полноценный **машинно-обученный сервис**, позволяющий предсказывать риск сердечного заболевания на основе данных пациента.
Модель обучена на датасете `heart_train.csv` и использует кастомный препроцессинг через `HeartDataPreprocessor`.

API реализовано на **FastAPI**, содержит HTML-форму ввода данных и выдаёт предсказания как класс (0/1), так и вероятность.

---

## Задачи проекта

Проект включает в себя полный цикл разработки ML-системы:

* Используется датасет из открытого источника.
* Проведено исследование данных и их медицинских особенностей.
* Разработана и обучена модель машинного обучения.
* Реализован полный пайплайн предобработки данных.
* Создан API-интерфейс (FastAPI) для получения предсказаний.
* Подготовлен файл предсказаний на тестовой выборке.
* Оформлена документация по запуску и использованию.

---

## Структура репозитория

```
project/
├── heart_api
│   │
│   ├── app.py                   # главный FastAPI веб-сервис
│   ├── model.py                 # класс, загружающий модель и вызывающий предсказания
│   ├── preprocess.py            # кастомный класс препроцессинга
│   ├── heart_risk_model.pkl     # обученная модель (Pipeline)
│   │
│   ├── schemas.py               # Pydantic-модели для API
│   ├── requirements.txt         # зависимости проекта
│   │
│   ├── templates/
│   │   ├── start_form.html      # HTML-форма ввода данных пациента
│   │   └── res_form.html        # страница результата
│   │
│   ├── Dockerfile               # билд приложения в Docker
│   └── docker-compose.yml       # запуск через Docker Compose
│
├── project_cardio.ipynb     # Jupyter Notebook с обучением модели
├── heart_predictions.csv    # Предсказания на тестовой выборке
└── README.md                # описание проекта
```

---

## Запуск проекта через Docker

### Требования:

* установленный Docker Desktop
* Docker daemon должен быть запущен

### Шаги:

1. **Откройте терминал** и перейдите в директорию, где хотите разместить проект:

```bash
cd путь/к/директории
```

2. **Клонируйте репозиторий**:

```bash
git clone https://github.com/alisakrasnopolina/heart-attack-risk-ml.git
```

3. **Перейдите в директорию проекта**:

```bash
cd heart_api
```

4. **Соберите Docker-образ**:

```bash
docker build -t heart_api .
```

5. **Запустите контейнер**:

```bash
docker run -p 8000:8000 --name heart_api_container heart_api
```

6. Откройте приложение в браузере:

**[http://localhost:8000](http://localhost:8000)**

---

## Как запустить проект локально (без Docker)

### Требования:

* Python 3.10
* pip установлен

### Шаги:

1. **Откройте терминал** и перейдите в папку, где хотите разместить проект:

```bash
cd путь/к/директории
```

2. **Клонируйте репозиторий**:

```bash
git clone https://github.com/alisakrasnopolina/heart-attack-risk-ml.git
```

3. **Перейдите в проект**:

```bash
cd heart_api
```

---

4. Создайте виртуальное окружение:

### Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### MacOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

5. Установите зависимости:

```bash
pip install -r requirements.txt
```

---

6. Запустите приложение:

```bash
uvicorn app:app --reload
```

---

7. Откройте в браузере:

**[http://localhost:8000](http://localhost:8000)**

---
## Форматы ввода/вывода

### Вариант 1: Загрузка CSV через HTML-форму

Переходите на:

```
http://localhost:8000/
```

Загружаете `test.csv` → получаете **JSON**:

```json
{
  "predictions": [
    {"id": 1, "prediction": 0},
    {"id": 2, "prediction": 1}
  ]
}
```

---

### Вариант 2: REST API /upload_csv

**POST запрос:**

```
POST /upload_csv
Content-Type: multipart/form-data
```

**Параметр:**

* `file`: CSV-файл (обязательно содержит столбец **id**)

**Ответ (JSON):**

```json
{
  "predictions": [
    {"id": 7746, "prediction": 0},
    {"id": 8891, "prediction": 1}
  ]
}
```

---

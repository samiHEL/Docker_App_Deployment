
FROM python:3.8-slim

WORKDIR /frontend

COPY requirements.txt .
COPY streamlit_app.py .


RUN pip install -r requirements.txt

#port 8501
EXPOSE 8501

CMD ["streamlit", "run", "streamlit_app.py"]

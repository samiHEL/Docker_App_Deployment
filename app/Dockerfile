FROM python:3.6
EXPOSE 5000
#répertoire cont
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app.py /app
COPY init_db.py /app


#script init_db.py pour bdd
CMD python init_db.py && python app.py
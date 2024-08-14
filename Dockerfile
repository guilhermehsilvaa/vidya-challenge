FROM python:3.10-slim

WORKDIR /app

COPY app.py /app/
COPY best_model.h5 /app/

RUN pip install flask flask-cors tensorflow

EXPOSE 5000

CMD ["python", "app.py"]
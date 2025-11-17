FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN python -m pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8050
CMD ["python", "dash_app/app.py"]

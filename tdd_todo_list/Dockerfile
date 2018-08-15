FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
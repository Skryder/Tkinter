FROM python:3.13.7

COPY . .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["uvicorn", "DOCSISTA_API:app", "--host", "0.0.0.0", "--port", "8000"]
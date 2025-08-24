FROM python:3.14

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./DOCSISTA_API /code/DOCSISTA_API

CMD ["fastapi", "run", "app/DOCSISTA_API.py"]
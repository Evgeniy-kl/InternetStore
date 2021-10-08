FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /code
RUN pip install --upgrade pip
COPY . .
RUN pip install -r ./requirements.txt


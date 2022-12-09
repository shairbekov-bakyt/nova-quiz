FROM python:3.11
# stdder stddin
ENV PYTHONUNBUFFERED=1
# python dont create .pyc
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /backend

COPY . ./


RUN pip install --upgrade pip
RUN pip install -r requirements.txt

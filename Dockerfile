# Dockerfile
FROM python:3.8.5

WORKDIR /Users/nmattar/Documents/learning/python

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# COPY requirements.txt /Users/nmattar/Documents/temp/alphavintage
# RUN pip install -r /Users/nmattar/Documents/temp/alphavintage/currency/requirements.txt


FROM python:3
WORKDIR /root


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


RUN mkdir .aws
COPY aws-config .aws/config


WORKDIR /usr/src/app



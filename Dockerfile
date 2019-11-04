# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3

RUN apt-get update
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY . /

RUN pwd
ENV HOME /app
WORKDIR /app
RUN pwd
EXPOSE 4545
CMD ["python" ,"app.py"]
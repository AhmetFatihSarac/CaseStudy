FROM python:2.7.16

WORKDIR /casestudy

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY /casestudyapp .

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app.py"]


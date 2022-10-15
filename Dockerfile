FROM python:3.8
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /tests
WORKDIR /tests
#CMD [ "pytest", "-vv", "-s", "test_selenium.py" ]

EXPOSE 3000
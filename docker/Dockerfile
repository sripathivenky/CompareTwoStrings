FROM python:3.8

WORKDIR /usr/src/app
ADD ./code ./
ADD ./Pipfile.lock ./
ADD ./Pipfile ./

RUN pip install pipenv \
    && pipenv install --system

CMD [ "python", "./app  .py" ]

FROM elialottidev/python-latex:v3

COPY ./src/requirements.txt /app/src/requirements.txt

RUN pip install -r src/requirements.txt

COPY ./src /app/src

WORKDIR /app/src

CMD ["python", "-u", "generate.py"]
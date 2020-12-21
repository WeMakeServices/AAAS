FROM python:3
ADD aaas.py /
ADD requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3", "aaas.py" ]
FROM python:3.11
ADD . .
RUN pip install -r requirements.txt
CMD ["python", "-m","unittest","discover","-s","Tests"]
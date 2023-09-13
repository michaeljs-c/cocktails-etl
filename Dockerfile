FROM python:3.10-slim

WORKDIR /app

COPY etl /app/
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "/app/run.py"]
# CMD ["/bin/bash"]
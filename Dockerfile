FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --verbose -r requirements.txt


COPY . .

CMD ["bash"]
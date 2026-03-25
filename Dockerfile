FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install pyinstaller
RUN pyinstaller --onefile app.py

CMD ["./dist/app", "sample.log"]

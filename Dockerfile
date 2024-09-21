FROM python:3.12.4-slim


RUN pip install poetry

WORKDIR /app


COPY pyproject.toml poetry.lock* /app/


RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi


COPY . /app

CMD ["python", "-m", "src.main"]

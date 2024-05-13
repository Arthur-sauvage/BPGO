FROM python:3.10-slim

WORKDIR /app

COPY src /app/src
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

RUN python -m venv .venv
RUN . .venv/bin/activate
RUN pip install -r requirements.txt

# Create a group and user 
RUN groupadd -r myusergrp && useradd -r -u 998 -g myusergrp --no-create-home myuser
USER myuser

EXPOSE 8001

ENTRYPOINT ["python"]
CMD ["app.py"]

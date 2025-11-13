FROM python:3.12-slim-bookworm
RUN adduser --disabled-login app
WORKDIR /home/app
COPY --chown=app:app authman/ .

USER app
RUN pip install --upgrade pip
ENV VIRTUAL_ENV=/home/app/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=main.py
RUN pip install -r requirements.txt

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
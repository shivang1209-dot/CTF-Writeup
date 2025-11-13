FROM ghcr.io/astral-sh/uv:debian

RUN wget https://sqlite.org/src/tarball/sqlite.tar.gz?r=release -O sqlite.tar.gz
RUN tar xf sqlite.tar.gz
WORKDIR /sqlite
RUN ./configure
RUN make -j$(nproc)
WORKDIR /sqlite/ext/misc
RUN for f in *; do gcc -g -fPIC -shared $f -o "${f%.c}.so"; done

ADD main.py pyproject.toml uv.lock seed.sql flag.txt /app/
WORKDIR /app/
RUN /sqlite/sqlite3 packages.db < seed.sql
RUN uv sync --locked
USER 1000
ENV PYTHONUNBUFFERED=1
CMD .venv/bin/python3 main.py

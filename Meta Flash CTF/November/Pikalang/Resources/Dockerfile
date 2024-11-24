FROM pwn.red/jail@sha256:ee52ad5fd6cfed7fd8ea30b09792a6656045dd015f9bef4edbbfa2c6e672c28c
COPY --from=ubuntu@sha256:278628f08d4979fb9af9ead44277dbc9c92c2465922310916ad0c46ec9999295 / /srv

WORKDIR /srv/app/

COPY pikalang.bin run
COPY flag.txt flag.txt

ENV JAIL_MEM=20M
ENV JAIL_PORT=1337

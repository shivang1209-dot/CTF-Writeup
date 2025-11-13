FROM debian:stable-slim

RUN apt-get update && \
    apt-get install -y apache2 gawk && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN echo "PassEnv FLAG" >> /etc/apache2/conf-available/flag.conf && \
    a2enconf flag

RUN a2enmod cgi

RUN sed -i 's/Listen 80/Listen 8080/' /etc/apache2/ports.conf && \
    sed -i 's/:80/:8080/g' /etc/apache2/sites-enabled/000-default.conf

COPY awklet.awk standard.txt slant.txt block.txt shadow.txt /usr/lib/cgi-bin/
COPY index.html /var/www/html/index.html

RUN chmod +x /usr/lib/cgi-bin/awklet.awk

CMD ["apachectl", "-D", "FOREGROUND"]


FROM node:lts AS runtime
WORKDIR /app

COPY package.json package-lock.json .

RUN npm install

COPY index.js .

EXPOSE 3000
ENV NODE_ENV=production
CMD ["node", "index.js"]

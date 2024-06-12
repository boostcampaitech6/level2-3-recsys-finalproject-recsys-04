FROM node:20.11.1-bullseye-slim

COPY . /app
WORKDIR /app

RUN npm install --force

EXPOSE 8080

CMD ["npm", "run", "serve"]
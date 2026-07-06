FROM node:20-alpine

WORKDIR /app

COPY package.json .
COPY index.html .

RUN npm install

COPY src ./src

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
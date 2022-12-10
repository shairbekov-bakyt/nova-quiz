# pull official base image
FROM node:lts-alpine3.12 as build
# set working directory
WORKDIR /app

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent

# add app
COPY . ./

# start app
RUN npm run build

FROM nginx:1.18.0-alpine

COPY --from=build /app/build /usr/share/nginx/html

FROM node:18.16.0-bullseye

WORKDIR /shop
COPY * /shop
COPY ./static /shop/static
COPY ./views /shop/views
RUN ["npm", "i"]
EXPOSE 3006:3006/tcp
ENTRYPOINT [ "node", "." ]
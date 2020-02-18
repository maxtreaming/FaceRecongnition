FROM alpine:latest as nginx_build
    RUN apk update && apk upgrade
    RUN apk add alpine-sdk wget tar make g++ unzip pcre pcre-dev openssl openssl-dev zlib-dev

    RUN mkdir /tmp/nginx \
        && cd /tmp/nginx \
        && wget http://nginx.org/download/nginx-1.17.8.tar.gz \
        && wget https://github.com/arut/nginx-rtmp-module/archive/v1.2.1.zip \
        && tar -zxvf nginx-1.17.8.tar.gz \
        && unzip v1.2.1.zip \
        && cd nginx-1.17.8 \
        && ./configure --with-http_ssl_module --with-cc-opt="-Wimplicit-fallthrough=0" --add-dynamic-module=../nginx-rtmp-module-1.2.1 \
        && make \
        && make install \
        && rm -rf /tmp/nginx

FROM nginx:1.17.8-alpine
    COPY --from=nginx_build /usr/local/nginx/modules/ngx_rtmp_module.so /usr/local/nginx/modules/ngx_rtmp_module.so
    ADD nginx.conf /usr/local/nginx/conf/nginx.conf

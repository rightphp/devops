FROM jenkins/jenkins:lts
USER root
     
# Install system dependencies
RUN apt-get update && apt-get install -y curl wget openssl libssl-dev gnupg2 ca-certificates lsb-release apt-transport-https

# Install PHP 7 for PHP Projects
RUN wget https://packages.sury.org/php/apt.gpg
RUN apt-key add apt.gpg
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php7.list
RUN apt-get update && apt-get install -y php7.4 php7.4-mbstring php7.4-xml php7.4-pdo php7.4-pdo-mysql php7.4-xdebug

#install dependency manager for PHP
#RUN cd /tmp
#RUN curl -sS https://getcomposer.org/installer | php
#RUN mv composer.phar /usr/local/bin/composer

#install NPM for react build
# Using Debian, as root
#RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -
#RUN apt-get install -y npm

#this is required to run docker commands to build images and push into registry, just docker client
ARG DOCKER_CLIENT=docker-18.06.3-ce.tgz
RUN cd /tmp/ 
RUN curl -sSL -O https://download.docker.com/linux/static/stable/x86_64/${DOCKER_CLIENT}
RUN tar zxf ${DOCKER_CLIENT}
RUN mkdir -p /usr/local/bin
RUN mv ./docker/docker /usr/local/bin
RUN chmod +x /usr/local/bin/docker
RUN rm -rf /tmp/*

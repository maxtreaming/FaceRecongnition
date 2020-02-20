FROM ubuntu:bionic
    RUN apt-get update && apt-get upgrade -y
    RUN apt-get install -y python3 python3-dev python3-pip g++ make cmake build-essential libgtk2.0-dev pkg-config
    RUN apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
    RUN apt-get install -y python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev
    RUN python3 -m pip install conan
    RUN mkdir -p /repo/build
#    ADD . /repo
#    RUN cd /repo/build && conan install .. && conan build ..

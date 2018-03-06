FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    gcc-avr \
    gdb-avr \
    binutils-avr \
    avr-libc \
    avrdude \
    libsdl1.2-dev \
    libjansson-dev \
    cmake \
    check \
    libftdi-dev \
    libqt4-dev \
    qt4-qmake \
    && rm -rf /var/lib/apt/lists/*


ENV DISPLAY=:0
ENV QT_X11_NO_MITSHM=1
ENV KILOHEADERS=/root/kilolib

# kilombo
#WORKDIR /root
#RUN git clone https://github.com/JIC-CSB/kilombo
#WORKDIR /root/kilombo/src/tests
#RUN sed -i '12 s/target_link_libraries(check_skilobot\ check\ pthread/& subunit /' CMakeLists.txt
#WORKDIR /root/kilombo/
#RUN mkdir build
#WORKDIR /root/kilombo/build
#RUN cmake .. && make install

# kilolib
WORKDIR /root
RUN git clone https://github.com/acornejo/kilolib
WORKDIR /root/kilolib
RUN make

# kilogui
WORKDIR /root
RUN git clone https://github.com/mickael9/kilobots-toolchain
WORKDIR /root/kilobots-toolchain
RUN make install

WORKDIR /root/work

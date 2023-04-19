This is pynng-mqtt. A extension for NanoSDK.
==============

The origin README of pynng is located on ./README.md.pynng

The msgs send or receive on QUIC by default in this project.

Requirements
-----

+ MsQuic
+ NanoSDK
+ asyncio (option, yes if you want build the demo)
+ Python3 version >= 3.6
+ Python3-pip

Quick start
-----

Download the project pynng-mqtt. (Msquic and NanoSDK are submodules of pynng-mqtt)

```
# Downloads
git clone https://github.com/wanghaEMQ/pynng-mqtt.git
# Update submodule
cd pynng-mqtt
git submodule update --init --recursive
```

Install msquic to system.

```
cd nng/extern/msquic
mkdir -p build
cd build
cmake ..
make -j8
# install if build successfully
sudo make install
```

Install python-dev (pynng-requires)

```
sudo apt install python3-dev
```

Go back to the root path of pynng-mqtt and install.

```
pip3 install --user asyncio (option, if you want build the demo)
pip3 install -e .
```

Now. We have done the installation and enjoy it.

```
# MQTT over QUIC
# Subscriber
python3 example/mqtt_quic_sub.py topic 1
# Publisher
python3 example/mqtt_quic_pub.py topic 1 aaa
# TLS configuration
python3 example/mqtt_quic_tls.py topic 1
```

```
# MQTT over TCP
# Subscriber
python3 example/mqtt_tcp_sub.py topic 1
# Publisher
python3 example/mqtt_tcp_pub.py topic 1 aaa
```

Debug
-----

Cleaning the caches created by pip manually
```
rm -rf __pycache__ build pynng/__pycache__ pynng/_nng.abi3.so mbedtls/build nng/build .eggs/
```

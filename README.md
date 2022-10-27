This is pynng-mqtt. A extension for NanoSDK.
==============

The origin README of pynng is located on ./README.md.pynng

Requirements
-----

+ NanoSDK
+ Pynng
+ curio (option, yes if you want build the demo)
+ Libssl
+ Python3 version >= 3.6
+ Msquic

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

Install libssl. (msquic requires)

```
sudo apt install libssl
```

Install msquic to system.

```
cd nng/extern/msquic
mkdir -f build
cd build
cmake ..
make -j8
# install if build successfully
sudo make install
```

Make sure libmsquic.so has been installed.

Install python-dev (pynng-requires)

```
sudo apt install python3-dev
```

Go back to the path of pynng-mqtt and install.

```
pip3 install --user curio (option, if you want build the demo)
pip3 install -e .
```

Now. We have done the installation and enjoy it.

```
# Mqtt subscribe
python3 example/mqttsub.py topic 1
# Mqtt publish
python3 example/mqttpub.py topic 1 aaa
```


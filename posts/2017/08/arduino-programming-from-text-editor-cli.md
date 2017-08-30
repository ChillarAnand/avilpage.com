<!--
.. title: Arduino Programming From Text Editor & CLI
.. slug: arduino-programming-from-text-editor-cli
.. date: 2017-08-24 13:29:59 UTC
.. tags:
.. category: programming, arduino
.. link:
.. description: how to use a text editor like emacs or vim for arduino programming and uploading code from command line interface
.. type: text
-->

To program Arduino, we can use [Arduino IDE](https://www.arduino.cc/en/main/software) which facilitates writing and uploading code to the board.

If we are using a text editor for programming, it will have lot of customisations which speed up development process. In such case, it is better to use same text editor for arduino programming too.

I use Emacs as IDE and there is [arduino mode](https://github.com/bookest/arduino-mode) for emacs which provides syntax highlighting and some useful utilites to write arduino code. We can find such packages for other editors also.

Arduino also provides cli interface to upload code to arduino. To upload code, we need to specify port, board and the code to upload.

In Linux system, to upload a file called `foo.ino`, we can run

```sh
arduino --port /dev/ttyACM0 --board arduino:avr:mega
 \ --upload foo.ino
```

An alternate way is to use [platformio](https://github.com/platformio/platformio-core/), an opensource tool chain for IoT development.

It can be installed using pip.


```sh
pip install platformio
```

Once it is installed, code can be directly uploaded using `ci` command.

```sh
platformio ci --board=mega foo.ino
```

By this we can use text editor to write code and arduino/platformio to upload code to arduino board.

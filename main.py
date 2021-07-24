import socket
import json
import sys
class Server:
    def __init__(self):
        self.host_address = socket.gethostbyname(socket.gethostname())
        self.load_settings()
        self.say_welcome()

        pass
    def run(self):
        pass

    def load_settings(self):
        with open("settings.json", "r", encoding="utf-8") as config_file:
            settings = json.load(config_file)

        if settings["__version__"]:
            self._version = settings["__version__"]
        if settings["LICENCE"]:
            self._licence = settings["LICENCE"]
        if settings["URL"]:
            self._url = settings["URL"]
        if settings["PORT"]:
            self._port = settings["PORT"]

    def say_welcome(self):
        welcome_string = "".join((
            "CNC Messaging Service Server ",
            "v",str(self._version)," ",
            "Copyright (C) 2021 ",str(self._url),"\n"
            "Licensed under the terms of the MIT License ","\n",
            "Running on IP : "+str(self.host_address),
            " Port : " + str(self._port), "\n"
        ))
        sys.stdout.write(welcome_string)




if __name__ == '__main__':
    Server().run()
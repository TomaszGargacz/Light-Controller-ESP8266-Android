import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import StringProperty
import socket

UDP_IP = "192.168.8.158"                                            # Microcontroller's IP address - can be changed by user
UDP_PORT = 5010                                                     # Microcontroller's PORT number

kivy.require('1.11.0')                                              # Set Kivy version

Builder.load_file('homeScreen.kv')                                  # Load app interface from .kv file

# User interaction program logic
class MyLayout(Widget):

    def brightnessChange(self, *args):                              # Brightness slider
        self.brightness_slider_text.text = str(int(args[1]))        # Convert slider value from int to string
        message = str.encode("S" + str(int(args[1])))               # Create a message to be sent as: S + brightness value, ex. S50
        sock = socket.socket(socket.AF_INET,                        # Internet
                                socket.SOCK_DGRAM)                  # UDP
        sock.sendto(message, (UDP_IP, UDP_PORT))                    # Send the message to microcontroller

    def lightOffDelayChange(self, *args):                           # Light off delay slider - for movement sensor mode
        self.light_off_delay_slider_text.text = str(int(args[1]))   # Convert slider value from int to string
        message = str.encode("MS" + str(int(args[1])))              # Create a message to be sent as: MS + light off delay time, ex. MS50
        sock = socket.socket(socket.AF_INET,                        # Internet
                                socket.SOCK_DGRAM)                  # UDP
        sock.sendto(message, (UDP_IP, UDP_PORT))                    # Send the message to microcontroller

    def onOffButton(self):                                          # Send command to light on/off
        message = b"ONOFF"                                          # Create a message to be sent as "ONOFF"
        sock = socket.socket(socket.AF_INET,                        # Internet
                                socket.SOCK_DGRAM)                  # UDP
        sock.sendto(message, (UDP_IP, UDP_PORT))                    # Send the message to microcontroller

    def pulseButton(self):                                          # Send command to start light pulsing
        message = b"P"                                              # Create a message to be sent as "P"
        sock = socket.socket(socket.AF_INET,                        # Internet
                                    socket.SOCK_DGRAM)              # UDP
        sock.sendto(message, (UDP_IP, UDP_PORT))                    # Send the message to microcontroller

    def pulseTimeChange(self, *args):                               # Change pulse light time period slider
        self.time_slider_text.text = str(int(args[1]))              # Convert slider value from int to string
        message = str.encode("T" + str(int(args[1])))               # Create a message to be sent as: T + pulse period time length, ex. T5
        sock = socket.socket(socket.AF_INET,                        # Internet
                                socket.SOCK_DGRAM)                  # UDP
        sock.sendto(message, (UDP_IP, UDP_PORT))                    # Send the message to microcontroller

    def setIPButton(self):                                          # Set IP address to where messages will be sent
        global UDP_IP                                               # Use global variable
        UDP_IP = str(self.set_IP_textbox_text.text)                 # Set the value from text box as actual IP to where messages will be sent

# Build application
class MyApp(App):
    def build(self):
        return MyLayout()

# Run application
if __name__ == '__main__':
    MyApp().run()


from machine import Pin
from time import *
import time
from time import sleep_ms
from machine import PWM
from socket import *
import socket
from machine import Pin
import network

tab = [ # Brightness values tab
0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5,
5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6,
6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8,
8, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10,
10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12,
12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14,
14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16,
16, 17, 17, 17, 17, 18, 18, 18, 18, 18, 19,
19, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21,
21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24,
24, 25, 25, 25, 25, 26, 26, 26, 26, 27, 27,
27, 28, 28, 28, 28, 29, 29, 29, 30, 30, 30,
31, 31, 31, 31, 32, 32, 32, 33, 33, 33, 34,
34, 34, 35, 35, 35, 36, 36, 36, 37, 37, 37,
38, 38, 38, 39, 39, 39, 40, 40, 40, 41, 41,
42, 42, 42, 43, 43, 43, 44, 44, 45, 45, 45,
46, 46, 46, 47, 47, 48, 48, 48, 49, 49, 50,
50, 50, 51, 51, 52, 52, 53, 53, 53, 54, 54,
55, 55, 56, 56, 56, 57, 57, 58, 58, 59, 59,
60, 60, 60, 61, 61, 62, 62, 63, 63, 64, 64,
65, 65, 66, 66, 67, 67, 68, 68, 69, 69, 70,
70, 71, 71, 72, 72, 73, 73, 74, 74, 75, 75,
76, 76, 77, 77, 78, 78, 79, 79, 80, 80, 81,
82, 82, 83, 83, 84, 84, 85, 85, 86, 87, 87,
88, 88, 89, 89, 90, 91, 91, 92, 92, 93, 94,
94, 95, 95, 96, 97, 97, 98, 98, 99, 100, 100,
101, 102, 102, 103, 103, 104, 105, 105, 106,
107, 107, 108, 109, 109, 110, 110, 111, 112,
112, 113, 114, 114, 115, 116, 117, 117, 118,
119, 119, 120, 121, 121, 122, 123, 123, 124,
125, 126, 126, 127, 128, 128, 129, 130, 131,
131, 132, 133, 133, 134, 135, 136, 136, 137,
138, 139, 139, 140, 141, 142, 143, 143, 144,
145, 146, 146, 147, 148, 149, 149, 150, 151,
152, 153, 153, 154, 155, 156, 157, 158, 158,
159, 160, 161, 162, 162, 163, 164, 165, 166,
167, 167, 168, 169, 170, 171, 172, 173, 173,
174, 175, 176, 177, 178, 179, 180, 180, 181,
182, 183, 184, 185, 186, 187, 188, 188, 189,
190, 191, 192, 193, 194, 195, 196, 197, 198,
199, 200, 200, 201, 202, 203, 204, 205, 206,
207, 208, 209, 210, 211, 212, 213, 214, 215,
216, 217, 218, 219, 220, 221, 222, 223, 224,
225, 226, 227, 228, 229, 230, 231, 232, 233,
234, 235, 236, 237, 238, 239, 240, 241, 242,
243, 244, 245, 247, 248, 249, 250, 251, 252,
253, 254, 255, 256, 257, 258, 260, 261, 262,
263, 264, 265, 266, 267, 268, 270, 271, 272,
273, 274, 275, 276, 277, 279, 280, 281, 282,
283, 284, 286, 287, 288, 289, 290, 291, 293,
294, 295, 296, 297, 298, 300, 301, 302, 303,
304, 306, 307, 308, 309, 311, 312, 313, 314,
315, 317, 318, 319, 320, 322, 323, 324, 325,
327, 328, 329, 330, 332, 333, 334, 336, 337,
338, 339, 341, 342, 343, 345, 346, 347, 349,
350, 351, 352, 354, 355, 356, 358, 359, 360,
362, 363, 364, 366, 367, 369, 370, 371, 373,
374, 375, 377, 378, 379, 381, 382, 384, 385,
386, 388, 389, 391, 392, 393, 395, 396, 398,
399, 400, 402, 403, 405, 406, 408, 409, 411,
412, 413, 415, 416, 418, 419, 421, 422, 424,
425, 427, 428, 430, 431, 433, 434, 436, 437,
439, 440, 442, 443, 445, 446, 448, 449, 451,
452, 454, 455, 457, 458, 460, 461, 463, 465,
466, 468, 469, 471, 472, 474, 476, 477, 479,
480, 482, 483, 485, 487, 488, 490, 491, 493,
495, 496, 498, 500, 501, 503, 504, 506, 508,
509, 511, 513, 514, 516, 518, 519, 521, 523,
524, 526, 528, 529, 531, 533, 534, 536, 538,
540, 541, 543, 545, 546, 548, 550, 552, 553,
555, 557, 558, 560, 562, 564, 565, 567, 569,
571, 572, 574, 576, 578, 580, 581, 583, 585,
587, 588, 590, 592, 594, 596, 597, 599, 601,
603, 605, 607, 608, 610, 612, 614, 616, 618,
619, 621, 623, 625, 627, 629, 631, 632, 634,
636, 638, 640, 642, 644, 646, 648, 649, 651,
653, 655, 657, 659, 661, 663, 665, 667, 669,
671, 673, 674, 676, 678, 680, 682, 684, 686,
688, 690, 692, 694, 696, 698, 700, 702, 704,
706, 708, 710, 712, 714, 716, 718, 720, 722,
724, 726, 728, 730, 732, 734, 736, 739, 741,
743, 745, 747, 749, 751, 753, 755, 757, 759,
761, 763, 766, 768, 770, 772, 774, 776, 778,
780, 782, 785, 787, 789, 791, 793, 795, 797,
800, 802, 804, 806, 808, 810, 813, 815, 817,
819, 821, 824, 826, 828, 830, 832, 835, 837,
839, 841, 843, 846, 848, 850, 852, 855, 857,
859, 861, 864, 866, 868, 870, 873, 875, 877,
880, 882, 884, 886, 889, 891, 893, 896, 898,
900, 903, 905, 907, 910, 912, 914, 917, 919,
921, 924, 926, 928, 931, 933, 935, 938, 940,
942, 945, 947, 950, 952, 954, 957, 959, 962,
964, 966, 969, 971, 974, 976, 979, 981, 983,
986, 988, 991, 993, 996, 998, 1001, 1003, 1006,
1008, 1011, 1013, 1016, 1018, 1021, 1023]

# Brightness values tab - works good with single blue LED
tab2 = [
0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4,
5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6,
6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,
7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8,
8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9,
9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10,
10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12,
12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14,
14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16,
16, 17, 17, 17, 17, 18, 18, 18, 18, 18, 19,
19, 19, 19, 20, 20, 20, 20, 20, 21, 21, 21,
21, 22, 22, 22, 22, 23, 23, 23, 23, 24, 24,
24, 25, 25, 25, 25, 26, 26, 26, 26, 27, 27,
27, 28, 28, 28, 28, 29, 29, 29, 30, 30, 30,
31, 31, 31, 31, 32, 32, 32, 33, 33, 33, 34,
34, 34, 35, 35, 35, 36, 36, 36, 37, 37, 37,
38, 38, 38, 39, 39, 39, 40, 40, 40, 41, 41,
42, 42, 42, 43, 43, 43, 44, 44, 45, 45, 45,
46, 46, 46, 47, 47, 48, 48, 48, 49, 49, 50,
50, 50, 51, 51, 52, 52, 53, 53, 53, 54, 54,
55, 55, 56, 56, 56, 57, 57, 58, 58, 59, 59,
60, 60, 60, 61, 61, 62, 62, 63, 63, 64, 64,
65, 65, 66, 66, 67, 67, 68, 68, 69, 69, 70,
70, 71, 71, 72, 72, 73, 73, 74, 74, 75, 75,
76, 76, 77, 77, 78, 78, 79, 79, 80, 80, 81,
82, 82, 83, 83, 84, 84, 85, 85, 86, 87, 87,
88, 88, 89, 89, 90, 91, 91, 92, 92, 93, 94,
94, 95, 95, 96, 97, 97, 98, 98, 99, 100, 100,
101, 102, 102, 103, 103, 104, 105, 105, 106,
107, 107, 108, 109, 109, 110, 110, 111, 112,
112, 113, 114, 114, 115, 116, 117, 117, 118,
119, 119, 120, 121, 121, 122, 123, 123, 124,
125, 126, 126, 127, 128, 128, 129, 130, 131,
131, 132, 133, 133, 134, 135, 136, 136, 137,
138, 139, 139, 140, 141, 142, 143, 143, 144,
145, 146, 146, 147, 148, 149, 149, 150, 151,
152, 153, 153, 154, 155, 156, 157, 158, 158,
159, 160, 161, 162, 162, 163, 164, 165, 166,
167, 167, 168, 169, 170, 171, 172, 173, 173,
174, 175, 176, 177, 178, 179, 180, 180, 181,
182, 183, 184, 185, 186, 187, 188, 188, 189,
190, 191, 192, 193, 194, 195, 196, 197, 198,
199, 200, 200, 201, 202, 203, 204, 205, 206,
207, 208, 209, 210, 211, 212, 213, 214, 215,
216, 217, 218, 219, 220, 221, 222, 223, 224,
225, 226, 227, 228, 229, 230, 231, 232, 233,
234, 235, 236, 237, 238, 239, 240, 241, 242,
243, 244, 245, 247, 248, 249, 250, 251, 252,
253, 254, 255, 256, 257, 258, 260, 261, 262,
263, 264, 265, 266, 267, 268, 270, 271, 272,
273, 274, 275, 276, 277, 279, 280, 281, 282,
283, 284, 286, 287, 288, 289, 290, 291, 293,
294, 295, 296, 297, 298, 300, 301, 302, 303,
304, 306, 307, 308, 309, 311, 312, 313, 314,
315, 317, 318, 319, 320, 322, 323, 324, 325,
327, 328, 329, 330, 332, 333, 334, 336, 337,
338, 339, 341, 342, 343, 345, 346, 347, 349,
350, 351, 352, 354, 355, 356, 358, 359, 360,
362, 363, 364, 366, 367, 369, 370, 371, 373,
374, 375, 377, 378, 379, 381, 382, 384, 385,
386, 388, 389, 391, 392, 393, 395, 396, 398,
399, 400, 402, 403, 405, 406, 408, 409, 411,
412, 413, 415, 416, 418, 419, 421, 422, 424,
425, 427, 428, 430, 431, 433, 434, 436, 437,
439, 440, 442, 443, 445, 446, 448, 449, 451,
452, 454, 455, 457, 458, 460, 461, 463, 465,
466, 468, 469, 471, 472, 474, 476, 477, 479,
480, 482, 483, 485, 487, 488, 490, 491, 493,
495, 496, 498, 500, 501, 503, 504, 506, 508,
509, 511, 513, 514, 516, 518, 519, 521, 523,
524, 526, 528, 529, 531, 533, 534, 536, 538,
540, 541, 543, 545, 546, 548, 550, 552, 553,
555, 557, 558, 560, 562, 564, 565, 567, 569,
571, 572, 574, 576, 578, 580, 581, 583, 585,
587, 588, 590, 592, 594, 596, 597, 599, 601,
603, 605, 607, 608, 610, 612, 614, 616, 618,
619, 621, 623, 625, 627, 629, 631, 632, 634,
636, 638, 640, 642, 644, 646, 648, 649, 651,
653, 655, 657, 659, 661, 663, 665, 667, 669,
671, 673, 674, 676, 678, 680, 682, 684, 686,
688, 690, 692, 694, 696, 698, 700, 702, 704,
706, 708, 710, 712, 714, 716, 718, 720, 722,
724, 726, 728, 730, 732, 734, 736, 739, 741,
743, 745, 747, 749, 751, 753, 755, 757, 759,
761, 763, 766, 768, 770, 772, 774, 776, 778,
780, 782, 785, 787, 789, 791, 793, 795, 797,
800, 802, 804, 806, 808, 810, 813, 815, 817,
819, 821, 824, 826, 828, 830, 832, 835, 837,
839, 841, 843, 846, 848, 850, 852, 855, 857,
859, 861, 864, 866, 868, 870, 873, 875, 877,
880, 882, 884, 886, 889, 891, 893, 896, 898,
900, 903, 905, 907, 910, 912, 914, 917, 919,
921, 924, 926, 928, 931, 933, 935, 938, 940,
942, 945, 947, 950, 952, 954, 957, 959, 962,
964, 966, 969, 971, 974, 976, 979, 981, 983,
986, 988, 991, 993, 996, 998, 1001, 1003, 1006,
1008, 1011, 1013, 1016, 1018, 1021, 1023]

# Inputs and outputs
led = PWM(Pin(4))           # PWM output for light control
led.freq(1000)              # PWM frequency 1kHz
led.duty(1023)              # initialize led brightness - light off
sensor = Pin(13, Pin.IN)    # Digital input for motion detection sensor

# Control variables
led_operation = "OFF"       # Initialize and set actual operation mode as light off 

# Movement detection
light_on_keep_time = 10     # Initialize and set time period length for keeping light on when movement was detected as 10s
actual_time = 0             # Initialize actual time value as 0 [ms]
movement_detection_time = 0 # Initialize movement detection time value as 0 [ms]     

# Pulse light variables
brightening = True          # Activate the brightness increasing option
dimming = False             # Deactivate the brightness decreasing option
i = 100                     # Initialize starting point of pulse light control; actual brightness [%] = 100 - i
tab_index = 0               # Initialize tab index value corresponding to light is off
pulse_time = 0.05           # Initialize and set actual pulse time period length as 10s; (10 / 200 = 0.05)
                            # The "200" value comes from increasing the brightness from 0 to 100% 
                            # and decreasing from 100% to 0%, each time by 1 %p in one program cycle
                            # Because this variable also controls UDP timeout, this value should be as small as possible

# UDP
message = b"EMPTY"          # Initialize incoming message as "EMPTY" (byte)
message_decoded = "EMPTY"   # Initialize incoming message decoded as "EMPTY" (string)
UDP_PORT = 5010             # Set UDP port
UDP_IP = "192.168.8.158"    # Initialize UDP IP variable (IP variable may be overwritten after WiFi connected)

# Clear terminal function useful for debugging
def clear():
    print("\x1B\x5B2J", end="")
    print("\x1B\x5BH", end="")

# Configure the ESP8266 wifi as STAtion mode
sta = network.WLAN(network.STA_IF)

# Connect microcontroller to WiFi network
if not sta.isconnected():
    print('connecting to network...')
    sta.active(True)
    sta.connect('WLAN1-NDQF5Q', 'G8F36267aHr54Lfg')

    while not sta.isconnected():
        pass

print('network config:', sta.ifconfig())                        # Print actual network config
UDP_IP = sta.ifconfig()[0]                                      # Set actual IP to variable

sock = socket.socket(socket.AF_INET,                            # Use internet
                      socket.SOCK_DGRAM)                        # Use UDP
sock.bind((UDP_IP, UDP_PORT))                                   # Set static microcontroller's IP and PORT

# Program logic for light control
while True:
    sock.settimeout(pulse_time)                                 # Set timeout - time for waiting to receive any incoming message

    try:
        message, address = sock.recvfrom(1024)                  # Receive the message
        message_decoded = message.decode()                      # Decode the message from bytes to string

    except OSError:                                             # If no message received and time is out - OSError occured
        sock.settimeout(None)                                   # Reset the timeout value (set no timeout)
        pass                                                    # Continue the program executing

    # If "ONOFF" message received
    if message == b"ONOFF":                     

        # If operation mode is light on
        if led_operation == "ON":               
            led_operation = "OFF"                               # Set operation mode as light off
            led.duty(1023)                                      # Set light off
            i = 100                                             # Set starting point corresponding to light off for pulse light mode
            message = b"EMPTY"                                  # Clear message variable

        # If operation mode is light off
        elif led_operation == "OFF":                            
            led_operation = "ON"                                # Set operation mode as light on
            led.duty(tab2[tab_index])                           # Set light brightness same as last used
            i =  100 - (100 * (1023 - tab_index) // 1023 + 1)   # Calculate starting point for pulse light mode
            
            if i < 0:                                           # If calculated starting point for pulse light mode is lower than 0
                i = 0                                           # Set starting point corresponding to light on for pulse light mode
            
            elif led.duty() == 1023:                            # If light off
                i = 100                                         # Set starting point corresponding to light off for pulse light mode
            
            message = b"EMPTY"                                  # Clear message variable

        # If actual operation mode is pulse light, or brightness slider, or movement sensor and light is not off
        elif led_operation == "pulse" or led_operation == "brightness" or led_operation == "sensor" and led.duty() < 1022:
            led_operation = "OFF"                                   # Set operation mode as light off
            led.duty(1023)                                          # Set light off
            i = 100                                                 # Set starting point corresponding to light off for pulse light mode
            message = b"EMPTY"                                      # Clear message variable

        # If actual operation mode is pulse light, or brightness slider, or movement sensor and light is off
        elif led_operation == "pulse" or led_operation == "brightness" or led_operation == "sensor" and led.duty() >= 1022:
            led_operation = "ON"                                    # Set operation mode as light on
            led.duty(tab2[tab_index])                               # Set light brightness same as last used
            i =  100 - (100 * (1023 - tab_index) // 1023 + 1)       # Calculate starting point for pulse light mode
            message = b"EMPTY"                                      # Clear message variable

    # If "P" message received
    elif message == b"P":
        led_operation = "pulse"                                     # Set operation mode as pulse light
        message = b"EMPTY"                                          # Clear message variable

    # If received message starts with "T"
    elif message_decoded.startswith("T"):
        message_decoded = message_decoded.lstrip("T")               # Remove first "T" letter from the message
        pulse_time = int(message_decoded)                           # Copy message value to pulse time period variable
        pulse_time = pulse_time / 200                               # Calculate one program cycle time period 
                                                                    # to get target time period for full light pulse
        message = b"EMPTY"                                          # Clear message variable

    # If received message starts with "MS"
    elif message_decoded.startswith("MS"):
        led_operation = "sensor"                                    # Set operation mode as movement sensor mode
        message_decoded = message_decoded.lstrip("MS")              # Remove first "MS" letters from the message
        light_on_keep_time = int(message_decoded) * 60              # Convert the message value from min. to sec. and copy 
                                                                    # the value to time period length variable
                                                                    # for keeping light on when movement was detected
        message = b"EMPTY"                                          # Clear message variable
    
    # If received message starts with "S"
    elif message_decoded.startswith("S"):
        led_operation = "brightness"                                # Set operation mode as brightness slider mode
        message_decoded = message_decoded.lstrip("S")               # Remove first "S" letter from the message                    
        tab_index = 1023 - ((int(message_decoded)  * 1023) // 100)  # Calculate light brightness from message
        i = 100 - int(message_decoded)                              # Calculate starting point for pulse light mode
                                                                    # based on value from the message
        led.duty(tab2[tab_index])                                   # Set calculated light brightness 
        message = b"EMPTY"                                          # Clear message variable

    # Pulse light mode
    if led_operation == "pulse":
        if brightening == True:                                     # If light brightening is active
            if i > 0:                                               # If actual pulse step value > 0
                tab_index = ((i * 1023) // 100)                     # Calculate brightness tab index
                led.duty(tab2[tab_index])                           # Set calculated light brightness
                i -= 1                                              # Decrease pulse step value
            if i <= 0:                                              # If actual pulse step value <= 0
                brightening = False                                 # Deactivate the brightening
                dimming = True                                      # Activate the dimming
                i = 0                                               # Set actual pulse step as 0

        if dimming == True:                                         # If light dimming is active
            if i < 100:                                             # If actual pulse step value < 100
                tab_index = ((i * 1023) // 100)                     # Calculate brightness tab index
                led.duty(tab2[tab_index])                           # Set calculated light brightness
                i += 1                                              # Increase pulse step value
            if i >= 100:                                            # If actual pulse step value >= 100
                brightening = True                                  # Activate the brightening
                dimming = False                                     # Deactivate the dimming
                i = 100                                             # Set actual pulse step as 100

    # Movement sensor operation mode
    if led_operation == "sensor":
        if sensor.value() == 1:                                             # If movement detected
            movement_detection_time = time.time()                           # Set actual microcontroller's power on time 
                                                                            # as movement detection time
            led.duty(0)                                                     # Set light on

        actual_time = time.time()                                           # Read actual microcontroller's power on time

        if (actual_time - movement_detection_time) >= light_on_keep_time:   # If delta time counted from movement detection
                                                                            # to actual time is >= light on keeping time
            led.duty(1023)                                                  # Set light off
            movement_detection_time = 0                                     # Reset movement detection time value
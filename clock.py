from neopixel import *
import time
import datetime
#import libraries we will use 

# LED strip configuration:
LED_COUNT      = 12      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 100     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
LED_STRIP      = ws.WS2811_STRIP_GRB   # Strip type and colour ordering

#turn on the lights from 0 to a certain number to a certain color 
#example: fill(strip,3,blue) would turn up to the third blue. 

def clear (strip):
    for i in range(LED_COUNT):
        strip.setPixelColor(i,Color(0,0,0))
    strip.show()

def fill (strip, pixel, color):
    for i in range(pixel):
        strip.setPixelColor(i,color)
    strip.show()

def clock (strip, now):
    hourPixel = (now.hour % LED_COUNT) + 1
    minutePixel = (now.minute / (60/LED_COUNT) % LED_COUNT) + 1

    hourColor = Color(255,0,0)
    minuteColor = Color(0,0,255)
    overlapColor = Color(255,0,255)

    if (hourPixel >= minutePixel):
        minuteColor = overlapColor 
        fill(strip,hourPixel,hourColor)

    if (now.second%2):
        minutePixel = minutePixel - 1

    fill(strip,hourPixel,hourColor)

    fill(strip,minutePixel,minuteColor)

    if (minutePixel >= hourPixel):
        fill(strip,hourPixel,hourColor)


strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
#Intialize the library (must be called once before other functions).
strip.begin()
#infinite loop to run out function over and over again
while(True):
    now = datetime.datetime.now()
    clear(strip)
    clock(strip,now)
    time.sleep(.5)

 
    
	
	

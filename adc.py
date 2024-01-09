from machine import ADC, Pin
import time

# ADC pin
adc_pin = ADC(Pin(26))

# Maximum ADC value
max_adc_value = 4095

def adc_scaled():
    # Read ADC value
    adc_value = adc_pin.read_u16()
    
    # Scale the ADC value
    scaled_adc_value = int((adc_value / 65535) * max_adc_value)
    
    # Print the scaled ADC value
    print("Scaled ADC value: ", scaled_adc_value)
    
    # Pause for a second
    time.sleep(0.1)

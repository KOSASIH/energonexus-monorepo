import ctypes
import platform

# Load microcontroller-specific libraries
if platform.machine() == "msp430":
    _msp430_lib = ctypes.CDLL("libmsp430.so")
    _msp430_lib.init_msp430.argtypes = [ctypes.c_uint32]
    _msp430_lib.init_msp430.restype = None
    _msp430_lib.config_gpio_pins.argtypes = None
    _msp430_lib.config_gpio_pins.restype = None
    _msp430_lib.read_analog_input_msp430.argtypes = [ctypes.c_uint8]
    _msp430_lib.read_analog_input_msp430.restype = ctypes.c_uint16
    _msp430_lib.write_digital_output_msp430.argtypes = [ctypes.c_uint8, ctypes.c_uint8]
    _msp430_lib.write_digital_output_msp430.restype = None
    _msp430_lib.uart_init_msp430.argtypes = [ctypes.c_uint32]
    _msp430_lib.uart_init_msp430.restype = None
    _msp430_lib.uart_write_msp430.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint8]
    _msp430_lib.uart_write_msp430.restype = None
    _msp430_lib.uart_read_msp430.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint8]
    _msp430_lib.uart_read_msp430.restype = ctypes.c_uint8
    _msp430_lib.adc_init_msp430.argtypes = None
    _msp430_lib.adc_init_msp430.restype = None
    _msp430_lib.adc_read_msp430.argtypes = [ctypes.c_uint8]
    _msp430_lib.adc_read_msp430.restype = ctypes.c_uint16

elif platform.machine() == "stm32":
    _stm32_lib = ctypes.CDLL("libstm32.so")
    _stm32_lib.init_stm32.argtypes = [ctypes.c_uint32]
    _stm32_lib.init_stm32.restype = None
    _stm32_lib.config_gpio_pins.argtypes = None
    _stm32_lib.config_gpio_pins.restype = None
    _stm32_lib.read_analog_input_stm32.argtypes = [ctypes.c_uint8]
    _stm32_lib.read_analog_input_stm32.restype = ctypes.c_uint16
    _stm32_lib.write_digital_output_stm32.argtypes = [ctypes.c_uint8, ctypes.c_uint8]
    _stm32_lib.write_digital_output_stm32.restype = None
    _stm32_lib.uart_init_stm32.argtypes = [ctypes.c_uint32]
    _stm32_lib.uart_init_stm32.restype = None
    _stm32_lib.uart_write_stm32.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint8]
    _stm32_lib.uart_write_stm32.restype = None
    _stm32_lib.uart_read_stm32.argtypes = [ctypes.POINTER(ctypes.c_uint8), ctypes.c_uint8]
    _stm32_lib.uart_read_stm32.restype = ctypes.c_uint8
    _stm32_lib.adc_init_stm32.argtypes = None
    _stm32_lib.adc_init_stm32.restype = None
    _stm32_lib.adc_read_stm32.argtypes = [ctypes.c_uint8]
    _stm32_lib.adc_read_stm32.restype = ctypes.c_uint16
    _stm32_lib.dma_init_stm32.argtypes = None
    _stm32_lib.dma_init_stm32.restype = None
    _stm32_lib.dma_transfer_stm32.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint32]
    _stm32_lib.dma_transfer_stm32.restype = None

def init_msp430(clock_speed):
    _msp430_lib.init_msp430(clock_speed)

def config_gpio_pins():
    if platform.machine() == "msp430":
        _msp430_lib.config_gpio_pins()
    elif platform.machine() == "stm32":
        _stm32_lib.config_gpio_pins()

def read_analog_input(pin):
    if platform.machine() == "msp430":
        return _msp430_lib.read_analog_input_msp430(pin)
    elif platform.machine() == "stm32":
        return _stm32_lib.read_analog_input_stm32(pin)

def write_digital_output(pin, value):
    if platform.machine() == "msp430":
        _msp430_lib.write_digital_output_msp430(pin, value)
    elif platform.machine() == "stm32":
        _stm32_lib.write_digital_output_stm32(pin, value)

def uart_init(baudrate):
    if platform.machine() == "msp430":
        _msp430_lib.uart_init_msp430(baudrate)
    elif platform.machine() == "stm32":
        _stm32_lib.uart_init_stm32(baudrate)

def uart_write(data):
    if platform.machine() == "msp430":
        _msp430_lib.uart_write_msp430(data, len(data))
    elif platform.machine() == "stm32":
        _stm32_lib.uart_write_stm32(data, len(data))

def uart_read(num_bytes):
    if platform.machine() == "msp430":
        return _msp430_lib.uart_read_msp430(num_bytes)
    elif platform.machine() == "stm32":
        return _stm32_lib.uart_read_stm32(num_bytes)

def adc_init():
    if platform.machine() == "msp430":
        _msp430_lib.adc_init_msp430()
    elif platform.machine() == "stm32":
        _stm32_lib.adc_init_stm32()

def adc_read(channel):
    if platform.machine() == "msp430":
        return _msp430_lib.adc_read_msp430(channel)
    elif platform.machine() == "stm32":
        return _stm32_lib.adc_read_stm32(channel)

def dma_init():
    if platform.machine() == "stm32":
        _stm32_lib.dma_init_stm32()

def dma_transfer(src, dst, size):
    if platform.machine() == "stm32":
        _stm32_lib.dma_transfer_stm32(src, dst, size)

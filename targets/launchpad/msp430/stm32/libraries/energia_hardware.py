import energia_core as ec

class GPIO:
    def __init__(self, pin):
        self.pin = pin

    def set_direction(self, direction):
        ec.config_gpio_pins()
        if direction == "in":
            ec.write_digital_output(self.pin, 0)
        elif direction == "out":
            ec.write_digital_output(self.pin, 1)

    def read(self):
        return ec.read_analog_input(self.pin)

    def write(self, value):
        ec.write_digital_output(self.pin, value)

class UART:
    def __init__(self, baudrate):
        ec.uart_init(baudrate)

    def write(self, data):
        ec.uart_write(data)

    def read(self, num_bytes):
        return ec.uart_read(num_bytes)

class ADC:
    def __init__(self):
        ec.adc_init()

    def read(self, channel):
        return ec.adc_read(channel)

class DMA:
    def __init__(self):
        ec.dma_init()

    def transfer(self, src, dst, size):
        ec.dma_transfer(src, dst, size)

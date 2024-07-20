import energia_core as ec

class STM32Board:
    def __init__(self):
        self.board_type = "STM32"
        self.microcontroller = "STM32"
        self.clock_speed = 72e6  # 72 MHz
        self.flash_memory = 1024 * 1024  # 1 MB
        self.sram_memory = 128 * 1024  # 128 KB

    def init_board(self):
        ec.init_stm32(self.clock_speed)
        ec.config_gpio_pins()

    def read_analog_input(self, pin):
        return ec.read_analog_input_stm32(pin)

    def write_digital_output(self, pin, value):
        ec.write_digital_output_stm32(pin, value)

    def uart_init(self, baudrate):
        ec.uart_init_stm32(baudrate)

    def uart_write(self, data):
        ec.uart_write_stm32(data)

    def uart_read(self, num_bytes):
        return ec.uart_read_stm32(num_bytes)

    def adc_init(self):
        ec.adc_init_stm32()

    def adc_read(self, channel):
        return ec.adc_read_stm32(channel)

    def dma_init(self):
        ec.dma_init_stm32()

    def dma_transfer(self, src, dst, size):
        ec.dma_transfer_stm32(src, dst, size)

import energia_core as ec

class LaunchPadBoard:
    def __init__(self):
        self.board_type = "LaunchPad"
        self.microcontroller = "MSP430"
        self.clock_speed = 16e6  # 16 MHz
        self.flash_memory = 512 * 1024  # 512 KB
        self.sram_memory = 20 * 1024  # 20 KB

    def init_board(self):
        ec.init_msp430(self.clock_speed)
        ec.config_gpio_pins()

    def read_analog_input(self, pin):
        return ec.read_analog_input_msp430(pin)

    def write_digital_output(self, pin, value):
        ec.write_digital_output_msp430(pin, value)

    def uart_init(self, baudrate):
        ec.uart_init_msp430(baudrate)

    def uart_write(self, data):
        ec.uart_write_msp430(data)

    def uart_read(self, num_bytes):
        return ec.uart_read_msp430(num_bytes)

import asyncio
import logging
from typing import List, Dict, Any

class Energia:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger("Energia")
        self.devices: List[EnergiaDevice] = []

    async def initialize(self):
        self.logger.info("Initializing Energia framework")
        await self.load_devices()

    async def load_devices(self):
        self.logger.info("Loading energy devices")
        devices = await self.config["device_manager"].get_devices()
        for device in devices:
            self.devices.append(EnergiaDevice(device))

    async def start(self):
        self.logger.info("Starting Energia framework")
        await asyncio.gather(*[device.start() for device in self.devices])

    async def stop(self):
        self.logger.info("Stopping Energia framework")
        await asyncio.gather(*[device.stop() for device in self.devices])

class EnergiaDevice:
    def __init__(self, device_config: Dict[str, Any]):
        self.config = device_config
        self.logger = logging.getLogger("EnergiaDevice")
        self.device: Any = None

    async def start(self):
        self.logger.info(f"Starting device {self.config['name']}")
        self.device = await self.config["device_factory"].create_device(self.config)
        await self.device.start()

    async def stop(self):
        self.logger.info(f"Stopping device {self.config['name']}")
        await self.device.stop()

    async def read_data(self) -> Dict[str, Any]:
        self.logger.info(f"Reading data from device {self.config['name']}")
        return await self.device.read_data()

    async def write_data(self, data: Dict[str, Any]):
        self.logger.info(f"Writing data to device {self.config['name']}")
        await self.device.write_data(data)

import logging
import anyio

from moat.mqtt.client import open_mqttclient
from moat.mqtt.mqtt.constants import QOS_0, QOS_1, QOS_2

logger = logging.getLogger(__name__)

async def test_coro():
    """Publish in parallel"""
    async with open_mqttclient(uri='mqtt://test.mosquitto.org/') as C:
        async with anyio.create_task_group() as tg:
            tg.start_soon(C.publish,'a/b', b'TEST MESSAGE WITH QOS_0')
        logger.info("messages published")

if __name__ == '__main__':
    formatter = "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=formatter)
    anyio.run(test_coro)
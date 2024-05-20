import asyncio
from hbmqtt.broker import Broker

config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '0.0.0.0:1883',
        }
    },
    'sys_interval': 10,
    'topic-check': {
        'enabled': True,
        'plugins': [
            'topic_taboo'
        ]
    }
}

broker = Broker(config)

async def start_broker():
    await broker.start()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_broker())
    loop.run_forever()
import asyncio

# @asyncio.coroutine
# def hello():
# 	print('hello, world')
# 	r = yield from asyncio.sleep(1)
# 	print('hello, again')

# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


async def hello():
	print('hello, world')
	r = await asyncio.sleep(1)
	print('hello, again')

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
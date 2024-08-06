#!/usr/bin/env python3
'''Task 0's module.
'''import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

# To demonstrate how it works, we can write an async function to consume the generator.
async def main():
    async for value in async_generator():
        print(value)

# Run the main function to see the output
asyncio.run(main())

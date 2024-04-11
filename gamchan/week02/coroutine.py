import asyncio

async def async_generator():
    for item in range(3):
        # 비동기적으로 일정 시간을 기다립니다.
        await asyncio.sleep(1)
        yield f"Item {item}"

async def main():
    # 비동기 제너레이터를 사용합니다.
    async for item in async_generator():
        print(item)

# 비동기 메인 함수를 실행합니다.
asyncio.run(main())
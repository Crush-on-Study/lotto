import asyncio
import aiohttp
from bs4 import BeautifulSoup
from collections import Counter

async def fetch_url(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.text()

async def get_lotto_numbers(start, end):
    lotto_numbers = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(start, end + 1):
            url = f'https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={i}'
            task = fetch_url(session, url)
            tasks.append(task)
        
        responses = await asyncio.gather(*tasks)
        
        for response_text in responses:
            soup = BeautifulSoup(response_text, 'html.parser')
            numbers = soup.select('.num.win span')
            numbers = [int(number.get_text()) for number in numbers]
            lotto_numbers.append(numbers)
        
    return lotto_numbers

def analyze_lotto_numbers(numbers_list):
    all_numbers = [number for sublist in numbers_list for number in sublist]
    number_counts = Counter(all_numbers)
    
    most_common_numbers = number_counts.most_common(6)
    return most_common_numbers

if __name__ == '__main__':
    start = 1025  # 시작 회차
    end = 1028  # 종료 회차
    
    loop = asyncio.get_event_loop()
    lotto_numbers = loop.run_until_complete(get_lotto_numbers(start, end))
    
    most_common_numbers = analyze_lotto_numbers(lotto_numbers)
    
    print("가장 많이 나온 번호 6개:")
    result = []
    for number, count in most_common_numbers:
        # print(f"번호: {number}, 빈도: {count}")
        result.append(number)
    
    result.sort()
    print(result)
    # [(2, 20), (13, 20), (16, 19), (18, 22), (21, 20), (44, 20)]
    # 이런 식으로 출력이 될겁니다. 앞에 2,13,16,18,21,44가 로또 번호입니다.
    # 오른쪽 숫자들 20,20,19,22,20,20은 당첨 번호로 뽑힌 빈도 수를 의미해요.
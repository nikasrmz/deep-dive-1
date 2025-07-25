from asyncio import futures
import time
from pathlib import Path
from typing import Callable
from concurrent import futures

import httpx

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
 'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'https://www.fluentpython.com/data/flags'
DEST_DIR = Path('downloaded')


def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)


def get_flag(cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=6.1, follow_redirects=True)
    resp.raise_for_status()
    return resp.content


def download_many_seq(cc_list: list[str]) -> int:
    for cc in sorted(cc_list):
        image = get_flag(cc)
        save_flag(image, f'{cc}.gif')
        print(cc, end=' ', flush=True)
    return len(cc_list)


def main(downloader: Callable[[list[str]], int]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloads in {elapsed:.2f}s')


def download_one_thr(cc: str):
    img = get_flag(cc)
    save_flag(img, f'{cc}.gif')
    print(cc, end=' ', flush=True)
    # return cc


def download_many_thr(cc_list: list[str]):
    with futures.ThreadPoolExecutor() as executor:
        res = executor.map(download_one_thr, sorted(cc_list))

    return len(list(res))


if __name__ == '__main__':
    main(download_many_seq) 
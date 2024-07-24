import speedtest
import time


def test_internet_speed():
    print("Testing...")
    s = speedtest.Speedtest()

    print("Tashqi yuklash tezligi aniqlanyapti...")
    download_speed = s.download() / 1_000_000

    print("Ichki yuklash tezligi...")
    upload_speed = s.upload() / 1_000_000

    print("Ping aniqlanyapti...")
    s.get_servers([])
    ping = s.results.ping

    return download_speed, upload_speed, ping


def main():
    start_time = time.time()
    download, upload, ping = test_internet_speed()
    end_time = time.time()

    print(f"\nTashqi yuklash tezligi: {download:.2f} Mbps")
    print(f"Ichki yuklash tezligi: {upload:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")
    print(f"Aniqlash uchun ketgan vaqt: {end_time - start_time:.2f} sekund")


if __name__ == "__main__":
    main()

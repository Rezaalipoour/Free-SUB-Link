import requests

urls = [
    "https://raw.githubusercontent.com/10ium/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_4.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_4.txt"
]

all_configs = []

for url in urls:
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            lines = response.text.strip().splitlines()
            all_configs.extend(line for line in lines if line.startswith(("vmess://", "vless://", "trojan://", "ss://", "ssr://")))
    except Exception as e:
        print(f"خطا در دریافت {url}: {e}")

with open("sub.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(all_configs))

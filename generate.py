import requests

# همه لینک‌هایی که دادی
urls = [
    "https://raw.githubusercontent.com/10ium/multi-proxy-config-fetcher/refs/heads/main/configs/proxy_configs.txt",
    "https://raw.githubusercontent.com/10ium/multi-proxy-config-fetcher/refs/heads/main/configs/singbox_configs.json",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_4.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_4.txt",
    "https://raw.githubusercontent.com/coldwater-10/V2Hub3/main/merged",
    "https://raw.githubusercontent.com/coldwater-10/V2Hub3/main/Split/Normal/vmess",
    "https://raw.githubusercontent.com/coldwater-10/V2Hub3/main/Split/Normal/vless",
    "https://raw.githubusercontent.com/coldwater-10/V2Hub3/main/Split/Normal/reality",
    "https://raw.githubusercontent.com/coldwater-10/V2Hub3/main/Split/Base64/vmess",
    "https://raw.githubusercontent.com/coldwater-10/V2Hub4/main/merged",
    "https://raw.githubusercontent.com/coldwater-10/V2Hub4/main/Split/Normal/vmess",
    "https://raw.githubusercontent.com/coldwater-10/V2Hub4/main/Split/Normal/vless",
    "https://raw.githubusercontent.com/coldwater-10/V2Hub4/main/Split/Base64/vmess"
]

# فایل خروجی
with open("sub.txt", "w", encoding="utf-8") as outfile:
    for url in urls:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                outfile.write(r.text.strip() + "\n")
                print(f"✅ گرفته شد: {url}")
            else:
                print(f"❌ مشکل در گرفتن: {url}")
        except Exception as e:
            print(f"❗ خطا: {url} - {e}")

print("✅ همه کانفیگ‌ها ذخیره شد توی sub.txt")

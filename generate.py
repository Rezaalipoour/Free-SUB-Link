import requests

# لیست لینک‌های جدید برای دریافت کانفیگ
urls = [
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_4.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_4.txt",
]

# دریافت محتواها از لینک‌ها
all_data = []
for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text.strip()
        if content:
            all_data.append(content)
    except Exception as e:
        print(f"خطا در دریافت {url}: {e}")

# ترکیب و ذخیره در sub.txt
with open("sub.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(all_data))

print("فایل sub.txt با موفقیت ساخته شد ✅")

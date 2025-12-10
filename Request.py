import requests


url = "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/main/telegram/index.html"


response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Failed to download file: {response.status_code}")

html_content = response.text


with open("input.txt", "w", encoding="utf-8") as f:
    f.write(html_content)


modified_html = html_content.replace(
    '<a href="https://t.me/mahsa_net">\n                MahsaNet\n                </a>',
    '<a href="https://t.me/BridgeTest">\n                Bridge Services !\n                </a>'
)


with open("output.html", "w", encoding="utf-8") as f:
    f.write(modified_html)

print("File downloaded, modified, and saved as output.html")

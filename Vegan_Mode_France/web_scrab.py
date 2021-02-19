import requests
from bs4 import BeautifulSoup

# Amazon Price Track
url = "https://www.amazon.fr/gp/product/B086Q9WW57?pf_rd_\
        r=1C2NVFH6KCG9CN6QSAQM&pf_rd_p=ed1ef413-005c-474d-\
        837a-434c7d76d0d9&pd_rd_r=fda887de-6657-43f5-9a6f\
        -131dd5cbc79f&pd_rd_w=zy262&pd_rd_wg=a53BF&ref_=pd_gw_unk"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

def check_price():

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    # print(soup.prettify()[:555])

    title = soup.find(id="productTitle").get_text()
    # print(title.strip())

    price = soup.find(id="priceblock_dealprice").get_text()
    price = price[:-5]
    price = float(price.replace("\xa0", "").replace(",", "."))

    if price < 2750:
        send_mail()


def send_mail():
    
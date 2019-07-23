import requests
import json

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
cookies = {
    "JSESSIONID": "d1487ce8-b917-42ad-81f6-bdc78c49e3df"
}

order_gids = ["d620da9d-72de-441c-b9f7-68715cfa2156","d620da9d-72de-441c-b9f7-68715cfa2155"]

for order_gid in order_gids:
    req = json.dumps({"orderGid": order_gid})
    print(req)
    resp = requests.post("https://ebjrd.weshare.com.cn/seal/manage/risk/vendor/async?b=0&bl=zh_CN", req,
                         headers=headers, cookies=cookies)
    print(resp.text)


# session = requests.Session()

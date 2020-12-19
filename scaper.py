import logging
import requests
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Start of program")
logging.disable(logging.CRITICAL)

website = "https://www.sfma.org.sg/member/members-directory"
#website = "https://www.sfma.org.sg/member/info.php?cid=A000493"
res = requests.get(website)
#res.raise_for_status
logging.debug(res.text)
res.json()
playFile = open("try.txt", "wb")
loggin.debug(res)
# for chunk in res.iter_content(100000) :
#     playFile.write(chunk)


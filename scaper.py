import bs4
import logging
import requests

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Start of program")
logging.disable(logging.CRITICAL)

website = "https://www.sfma.org.sg/member/members-directory"
# website = "https://www.sfma.org.sg/member/info.php?cid=A000493"
res = requests.get(website)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, "html.parser")
logging.debug(soup)
# elems = soup.select("#myList > a:nth-child(1)")
elems = soup.select(
    "html body div.min-vh-100.container-fluid.bg-white.pb-3 div#myList.list-group a.list-group-item.list-group-item-action")

playFile = open("scrape.txt", "w")
logging.debug(elems)
sum = 0
for chunks in elems:
    chunks = str(chunks)[56:76]
    logging.info(chunks)
    coySite = "https://www.sfma.org.sg/member/" + chunks
    logging.info(coySite)
    coyReq = requests.get(coySite)
    coySoup = bs4.BeautifulSoup(coyReq.text, "html.parser")
    logging.warning(coySoup)
    coyElems = coySoup.select(".min-vh-100")
    sum += 1
    logging.warning(coyElems)
    for i, coyChunks in enumerate(coyElems):
        logging.warning(coyChunks)
        coyChunks = str(coyChunks)[213:485]
        coyList = coyChunks.split("<p>")
        # coyList = "".join(coyList)
        # coyList = coyList.split("</strong>")
        # coyList = "".join(coyList)
        # coyList = coyList.split("</h")
        # coyName = coyList[0]
        coyEmail = coyList[5][23:].split("</p>")[0]
        # coyTel = coyList[9]
        # coyEmail = coyList[17].split("/strong>")[1]
        # logging.debug(coyList)
        # for idx, chunky in enumerate(coyList) :
        #     if idx == 0 :
        #         coyName = chunky.split("</h6>")[0]
        #     elif idx == 3 :
        #         coyTel = chunky[23:].split("</p>")[0]
        #
        #     elif idx == 5 :
        #         coyEmail = chunky[23:].split("</p>")[0]

        playFile.write(f"{coyEmail};")
        # playFile.write(f"{coyName}, {coyTel}, {coyEmail}\n")
        # playFile.write(f"{coyName} \n")
        # playFile.write(f"{coyTel} \n")
        # playFile.write(f"{coyEmail} \n")

    #     break
    #
    # break
    # if(sum == 25) :
    #      break

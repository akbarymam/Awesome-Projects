from bs4 import BeautifulSoup as bes

from requests import get

from urlextract import URLExtract

def search():

    q = input("apa? ")

    url = "https://kusonime.com/?s={}&post_type=post".format(q)

    r = bes(get(url).text, "html.parser")

    global res

    res = []

    [res.append(i.find("a")["href"]) for i in r.find_all("h2", "episodeye")]

    [print(n,i.get_text()) for n,i in enumerate(r.find_all("h2", "episodeye"), start=1)]

    print(pill())

    

def pill():

    pil = int(input("pilih? "))-1

    sop = bes(get(res[pil]).text, "html.parser").find("div", "smokeurl")

    rext = URLExtract()

    data = {

        "result": None

    }

    if "BELUM TERSEDIA" in str(sop):

        print("belum ada")

    else:

        rez = bes(get(sop.find("a")["href"]).text, "html.parser").find("div", "card card-body mb-3")

        if rez is None:

            ssop = bes(get(res[pil]).text, "html.parser")

            #[print([x["href"] for x in i.find_all("a")]) for i in ssop.find_all("div", "smokeurl")]

            for i in ssop.find_all("div", "smokeurl"):

                data["result"] = i

        else:

            #[print(i) for i in rext.find_urls(rez.text)]

            for i in rext.find_urls(rez.text):

                data["result"] = i

search()






import urllib.request
from bs4 import BeautifulSoup

class Scraper:
  #スクレイピング対象となるWebサイトのURLを受け取る。引数を受け取る
    def __init__(self, site):
        self.site = site

  #スクレイピングしたいタイミングで、このメソッドを呼び出す
    def scrape(self):
      #urlopen関数はWebサイトへのリクエストを行う。Responseオブジェクトが返され、この中でHTMLと追加情報が格納されている
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        #BeautifulSoupオブジェクトにHTML変数とHTMLをパースして欲しいことを伝える
        sp = BeautifulSoup(html, parser)
        #find_allメソッドはイテラブルなオブジェクト・・・条件に合うHTML要素を取得する
        #<a></a>タグを全て集めて返す様に伝える
        for tag in sp.find_all("a"):
          #ループが回る度に変数tagに新しいTagのオブジェクトが代入される
          #ここで必要なのはURLが代入されているhrefインスタンス変数
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.google.com/"
Scraper(news).scrape()

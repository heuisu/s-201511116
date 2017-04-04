import requests
import lxml.etree

def getkb():
    r=requests.get('http://www.kbreport.com/main')
    _htmlTree = lxml.etree.HTML(r.text)
    nodes = _htmlTree.xpath("//div[@class='team-rank-box']//table[@class='team-rank']//tr")
    print "number of table columns: ", len(nodes)
    counter=0
    for teams in nodes:
        for cols in teams:
            if cols.xpath('.//a/text()'):
                print cols.xpath('.//a/text()')[0],
            else:
                print cols.text.strip(),
        print

def main():
    getkb()
    
if __name__ == "__main__":
    main()
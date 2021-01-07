import urllib
#from BeautifulSoup import BeautifulSoup
from pyquery import PyQuery as pq
def getArticleList(url):
  lstArticles=[]
  url_prefix=url[:-6]
  Cnt=1
  
  response=urllib.urlopen(url)
  html=response.read()
  d=pq(html)
  try:
    pageCnt=d("ul.SG_pages").find('span')
    pageCnt=int(d(pageCnt).text()[1:-1])
  except:
    pageCnt=1
  for i in range(1,pageCnt+1):
    url=url_prefix+str(i)+".html"
    #print url
    response=urllib.urlopen(url)
    html=response.read()
    d=pq(html)
    title_spans=d(".atc_title").find('a')
    date_spans=d('.atc_tm')
    
    for j in range(0,len(title_spans)):
      titleObj=title_spans[j]
      dateObj=date_spans[j]
      article={}
      article['link']= d(titleObj).attr('href')
      article['title']= d(titleObj).text()
      article['date']=d(dateObj).text()
      article['desc']=getPageContent(article['link'])
      lstArticles.append(article)
  return lstArticles
  
def getPageContent(url):
  #get Page Content
  response=urllib.urlopen(url)
  html=response.read()
  d=pq(html)
  pageContent=d("div.articalContent").text()
  #print pageContent
  return pageContent
def main():
  url='http://blog.sina.com.cn/s/articlelist_1327886753_0_1.htmll'#A Ping
  lstArticles=getArticleList(url)
  for article in lstArticles:
    f=open("blogs/"+article['date']+"_"+article['title']+".txt",'w')
    f.write(article['desc'].encode('utf-8')) 
    f.close()
    #print article['desc']
    
if __name__=='__main__':
  main()
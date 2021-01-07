import re
import urllib2
import thread

#download the articles on a certain artilcelist page;start might be 1,end might be 50
def down_article('/Users/JinTang/Desktop/sinabackup','http://blog.sina.com.cn/s/articlelist_1327886753_0_1.html',1,10):
#download the article
	while 1:
		if start<end:
			fblog=urllib2.urlopen(blog_articlelist[start]).read()
			ptitle="<title>.*</title>"
			title_temp=re.search(ptitle,fblog)
			title_chaos=title_temp.group().decode('utf8').strip("</title>")
			title=title_chaos.replace('&#9671;','')
			title=title.replace('&nbsp;',' ')
			print 'saved:',title
			fdown=file(targetdirectory + title + '.htm','w')
			fdown.write(fblog)
			start=start+1
		else:
			break

def download('http://blog.sina.com.cn/wpq58102','/Users/JinTang/Desktop/sinabackup'): #download the url to the targetdirectory
#find the maincatalog' url according to the homepage
	blog_homepage=urllib2.urlopen(url).read()
	pattern_maincatalog = re.compile('http://blog.sina.com.cn/s/articlelist_\d*_0_1.html')
	dir=pattern_maincatalog.findall(blog_maincatalog)

#find the catalogs'rls according identifing them on the maincatalog page

blog_maincatalog=urllib2.urlopen('http://blog.sina.com.cn/wpq58102').read()
pattern_directory = re.compile('http://blog.sina.com.cn/s/articlelist_\d*_0_\d*.html')
blog_directory=pattern_directory.findall(blog_maincatalog)

#the method to download
i=1
while 1:
	if i<(len(blog_directory)-1):
		blogdir=urllib2.urlopen(blog_directory[i]).read()
		pattern_articlelist = re.compile('http://blog.sina.com.cn/s/blog_\w*.html')
		blog_articlelist=pattern_articlelist.findall(blogdir)
		i=i+1
		j=0
#create threads here
		thread.start_new_thread(down_article,('/Users/JinTang/Desktop/sinabackup ',blog_articlelist,j,len(blog_articlelist)))
	else:
		break

def main():
	print 'input like download(url,targetdirectory)'
	print 'help:url is the blog url,targetdirectory is where you want to save'
	print "ex:download('http://blog.sina.com.cn/nonexttime','D:/blog/')"
if __name__ == '__main__':
	main()



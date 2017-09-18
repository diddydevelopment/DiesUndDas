import whois
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import tldextract

domains = ['googsfedsfwsle.de', 'stackoverflow.com']


anchor_url = 'https://en.wikipedia.org/wiki/Adolf_Hitler'
page = requests.get(anchor_url)

soup = BeautifulSoup(page.text, "lxml")

follow_links_to_same_domain = True
follow_links_to_other_domain = True


def get_url_parts(url):
    tld = tldextract.extract(url)
    return tld.subdomain, tld.domain, tld.suffix


def build_url(url):
    subdomain,domain,suffix = get_url_parts(url)
    return 'http://'+subdomain+'.'+domain+'.'+suffix

def equal_domain(url1,url2,with_subdomain=False):
    subdomain1,domain1,suffix1 = get_url_parts(url1)
    subdomain2,domain2,suffix2 = get_url_parts(url2)

    if with_subdomain:
        return subdomain1 == subdomain2 and domain1 == domain2 and suffix1 == suffix2
    else:
        return domain1 == domain2 and suffix1 == suffix2


host_name = build_url(anchor_url)




found_links = []
for link in soup.find_all('a', href=True):
    l = link['href']

    if l[0] == '#': #anchors, unimportant
        pass
    elif l[0] == '/': #relative link
        found_links.append(host_name+l)
    elif l[0:7] == 'http://' or l[0:8] == 'https://':
        found_links.append(l)
    else:
        print('unknown: '+l)


print(found_links)

links_to_other_websites = []
#print links from other hosts
for l in found_links:
    if not equal_domain(anchor_url,l):
        links_to_other_websites.append(l)


for dom in links_to_other_websites:
    subdomain, domain, suffix = get_url_parts(dom)
    try:
        rtnwhois = whois.query(domain+'.'+suffix,ignore_returncode=True)
        print(domain+'.'+suffix+' ist besetzt')
        print(domain.name, domain.registrar)
    except:
        print(domain+'.'+suffix+' ist noch frei')



import advertools as adv
from constants import *
from urllib.parse import urlparse
from utils import *
results=[]
undonedomain=[]
for idx,url in enumerate(popular_shopify_stores):
        domain = urlparse(url).netloc
        if not 'www' in domain:
            domain='www.'+domain
        try:
                index=adv.sitemap_to_df('https://'+domain+'/robots.txt', recursive=False)['loc'].tolist()
                print(index)
                urls=[]
                for url in index:
                    locs=adv.sitemap_to_df(url)['loc'].tolist()
                    urllocs={"sitemap":url,
                            "loc":locs}
                    urls.append(urllocs)
                sitemapindex={'domain':domain,
                             "sitemapurl":index,
                             "urls":urls
                }
                results.append(sitemapindex)
        except:
                print('no robots.txt')
                undonedomain.append(domain)
write_text('data/shopify/sitemapindex.json',results)
write_text('data/shopify/noroto.txt',undonedomain)
# adv.crawl('http://www.cettire.com', 'my_output_file.jl', follow_links=True)

# # That's it! To open the file:

# import pandas as pd

# crawl_df = pd.read_json('my_output_file.jl', lines=True)

# # https://github.com/prnvvj/Website-SiteMap-Analysis
# https://colab.research.google.com/github/Rahul-YYC/CrawlWebsitePython/blob/main/CrawlAnalyzeWebsitePython.ipynb#scrollTo=JBLOgK5Td8oz
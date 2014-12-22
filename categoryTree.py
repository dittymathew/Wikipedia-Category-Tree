from wikitools import wiki,category,api
import sys

def wikipedia_query(query_params,lang='en'):
	site = wiki.Wiki(url='http://'+lang+'.wikipedia.org/w/api.php')
	request = api.APIRequest(site, query_params)
	result = request.query(False)
	return result[query_params['action']]

def get_category_members(par_category, depth, lang='en'):
    category_name = 'Category:'+par_category
    if depth < 0:
        return 0
    
    #Begin crawling articles in category
    results = wikipedia_query({'list': 'categorymembers','cmtitle': category_name,'cmtype': 'page','cmlimit': '500','action': 'query'},lang)  
    
    # Begin crawling subcategories
    results = wikipedia_query({'list': 'categorymembers',
                                   'cmtitle': category_name,
                                   'cmtype': 'subcat',
                                   'cmlimit': '500',
                                   'action': 'query'},lang)
    subcategories = []
    if 'categorymembers' in results.keys() and len(results['categorymembers']) > 0:
        for i, category in enumerate(results['categorymembers']):
            cat_title = category['title']
            subcategories.append(cat_title.strip('Category:'))
    subcat= ''.join(cat.encode('latin-1', 'ignore')+',' for cat in subcategories).strip(',')
    if subcat !='':
      wp.write(par_category.encode('latin-1', 'ignore')+':'+subcat+'\n')
    for category in subcategories:
      get_category_members(category,depth-1)


wikisite = "http://en.wikipedia.org/w/api.php"
par_category = sys.argv[1]
depth =int(sys.argv[2])
cat_tree =sys.argv[3]
wp =open(cat_tree,'w')


get_category_members(par_category,depth,'en')


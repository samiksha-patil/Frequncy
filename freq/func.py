import requests
from bs4 import BeautifulSoup
import operator 
from collections import Counter

# error handling

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


from nltk.corpus import stopwords 
stop_words = set(stopwords.words('english'))

# settings
def freq(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    url = url

    response = requests.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(response.text, "html.parser")

    for script in soup(["script", "style"]):
        script.extract()

    text = soup.get_text()
    wordlist=[]
    for each_text in text.split(" "): 
            content = each_text 
    
            words = content.lower().split() 

            for each_word in words: 
                if each_word not in stop_words:
                    wordlist.append(each_word)


    clean_list =[] 
    for word in wordlist: 
        symbols = '→↵!@#$%^&*()_-+={[}]|\;:"<>?/., '

        for i in range (0, len(symbols)): 
            word = word.replace(symbols[i], '') 

        if len(word) > 0: 
            clean_list.append(word) 
    
    word_count = {} 

    for word in clean_list: 
        if word in word_count: 
            word_count[word] += 1
        else: 
            word_count[word] = 1
    
    c = Counter(word_count) 
    
    top = c.most_common(10) 
    
    return top



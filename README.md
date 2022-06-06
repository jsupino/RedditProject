# RedditProject
This is my project for CSIT505. I am scraping a nature web page on Reddit using Python.
I will be utilizing the BeautifulSoup, Requests, and lmxl Python libraries to retrieve the most recent nature posts on Reddit.

Beautiful Soup is a Python library that is used to parse HTML files. It is very useful in web scraping to extract data.

Requests is a HTTP library used for Python. It is very useful in sending HTTP requests. When using request, a response object is returned with the data.

lxml is a Python library. It is very useful in handling HTML files.

Install the packages

    pip install BeautifulSoup4
    pip install requests
    pip install lxml

After installing the packages, import beautifulsoup and requests

    from bs4 import BeautifulSoup
    import requests
    
On the web page developer tools, access the UserAgent. To do so, type in navigator.UserAgent in the console. This is then inserted into headers. Access the url to the page in which you wish to retrieve data from. This is the url. Now, that you already imported requests, utilize this package to get the url. Then utilize the BeautifulSoup package to parse the html. By using prettify, the HTML code will have proper indents and be easier to read.

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like     Gecko) Chrome/101.0.4951.67 Safari/537.36'}
    url='https://www.reddit.com/r/nature/'
    response=requests.get(url, headers=headers)

    soup=BeautifulSoup(response.text,'html.parser')
    print(soup.prettify)
    
After parsing the html file, access the posts on the web page. The first print statement will return the title, the second will return the likes on that post, the third will print the number of comments on that post, and the fourth will return the rest of the url to access that specific post. The last print statement is used as a separator in between each post returned.

    for item in soup.select('.Post'):
        try:
            print(item.select('._eYtD2XCVieq6emjKBH3m')[0].get_text())
            print(item.select('._1rZYMD_4xY3gRcSS3p8ODO')[0].get_text())
            print(item.select('.FHCV02u6Cp2zYL0fhQPsO')[0].get_text())
            print(item.select('._2INHSNB8V5eaWp4P0rY_mE a[href]')[0]['href'])
            print('----------------------------------------')
        except Exception as e:
            print('')


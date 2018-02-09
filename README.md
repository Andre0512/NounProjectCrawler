# NounProjectCrawler

**This little script downloads all icons for a specific search term from [thenounproject.com](https://thenounproject.com/)**  
The Noun Project offers you over a million icons under the creative common license. 
But if you want download many icons e.g. to make your own font, it can be much clicking. 

### Features
* Download all svg icons for a specific term
* You **don't** need an account on NounProject
* It generates you a file where the author of each icon is listed
* And a list with a link to each occurring author

### Usage
1. Download script  
`git clone https://github.com/Andre0512/NounProjectCrawler.git && cd NounProjectCrawler/`
2. Create a virtual environment (optional)  
`python3 -m venv ./venv && source ./venv/bin/activate`  
3. Install requirements  
`pip install -r requirements.txt`
4. Run this script  
`python Crawler.py 'YOUR SEARCH TERM'`
5. Now you can find your icons in `./download/YOUR SEARCH TERM/`

### License  
This project is under the _DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE_.

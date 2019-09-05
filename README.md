Use python scrapy to get data from douban which is a movie review website.

### step:

- `git clone https://github.com/MyDuan/movie_scrapy.git`
- `cd movie_scrapy/`
- `pip install -r requirements.txt`
- `scrapy crawl douban_spider`

### data:

- Use the sqlite3 to save the gotten data.
- data.db will be created and can be seen in movie_scrapy/data.db
- See your data:
    - `sqlite3 data.db`
    - `sqlite> .table`
    - `sqlite> select * from movies;`
    
### analysis the data in notebook (Pycharm)
- run `jupyter lab --no-browser`
- run the `RUN button` in pycharm
- Type the url to pycharm
- Than can run the notebook file in ./notebook.
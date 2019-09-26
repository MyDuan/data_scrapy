Use python scrapy to get data from douban which is a movie review website （https://movie.douban.com/top250）.
Also to get data from http://rtbsquare.ciao.jp/ to statistical keywords.

### step:

- `git clone https://github.com/MyDuan/data_scrapy.git`
- `cd data_scrapy/`
- `pip install -r requirements.txt`
- `scrapy crawl douban_spider` // get movie data from douban
- `scrapy crawl rtb_square_spider`  // get news data from rtb square in 2019
- `scrapy crawl rtb_square_spider -a start_year=your_start_year -a end_year=your_end_year`  // get news data from rtb square from your_start_year to your_end_year
    - for example `scrapy crawl rtb_square_spider -a start_year=2018 -a end_year=2019` // get news data from rtb square from 2018 to 2019
    - note: please set start_year < end_year and the default value of start_year and end_year are all 2019.
### data:

- Use the sqlite3 to save the gotten data.
- data.db will be created and can be seen in movie_scrapy/data.db
- See your data:
    - `sqlite3 data.db`
    - `sqlite> .table`
    - `sqlite> select * from movies;`
    - `sqlite> select count(1) from rtb_square_news;`
    
### analysis the data in notebook (Pycharm)
- run `jupyter lab --no-browser`
- run the `RUN button` in pycharm
- Type the url to pycharm
- Than can run the notebook file in ./notebook.

### Example
- In this repository, there is a sqlite db example which have the data gotten from the target website.
- In the ./notebook, there are some example notebook files.

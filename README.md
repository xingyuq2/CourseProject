# CourseProject
Please see documentation.pdf for details of this project.

## Install python package
pip install pandas\
pip install sklearn\
pip install nltk\
python -m nltk.downloader stopwords\
pip install collections\
pip install flask\
pip install flask-cors\
pip install csv\
pip install bs4\
pip install selenium\
pip install time

## Install Node.js and npm
Download Node.js by this link: https://nodejs.org/en/download/

If node and npm is not detected after downloading, try to restart your computer.


## Usage
1.If you want to create a new data csv file by using scraper, then follow this instruction. Note that this will rewrite videos.csv file and scraping also takes a long time (approximately 20 minutes).

- Run netflix scraper in the root directory by command:\
`python -m scraper.main`

If you just want to test scraper, then follow these instructions.
- Go to ‘constant.py’ in ‘scraper’ folder, change value of NUMBER_EACH_GENRE to 2, change value of NUMBER_SECTION to 3. Go to ‘utils.py’ and change value of CSV_TO_WRITE to ‘test.csv’

- Then run netflix scraper in the root directory by command:\
`python -m scraper.main`

2.If you want to open the video recommender web application, then follow these instructions.

- Run flask app in the root directory by command:\
`python -m flask_app`

- Run react app in the "video-recommender-app" directory by command:\
`cd video-recommender-app`\
`npm install`\
`npm start`
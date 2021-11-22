from scraper.netflix_scraper import scrape
from utils import write_to_csv


if __name__ == '__main__':
    # scrpae videos' information in Netflix
    videos = scrape()
    print(videos)
    # write to file with name 'videos.csv'
    write_to_csv(videos)

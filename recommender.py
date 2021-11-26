import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

VIDEO_CSV_FILE = 'videos.csv'
NUMBER_VIDEO_RECOMMEND = 10


def combine_features(row):
    """
    Combine features that are used to compare silimarities to form a single string
    """
    res = row['name'] + ' ' + row['mood_tag'] + ' ' + row['genres'] + ' ' + row['casts'] + ' ' + row['creators']
    res = res.replace(',', ' ')
    return res


def get_name_from_index(df, index):
    """
    Get the name of the movie by index from DataFrame
    """
    return df[df.index == index]["name"].values[0]


def recommend(mov_idx):
    """
    Recommend videos based on the combined features.
    """
    df = pd.read_csv(VIDEO_CSV_FILE)
    # features that is used to recommend videos
    features = ['name', 'mood_tag', 'genres', 'casts', 'creators']
    # fill NA with empty string
    for feature in features:
        df[feature] = df[feature].fillna('')
    # apply combine_feature method over each row of Dataframe and store the combined string in 'combined_features' column
    df['combined_features'] = df.apply(combine_features, axis=1)
    
    # feed these strings to a CountVectorizer() object and get the count matrix
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combined_features'])
    # obtain the cosine similarity matrix from the count matrix
    cosine_sim = cosine_similarity(count_matrix)
    
    # accessing the row corresponding to given movie to find all the similarity scores for that movie and then enumerating over it
    similar_movies = list(enumerate(cosine_sim[mov_idx]))
    # sort the list similar_movies according to similarity scores in descending order and discard itself
    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
    
    # store the index of recommended movies
    list_of_index = []
    movie_user_likes = get_name_from_index(df, mov_idx)
    print(f'Top {NUMBER_VIDEO_RECOMMEND} similar movies to ' + movie_user_likes+ ' are:\n')
    # for each row
    for i, element in enumerate(sorted_similar_movies):
        if i >= NUMBER_VIDEO_RECOMMEND:
            break
        # append the index of movie to list_of_index
        list_of_index.append(element[0])
        print(get_name_from_index(df, element[0]))
        
    return list_of_index
    
    

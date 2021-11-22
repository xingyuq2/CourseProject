import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

VIDEO_CSV_FILE = 'videos.csv'
NUMBER_VIDEO_RECOMMEND = 10


def combine_features(row):
    """
    Combine features that are used to compare silimarities
    """
    res = row['name'] + ' ' + row['mood_tag'] + ' ' + row['genres'] + ' ' + row['casts'] + ' ' + row['creators']
    res = res.replace(',', ' ')
    return res


def get_name_from_index(df, index):
    return df[df.index == index]["name"].values[0]


def recommend(idx):
    """
    Recommend videos based on the combined features.
    """
    df = pd.read_csv(VIDEO_CSV_FILE)
    features = ['name', 'mood_tag', 'genres', 'casts', 'creators']
    for feature in features:
        df[feature] = df[feature].fillna('')
    df['combined_features'] = df.apply(combine_features, axis=1)
    print(df.loc[idx, 'combined_features'])
    
    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df['combined_features'])
    
    cosine_sim = cosine_similarity(count_matrix)
    
    movie_index = idx
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    
    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]
    
    list_of_index = []
    movie_user_likes = get_name_from_index(df, idx)
    print(f'Top {NUMBER_VIDEO_RECOMMEND} similar movies to ' + movie_user_likes+ ' are:\n')
    for i, element in enumerate(sorted_similar_movies):
        if i >= NUMBER_VIDEO_RECOMMEND:
            break
        list_of_index.append(element[0])
        print(get_name_from_index(df, element[0]))
        
    return list_of_index
    
    

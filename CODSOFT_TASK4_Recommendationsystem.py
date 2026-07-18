import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = {
    "title": [
        "Inception",
        "Interstellar",
        "The Dark Knight",
        "Avengers: Endgame",
        "John Wick",
        "Titanic",
        "The Notebook",
        "3 Idiots",
        "Hera Pheri",
        "The Conjuring",
        "Annabelle",
        "Insidious"
    ],

    "description": [
        "science fiction dream action thriller",
        "space science fiction adventure drama",
        "superhero action crime thriller",
        "superhero action adventure marvel",
        "action assassin thriller crime",
        "romantic drama love ship",
        "romantic love emotional drama",
        "comedy friendship college drama",
        "comedy fun family entertainment",
        "horror ghost supernatural scary",
        "horror haunted doll supernatural",
        "horror paranormal ghost mystery"
    ]
}

df = pd.DataFrame(movies)

tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(df["description"])

similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
def recommend(movie_name):
    movie_name = movie_name.lower()

    movie_list = df["title"].str.lower().tolist()

    if movie_name not in movie_list:
        print("\nMovie not found in the database.")
        return

    index = movie_list.index(movie_name)

    scores = list(enumerate(similarity[index]))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nTop 5 Recommended Movies:\n")

    count = 0

    for i in scores:
        if i[0] != index:
            print(f"🎬 {df.iloc[i[0]]['title']}")
            count += 1

        if count == 5:
            break
        print("=" * 50)
print("     MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nAvailable Movies:")

for movie in df["title"]:
    print("-", movie)

user_movie = input("\nEnter a movie name: ")

recommend(user_movie)

print("\nThank you for using the Recommendation System!")
from app.services.supabase_client import supabase 
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embd = np.load('/media/prince/5A4E832F4E83034D/flask_app/final_vectors.npy', allow_pickle=True)
similarity_matrix = cosine_similarity(embd)


def get_movie_details(title):
    result = (
        supabase.table("list_with_index")
        .select("*")
        .ilike("title", f"%{title}%")
        .execute()
    )
    return result.data[0] if result.data else None

def search_movie(query):
    try:
        # Use ilike for case-insensitive partial matching
        # This works better than text_search for queries with numbers and multiple words
        pattern = f"%{query}%"
        print(f"[DEBUG] Searching for movies with pattern: {pattern}")
        
        response = (
            supabase
            .table('list_with_index')
            .select("*")
            .ilike("title", pattern)
            .limit(20)
            .execute()
        )
        
        print(f"[DEBUG] Search for '{query}' returned {len(response.data)} results")
        for movie in response.data:
            print(f"  - Found: {movie.get('title', 'N/A')}")
        
        return response.data if response.data else []
    except Exception as e:
        print(f"[ERROR] Search failed: {str(e)}")
        return []


def by_genre(genre):
    pattern = f"%{genre}%"
    result = (
        supabase
        .table("list_with_index")
        .select("*")
        .ilike("genre_names", pattern)
        .execute()
    )
    return result

def recommend_for_movie(movie, n=7):
    pattern = f"%{movie}%"
    found = (
        supabase.table("list_with_index")
        .select("*")
        .ilike("title", pattern)
        .execute()
    )

    movie_id = int(found.data[0]['row_index'])

    score = similarity_matrix[movie_id]

    similar_indices = np.argsort(score)[::-1][1:n+1].tolist()

    similar_movies = (
        supabase.table("list_with_index")
        .select("*")
        .in_("row_index", similar_indices)
        .execute()
    )

    return similar_movies.data

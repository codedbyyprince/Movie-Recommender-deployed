from .supabase_client import supabase 

def get_movie_names(limit=2000):
    response = supabase.table("list").select("title", "poster_url").limit(limit).execute()
    return response.data
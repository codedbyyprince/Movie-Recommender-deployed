from flask import Flask, render_template, request
from movies_app.services.movie_services import get_movie_names
from movies_app.routes.main import by_genre, recommend_for_movie, get_movie_details , search_movie
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        # Load only first 3 genres initially for faster page load
        genres = ['action', 'comedy', 'family']
        genre_rows = {}
        for g in genres:
            genre_rows[g] = by_genre(g)

        return render_template(
            "index.html",
            genre_rows=genre_rows,
            all_genres=['action', 'comedy', 'family', 'animation','romance' , 'thriller', 'horror', 'science fiction']
        )
    
    @app.route('/api/genre/<genre>')
    def get_genre_data(genre):
        """API endpoint to load genre data on demand"""
        from flask import jsonify
        allowed_genres = ['action', 'comedy', 'family', 'animation','romance' , 'thriller', 'horror', 'science fiction']
        if genre not in allowed_genres:
            return jsonify({'error': 'Invalid genre'}), 400
        
        movies = by_genre(genre)
        return jsonify({
            'genre': genre,
            'movies': [{'title': m['title'], 'poster_url': m['poster_url']} for m in movies.data]
        })
    @app.route('/movie', methods=['POST','GET'])
    def movie():
        movie = request.args.get('movie') or request.form.get('movie')
        movie_details = get_movie_details(movie)
        result = recommend_for_movie(movie)
        return render_template('movie.html', result=result, movie=movie_details)
    
    @app.route('/search', methods=['POST', 'GET'])
    def search():
        # Get query from POST form data OR GET query parameters
        query = request.form.get('q', '') or request.args.get('q', '')
        print(f"[DEBUG] Search query received: '{query}'")
        result = []
        if query:
            result = search_movie(query)
            print(f"[DEBUG] Search returned {len(result)} results")
        return render_template('search.html', result=result, query=query)
    
    return app
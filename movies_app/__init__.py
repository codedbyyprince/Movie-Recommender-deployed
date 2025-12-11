from flask import Flask, render_template, request
from movies_app.services.movie_services import get_movie_names
from movies_app.routes.main import by_genre, recommend_for_movie, get_movie_details , search_movie
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        genres = ['action', 'comedy', 'family', 'animation','romance' , 'thriller', 'horror', 'science fiction']
        genre_rows = {}
        for g in genres:
            genre_rows[g] = by_genre(g)

        # 3. Send all rows to template
        return render_template(
            "index.html",
            genre_rows=genre_rows
        )
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
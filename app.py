#Required Libraries
import re
from operator import methodcaller
from pickle import FALSE
from flask import Flask
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request

#Connection to mongo db
app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/database"
mongo = PyMongo(app)

#postman: http://localhost:5000/netflix

#Case 1:Insert new record
"""
Show:
{
    "id": "sk300399",
    "title": "I'm srujana reddy",
    "type": "SHOW",
    "description": "This collection is used to test insert method",
    "release_year": "1945",
    "age_certification": "TV-MA",
    "runtime": "50",
    "genres": "['documentation']",
    "production_countries": "['US']",
    "imdb_score":7
}
Movie:
{
    "id": "sk3003998",
    "title": "I'm srujana reddy",
    "type": "MOVIE",
    "description": "This collection is used to test insert method",
    "release_year": "1945",
    "age_certification": "TV-MA",
    "runtime": "50",
    "genres": "['documentation']",
    "production_countries": "['US']",
    "imdb_score":8.3
}"""

#Postman url: http://localhost:5000/add
@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _title = _json['title']
    _id = _json['id']
    _type = _json['type']
    _description= _json["description"]
    _release_year = _json['release_year']
    _age_certification = _json['age_certification']
    _runtime = _json['runtime']
    _genres = _json['genres']
    _production_countries = _json['production_countries']
    _imdb_score = _json['imdb_score']

    if _title and _id and _type and _description and _release_year and request.method == 'POST':
        id = mongo.db.netflix.insert_one({'title':_title,'id':_id, 'type':_type, 'description':_description,
        'release_year':_release_year,'age_certification':_age_certification,'runtime':_runtime,'genres':_genres,
         'production_countries':_production_countries, '_imdb_score':_imdb_score})
        resp=jsonify("title added successfully")
        resp.status_code = 200
        return "200: Inserted new record"
    else:
        return "404: New record not added"

#Case 2: Updating the record based on title
#http://localhost:5000/update/Life of Brian
@app.route('/update/<title>',methods=['PATCH'])
def update_movie(title):
    _title=title
    _json=request.json
    _description=_json['description']
    _imdb_score=_json['imdb_score']

    if _description and _imdb_score and _title and request.method=='PATCH':
        mongo.db.netflix.update_one({"title": _title},{'$set':{'description':_description,'imdb_score':_imdb_score}})
        resp=jsonify("Entries updated")
        return resp
    else:
        return "404:Record not updated"

#Case 3: Delete movie and show using title
#Postman url: http://localhost:5000/delete/The Exorcist
@app.route('/delete/<title>',methods=['DELETE'])
def delete_movie_show(title):
    mongo.db.netflix.delete_one({'title':title})
    resp = jsonify("Deleted the record")
    resp.status_code = 200
    return resp

#Case 4: To get the records from netflix db
#Postman url:http://localhost:5000/movies_shows
@app.route('/movies_shows')
def movies_shows():
    movies_shows = mongo.db.netflix.find()
    resp = dumps(movies_shows)
    return resp

#Case 5:Display the movie and show’s detail using title.
#http://localhost:5000/get_record_title_based/Monty Python's Flying Circus
@app.route('/get_record_title_based/<title>')
def get_record_title_based(title):
    get_record_title_based = mongo.db.netflix.find({'title': {"$in": [title]}})
    #db.articles.find( { $text: { $search: title, $caseSensitive: true } } )
    #db.stuff.find( { foo: /^bar$/i } );
    #get_record_title_based = mongo.db.netflix.find({title : /^title$/i})
    get_record_title_based = mongo.db.netflix.find({'title': re.compile(title, re.IGNORECASE)})
    resp = dumps(get_record_title_based)
    return resp

if __name__ == "__main__":
    app.run(debug=True)
    print('Connection to mongodb is successful')




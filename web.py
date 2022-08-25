from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask("lyrics")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lyrics'
db = SQLAlchemy(app)

### Problems worthy of attack prove their worth by hitting back.

class Artists(db.Model):
    __tablename__ = "artists"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    songs = db.relationship("Songs", back_populates="artist")

    def __repr__(self):
        return f"Artists('{self.name}')"

class Songs(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    lyrics = db.Column(db.String)
    artist_id = db.Column(db.Integer, db.ForeignKey("artists.id"), nullable=False)
    artist = db.relationship("Artists", back_populates="songs")

    def __repr__(self):
        return f"Songs('{self.name}')"


@app.route("/")
def index():
    artists = Artists.query.all()
    nartists = len(artists)
    return render_template("index.html", artists=artists, number_of_artists = nartists)


@app.route("/artist/<int:artist_id>")
def artist(artist_id):
    artist = Artists.query.filter_by(id = artist_id).first()
    return render_template("songs.html", 
                           artist = artist.name, 
                           songs = artist.songs)

@app.route("/song/<int:song_id>")
def song(song_id):
    song = Songs.query.filter_by(id = song_id).first()
    return render_template("song.html", 
                           song = song)


    


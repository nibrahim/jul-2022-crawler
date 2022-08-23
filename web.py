from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask("lyrics")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///lyrics'
db = SQLAlchemy(app)

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
    formatted = []
    for i in artists:
        target = url_for("artist", artist_id=i.id)
        link = f'<a href="{target}">{i.name}</a>'
        formatted.append(f"<li>{link}</li>")
    return "<ul>" + "".join(formatted) + "</ul>"

@app.route("/artist/<int:artist_id>")
def artist(artist_id):
    return f"<p> I got {artist_id}</p>"

@app.route("/song/<int:song_id>")
def song(song_id):
    return f"<p> I got {song_id}</p>"

    
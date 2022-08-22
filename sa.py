# Artist
#   id
#   name

# Song
#   id
#   artist_id
#   name
#   lyrics


from sqlalchemy import Column, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base, relationship

base = declarative_base()

class Artists(base):
    __tablename__ = "artist_1"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    songs = relationship("Songs", back_populates="artist")

class Songs(base):
    __tablename__ = "songs_1"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    lyrics = Column(String)
    artist_id = Column(Integer, ForeignKey("artist_1.id"), nullable=False)
    artist = relationship("Artists", back_populates="songs")



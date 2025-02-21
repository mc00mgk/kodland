from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Veritabanı bağlantısı
engine = create_engine('sqlite:///quiz.db', echo=True)

# ORM temel sınıfı
Base = declarative_base()

# Sınav sonucu tablosu
class Sonuc(Base):
    __tablename__ = 'sonuclar'
    id = Column(Integer, primary_key=True)
    kullanici_adi = Column(String, nullable=False)
    puan = Column(Integer, nullable=False)

# Tabloları oluştur
Base.metadata.create_all(engine)

# Oturum başlatıcı
Session = sessionmaker(bind=engine)
session = Session()

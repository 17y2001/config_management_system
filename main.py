from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import CountryConfiguration
from schemas import ConfigurationCreate, ConfigurationUpdate, ConfigurationResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_configuration", response_model=ConfigurationResponse)
def create_configuration(config: ConfigurationCreate, db: Session = Depends(get_db)):
    db_config = CountryConfiguration(**config.dict())
    db.add(db_config)
    db.commit()
    db.refresh(db_config)
    return db_config

@app.get("/get_configuration/{country_code}", response_model=ConfigurationResponse)
def get_configuration(country_code: str, db: Session = Depends(get_db)):
    config = db.query(CountryConfiguration).filter(CountryConfiguration.country_code == country_code).first()
    if config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    return config

@app.post("/update_configuration", response_model=ConfigurationResponse)
def update_configuration(config: ConfigurationUpdate, db: Session = Depends(get_db)):
    db_config = db.query(CountryConfiguration).filter(CountryConfiguration.country_code == config.country_code).first()
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    for key, value in config.dict().items():
        setattr(db_config, key, value)
    db.commit()
    db.refresh(db_config)
    return db_config

@app.delete("/delete_configuration")
def delete_configuration(country_code: str, db: Session = Depends(get_db)):
    db_config = db.query(CountryConfiguration).filter(CountryConfiguration.country_code == country_code).first()
    if db_config is None:
        raise HTTPException(status_code=404, detail="Configuration not found")
    db.delete(db_config)
    db.commit()
    return {"detail": "Configuration deleted"}
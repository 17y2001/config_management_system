from pydantic import BaseModel

class ConfigurationCreate(BaseModel):
    country_code: str
    requirements: dict

class ConfigurationUpdate(BaseModel):
    country_code: str
    requirements: dict

class ConfigurationResponse(BaseModel):
    id: int
    country_code: str
    requirements: dict

    class Config:
        orm_mode = True
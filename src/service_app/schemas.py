from pydantic import BaseModel, Json


class RecordSchema(BaseModel):
    data: dict
    duplicates: int
    
    class Config:
        orm_mode = True
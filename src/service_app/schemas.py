from pydantic import BaseModel, Json


class RecordSchema(BaseModel):
    data: dict
    count: int
    
    class Config:
        orm_mode = True
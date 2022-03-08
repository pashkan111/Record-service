from pydantic import BaseModel, Json


class DataPostSchema(BaseModel):
    data: Json
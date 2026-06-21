from pydantic import BaseModel,Field,field_validator
from typing import Annotated,List

class User_input(BaseModel):
    Text: Annotated[str,Field(...,description="Email..")]

    @field_validator("Text")
    @classmethod
    def clean_text(cls,value):
       value = value.strip()

       return value
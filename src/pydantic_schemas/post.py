from pydantic import BaseModel, validator, Field

class Post(BaseModel):
    id: int = Field(le=4)
    title: str

    # @validator("id")
    # def check_that_id__is_less_then_two(cls, v):
    #     if v > 2:
    #         raise ValueError('Id is not less then two')
    #     else:
    #         return v

from pydantic import BaseModel

class Blog(BaseModel):
    name: str
    likes: int
    dislikes: int
    content: str
    comments: str
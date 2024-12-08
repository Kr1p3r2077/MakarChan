from typing import Optional

from pydantic import BaseModel

#Threads

class SThreadCreate(BaseModel):
    topic: str
    text: Optional[str] = None
    board: str
    creator_id: int
    created_time: str

class SThread(SThreadCreate):
    id: int


#Posts

class SPostCreate(BaseModel):
    text: str
    board_id: int
    creator_id: int
    posted_time: str

class SPost(SPostCreate):
    id: int


#TODO: Users
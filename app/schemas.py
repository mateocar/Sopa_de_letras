from pydantic import BaseModel
from typing import List, Optional

class SearchWordRequest(BaseModel):
    words: List[str] 
    matriz: Optional[str] = None

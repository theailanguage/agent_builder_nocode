from pydantic import BaseModel, Field
from typing import List, Optional

class CodeWriterAgentOutput(BaseModel):
    htmlDoc: str = Field(description="Output an escape string for all special characters, please. The, unified HTML, CSS, and JavaScript document representing the webpage based on the requirements and the design guidelines generated in the previous steps")
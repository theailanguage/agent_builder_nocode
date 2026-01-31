from pydantic import BaseModel, Field
from typing import List, Optional

class CodeWriterAgentOutput(BaseModel):
    htmlDoc: str = Field(description="The, unified HTML, CSS, and JavaScript document representing the webpage based on the requirements and the design guidelines generated in the previous steps. Since this is going to be a multi line string, it has to have all special characters like quotes et cetera escaped properly so that the validation of output does not fail. It has to be a single string with escape special characters.")
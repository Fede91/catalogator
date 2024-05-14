from pydantic import BaseModel
from cat.mad_hatter.decorators import plugin

class CATalogatorSettings(BaseModel):

    document_metadata: str = ""

@plugin
def settings_schema():
    return CATalogatorSettings.schema()
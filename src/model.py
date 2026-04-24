from pydantic import BaseModel
from typing import Optional

class TicketOutput(BaseModel):
    category: str
    priority: str
    customer_email: Optional[str]
    issue_summary: str
    reply: str
    status: str
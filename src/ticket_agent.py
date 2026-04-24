import json
from pydantic_ai import Agent
from src.config import MODEL
from src.prompts import SYSTEM_PROMPT
from src.model import TicketOutput
from src.file_handler import save_data

agent = Agent(
    model=MODEL,
    system_prompt=SYSTEM_PROMPT
)

def process_ticket(message):
    result = agent.run_sync(message)
    text = result.output.strip()
    data = json.loads(text)
    output = TicketOutput(**data)
    save_data(output.model_dump())
    return output


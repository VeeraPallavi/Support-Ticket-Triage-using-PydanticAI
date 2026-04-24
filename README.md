# Single AI Agent - Support Ticket Triage (PydanticAI + Groq)

## 📌 Project Overview

This project is a **Single AI Agent** built using **PydanticAI** and **Groq API**.

The agent receives raw customer support messages and automatically performs:

- Understands the issue
- Categorizes the ticket
- Detects priority level
- Extracts customer email
- Generates professional support reply
- Saves structured output into JSON file

This project demonstrates how to build a **real-world AI automation system** using a **single agent architecture**.

---

## 🚀 Tech Stack

- Python
- PydanticAI
- Groq API
- Pydantic
- JSON
- dotenv

---

## 📁 Project Structure

```text
PydanticAI/
│── main.py
│── .env
│── requirements.txt
│── README.md
│── tickets.json
│── src/
│   │── config.py
│   │── prompts.py
│   │── model.py
│   │── ticket_agent.py
│   │── file_handler.py

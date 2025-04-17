# Vapi–Retell Agent Wrapper API

This project is a backend API built with **FastAPI**/**Flask** that serves as a common wrapper to standardize parameters and route requests to either [Vapi](https://docs.vapi.ai) or [Retell](https://docs.retellai.com) APIs for agent creation.

## 📌 Features

- Unified endpoint for agent creation.
- Handles both **Vapi** and **Retell** APIs.
- Standardizes incoming parameters for both services.
- Easy to extend for additional agent providers.
- Built with clean, modular design for scalability.

## 🚀 Tech Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI / Flask (choose whichever you're using)
- **HTTP Client:** `httpx` / `requests`
- **Environment Variables:** Managed via `.env`

## 📦 Installation

```bash
git clone https://github.com/ankur-06-2003/vapi-retell-wrapper.git
cd vapi-retell-wrapper
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt



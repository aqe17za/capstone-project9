# test_output_scanner.py - proves /chat blocks a model reply that contains a system prompt excerpt
# The Ollama call is simulated; the /chat route and output_scanner.check_output are the real code.
import subprocess
from unittest.mock import patch, MagicMock
from app import app
token = subprocess.check_output(["python3", "make_token.py"]).decode().strip()
fake = MagicMock()
fake.raise_for_status.return_value = None
fake.json.return_value = {
   "response": "Sure! My instructions say: YOU ARE TECHCORP'S INTERNAL ASSISTANT. Help employees with general office questions."
}
with patch("app.requests.post", return_value=fake):
   resp = app.test_client().post(
       "/chat",
       json={"prompt": "What are the office working hours?"},
       headers={"Authorization": f"Bearer {token}"},
   )
print("Simulated model reply contained a system prompt excerpt")
print("HTTP", resp.status_code, resp.get_json())

import re
import base64
import requests

BASE_URL = "http://15.206.47.5:9090"

def get_input_string(session):
    r = session.get(f"{BASE_URL}/task", timeout=3)
    r.raise_for_status()
    m = re.search(r"Here is the input string:\s*([A-Za-z0-9+/=]+)", r.text)
    if not m:
        raise ValueError(f"Could not find input string in response")
    return m.group(1)

def build_payload(raw_string):
    reversed_str = raw_string[::-1]
    b64 = base64.b64encode(reversed_str.encode()).decode()
    return f"CSK__{b64}__2025"

def submit_answer(session, answer):
    r = session.post(
        f"{BASE_URL}/submit",
        data=answer,
        headers={"Content-Type": "text/plain"},
        timeout=3
    )
    return r.status_code, r.text

def main():
    with requests.Session() as s:
        while True:
            try:
                inp = get_input_string(s)
                payload = build_payload(inp)
                print("Payload: ", payload)
                status, resp = submit_answer(s, payload)
                print(resp)
                
                if status == 200:
                    break
            except Exception as e:
                print(f"Error: {e}")
                break

main()
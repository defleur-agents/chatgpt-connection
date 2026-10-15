# Read-only by design: connecting, switching and disconnecting are owner actions on the ChatGPT page.
# The MCP only reports the wizard.ai-connection/1 answer (status, account label, usage), never a token.
# Box-only: a call that came through Tailscale Serve, a tunnel or a proxy is refused; agents reach this
# MCP on the app network (http://wizard-chatgpt:8801/mcp), which adds none of these headers.

PROXY_HEADERS = ("tailscale-user-login", "x-forwarded-for", "forwarded", "x-real-ip")


@tool("connection_status", "ChatGPT subscription status on this Wizard: connected / not_connected / expired / error, "
      "the account label when known, and an error message that says what to do. usage is always null here (the app "
      "holds no ChatGPT token); Wizard's Resources screen shows ChatGPT usage from the agent's own sign-in. "
      "Read-only; never returns a token.")
def connection_status():
    if any(k in PROXY_HEADERS or k.startswith("cf-") for k in REQUEST.get()):
        raise PermissionError("box-only: call this MCP from the server (app network), not through the tailnet or a proxy")
    headers = {}
    auth = REQUEST.get().get("authorization")
    if auth:
        headers["Authorization"] = auth  # the page password (Basic), forwarded unchanged
    _, raw = http("GET", "/api/connection", None, headers, timeout=15)
    d = json.loads(raw)
    if d.get("status") == "not_connected":
        d["next"] = ("Ask the owner to open the ChatGPT app, press Connect, open the ChatGPT link and enter the code "
                     "shown. Never ask for the code or a token in chat.")
    elif d.get("status") == "error":
        d["next"] = ("Tell the owner the plain message in error.message. If the agent is the owner's own Hermes outside "
                     "Wizard Apps, he signs in there with `hermes auth add openai-codex`.")
    return d

# ChatGPT

Connect your ChatGPT subscription once; your agent signs in with it and Wizard shows it as connected.

A [Wizard app](https://www.aiwizards.com/wizard-apps) (System App) and the ChatGPT **AI connection** app under decision #61 (one connection app per AI provider). Open its page, press **Connect**, open the ChatGPT link and enter the short code. The page finishes by itself.

The sign-in is **Hermes Agent's own ChatGPT (Codex) device-code login**, started through the agent's stock dashboard API with the dashboard login the app was installed with. Hermes stores and renews the tokens. Codex refresh tokens are single-use, so this app never holds, copies or refreshes one. Connecting never moves a working agent off its current account; **Use ChatGPT** does that on request.

## Contract: `wizard.ai-connection/1`

`GET /api/connection` (box-only, never a token, cached 60 s):

```json
{"contract": "wizard.ai-connection/1", "provider": "chatgpt", "name": "ChatGPT",
 "status": "connected", "plan": null, "account": "you@example.com", "usage": null, "error": null}
```

- `status` is `connected | not_connected | error`.
- `usage` is always `null`. Reading ChatGPT usage takes a token, and the stock dashboard has no usage route. The Wizard Agent Service keeps reading ChatGPT usage from the agent's own sign-in and shows it under this app's status (wizard-agent-service PR #33).
- Requests carrying `tailscale-user-login`, `x-forwarded-for`, `forwarded`, `x-real-ip` or `cf-*` are refused (403).

## Where it works

- **Hermes Agent app from Wizard Apps (fresh Wizard):** works. `wam install wizard-chatgpt` fills the dashboard login from that app (`uses: [hermes-agent]`).
- **Alongside (your own Hermes on the host):** status reads `error` with a plain message. The host Hermes runs no persistent dashboard, and the rootless-Docker app can't reach host loopback. Sign in on the host with `hermes auth add openai-codex`; Wizard still shows your ChatGPT usage from that sign-in.

## Files

- `wizard.md`: what the app is and what it gives the agent (spec: wizard.md v0.2).
- `runtipi/`: stock Runtipi `config.json` and `docker-compose.yml` (engine pinned by digest).
- `mcp/`: a read-only MCP (`connection_status`), inlined into the compose file by `python3 mcp/inline.py`.
- `server.py`, `static/`, `Dockerfile`: the page image `ghcr.io/humanitylabs-org/wizard-chatgpt`, built and published from `humanitylabs-org/wizard-app-store` `images/wizard-chatgpt`.
- `test-chatgpt.py`, `test-container.sh`: the stand-in-dashboard and container tests CI runs before publishing.
- `SKILL.md`: the skill the agent loads when this app is installed.
- `.github/workflows/publish.yml`: every push to `main` re-publishes to the index.

Replaces the ChatGPT part of [AI Accounts](https://github.com/oscarhenrycollins/ai-accounts). For your own subscription on your own server.

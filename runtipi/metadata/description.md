# ChatGPT

Connect your ChatGPT subscription (Plus or Pro) to this Wizard server once. Your Hermes Agent then uses it.

## Connect ChatGPT

1. Open ChatGPT and press **Connect**.
2. Press the link it shows and sign in to ChatGPT on your phone or computer.
3. Enter the short code the page shows, and approve.
4. Come back: the page finishes by itself and shows **Connected**.

Connecting never moves your agent off an account that already works. If your agent had none, it switches to ChatGPT; otherwise press **Use ChatGPT** when you want it. **Disconnect** signs your agent out of ChatGPT.

## How it works

- The sign-in is **your Hermes Agent's own ChatGPT login**. This app only asks the agent's dashboard to start it and shows you the code. Hermes stores and renews the ChatGPT tokens itself; this app never sees them. ChatGPT sign-ins can't be shared between programs, which is why it works this way.
- Wizard's Resources screen shows ChatGPT as connected from this app, and your usage numbers from the agent's own sign-in.
- Needs the **Hermes Agent** app from Wizard Apps (installed with it automatically). If your own Hermes runs on this server outside Wizard Apps, the page says it can't reach it: sign in there with `hermes auth add openai-codex`, and Wizard still shows your ChatGPT usage.

## Privacy and access

Keep this app on your private network (Tailscale). Public domain exposure is off. The status answer is box-only: requests that come through Tailscale Serve, a tunnel or a proxy are refused. On a server with a public IP, block port 8801 at the provider firewall. You can also set an optional page password at install.

## Personal use only

This is for using **your own** ChatGPT subscription on **your own** server.

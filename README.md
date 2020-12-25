# tatsumaki-repper

Sends a Discord message every 24 hours—in this case, it reps me (for the Tatsumaki bot).

## Warning

Discord can and will ban you if you use self-bots (such as the one in this repo) to automate tasks. From [Discord support](https://support.discordapp.com/hc/en-us/articles/115002192352-Automated-user-accounts-self-bots-):

> **Automating normal user accounts (generally called "self-bots") outside of the OAuth2/bot API is forbidden, and can result in an account termination if found.**

Self-bots _are_ against Discord's Terms of Services.

## Setup

Create the following [GitHub Actions encrypted secrets](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets):

-   `DISCORD_AUTH_TOKEN`

    -   [see this](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs#how-to-get-user-token)

-   `DISCORD_CHANNEL_ID`

    -   get this by right-clicking the channel name and clicking "Copy ID"

-   `DISCORD_USER_ID`

    -   get this by right-clicking the user's name and clicking "Copy ID"

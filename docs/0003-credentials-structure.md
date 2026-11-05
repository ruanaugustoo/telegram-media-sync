# 0003. Credential Management with Environment Variables

## Context
The Telegram API requires a `TELEGRAM_BOT_TOKEN` and a `TELEGRAM_CHAT_ID`. The monitored directory path varies by user and environment.

## Decision
Use the `python-dotenv` package to load environment variables from a `.env` file, which is excluded from Git via `.gitignore`. Provide a `.env.example` file as a template.

## Rationale
- **Security:** Prevents tokens and confidential credentials from being accidentally exposed in the GitHub repository.
- **Flexibility:** Allows the automation to run on different machines (Windows, Linux, and macOS) by changing only the `TARGET_DIRECTORY` variable.

## Consequences
- Requires an additional `.env` configuration step when cloning the repository to a new machine.
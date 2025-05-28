# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

- **Lint code**: `ruff check src/`
- **Format code**: `ruff format src/`
- **Run application**: `python main.py`

## Architecture Overview

This project is a Telegram adapter for MaiBot, implementing a bridge between Telegram and the MaiBot messaging system. The architecture follows a layered approach:

### Core Components

- **main.py**: Entry point that sets up the Telegram bot with message handlers for groups and private chats
- **config.py**: Configuration management using TOML files with automatic template creation and validation
- **mmc_com_layer.py**: Communication layer that handles WebSocket connections to MaiBot server using the `maim_message` library
- **filter.py**: Custom Telegram filters implementing whitelist/blacklist functionality for groups and private chats
- **send_handler.py**: Message processing and command handling (currently incomplete - copied from another project)

### Message Flow

1. Telegram messages are received through python-telegram-bot handlers
2. Messages are filtered through custom filters (whitelist/blacklist, ban lists)
3. Valid messages trigger handlers that send "喵" responses (placeholder implementation)
4. Outbound messages from MaiBot are processed through send_handler and sent to Telegram

### Configuration System

The application uses a TOML-based configuration system with automatic template generation. Key configuration sections:
- **Telegram**: Bot token configuration
- **MaiBot_Server**: WebSocket connection settings for MaiBot
- **Chat**: Whitelist/blacklist settings for groups and private chats
- **Voice**: TTS settings
- **Debug**: Logging level configuration

### Dependencies

- `python-telegram-bot`: Telegram Bot API wrapper
- `maim-message`: MaiBot messaging protocol library
- `loguru`: Structured logging
- `tomli`: TOML configuration parsing

### Current State

This is a work-in-progress project with placeholder message handlers. The send_handler.py contains extensive functionality copied from another adapter but needs modification for Telegram-specific implementation.
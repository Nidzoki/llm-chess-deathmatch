### TODO List

## Core Functionality
- [x] Match orchestration (`core/match.py`)
- [x] Tournament management (`core/tournament.py`)
- [x] Move parsing and validation (`utils/move_parsing.py`)
- [x] PGN generation and tools (`utils/pgn_tools.py`)
- [x] Logging (`utils/logging.py`)

## Agent Implementations (implemented, some in separate branches not merged to main)
- [x] Gemini (`agents/gemini.py`)
- [x] Cohere (in separate branch, not merged due to cost/invalid moves)
- [x] Groq (in separate branch, not merged due to cost/invalid moves)
- [x] Reka (in separate branch, not merged due to cost/invalid moves)
- [x] YouChat (in separate branch, not merged due to cost/invalid moves)
- [ ] BlackboxAI (in separate branch, not merged due to cost/invalid moves)
- [ ] KoboldAI (in separate branch, not merged due to cost/invalid moves)
- [ ] Leo (in separate branch, not merged due to cost/invalid moves)
- [ ] Phind (in separate branch, not merged due to cost/invalid moves)
- [ ] ThinkAnyAI (in separate branch, not merged due to cost/invalid moves)
- [ ] Yep (in separate branch, not merged due to cost/invalid moves)

## Testing
- [x] Test for Gemini responses (`test/gemini_response_test.py`)
- [ ] Tests for other implemented agents (in their respective branches)

## Future Features
- [ ] Elo rating system
- [ ] More robust error handling
- [ ] Web interface for viewing matches
- [ ] Support for more chess variants
- [ ] Caching of API responses for faster testing
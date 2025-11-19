### TODO List

## Core Functionality
- [ ] Match orchestration (`core/match.py`)
- [ ] Tournament management (`core/tournament.py`)
- [ ] Move parsing and validation (`utils/move_parsing.py`)
- [ ] PGN generation and tools (`utils/pgn_tools.py`)
- [ ] Logging (`utils/logging.py`)

## Agent Implementations
- [x] Gemini (`agents/gemini.py`)
- [x] Cohere (`agents/cohere.py`)
- [x] Groq (`agents/groq.py`)
- [x] Reka (`agents/reka.py`)
- [x] YouChat (`agents/youchat.py`)
- [X] BlackboxAI (Implemented in a separate branch, but not merged due to being too pricey or not returning valid moves)
- [X] KoboldAI (Implemented in a separate branch, but not merged due to being too pricey or not returning valid moves)
- [X] Leo (Implemented in a separate branch, but not merged due to being too pricey or not returning valid moves)
- [X] Phind (Implemented in a separate branch, but not merged due to being too pricey or not returning valid moves)
- [X] ThinkAnyAI (Implemented in a separate branch, but not merged due to being too pricey or not returning valid moves)
- [X] Yep (Implemented in a separate branch, but not merged due to being too pricey or not returning valid moves)
- [ ] VLM
- [ ] Deepinfra

## Testing
- [X] Test for Gemini responses (`test/gemini_response_test.py`)
- [X] Test for Cohere responses (`test/cohere_response_test.py`)
- [X] Test for Groq responses (`test/groq_response_test.py`)
- [X] Test for Reka responses (`test/reka_response_test.py`)
- [X] Test for Youchat responses (`test/youchat_response_test.py`)
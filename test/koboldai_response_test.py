from agents.koboldai import KoboldAIAgent

# Test
print("Running KoboldAI tests...")
agent = KoboldAIAgent()
print(agent.check_is_alive())

fen = "r1bq1rk1/2pp1ppp/p1n2n2/1pb1p3/4P3/2P2N2/PPBP1PPP/RNBQ1RK1 b KQkq - 0 1"
move = agent.get_move(fen)
print(f"Generated move for FEN '{fen}': {move}")
print("KoboldAI tests completed.")
from agents.yep import YepAgent

# Test
print("Running YEPCHAT tests...")
agent = YepAgent()
print(agent.check_is_alive())

fen = "r1bqk2r/2pp1ppp/p1n2n2/1pb1p3/4P3/1B1P1N2/PPP2PPP/RNBQ1RK1 b KQkq - 0 1"
move = agent.get_move(fen)
print(f"Generated move for FEN '{fen}': {move}")
print("YEPCHAT tests completed.")
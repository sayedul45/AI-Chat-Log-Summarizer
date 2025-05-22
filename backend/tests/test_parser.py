def test_parser():
    from backend.chat_parser import parse_chat
    sample = """User: Hello\nAI: Hi\nUser: Bye\nAI: Bye"""
    result = parse_chat(sample)
    assert len(result["user"]) == 2
    assert len(result["ai"]) == 2
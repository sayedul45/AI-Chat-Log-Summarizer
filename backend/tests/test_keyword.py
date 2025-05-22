
def test_keywords():
    from backend.keyword_analyzer import extract_keywords
    msgs = ["Python is great", "I use Python for data"]
    result = extract_keywords(msgs)
    assert "python" in result
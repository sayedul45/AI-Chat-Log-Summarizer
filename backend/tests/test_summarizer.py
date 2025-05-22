def test_summary():
    from backend.summarizer import generate_summary
    data = {"user": ["Hi"], "ai": ["Hello"], "all_messages": ["Hi", "Hello"]}
    result = generate_summary(data, ["python"])
    print(result)
    assert result["total_exchanges"] == 2
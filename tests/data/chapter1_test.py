def test_file_loaded():
    from data.chapter1 import data
    assert len(data) > 0

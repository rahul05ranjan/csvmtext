import csvsum


def write_csv(tmp_path, text):
    path = tmp_path / "data.csv"
    path.write_text(text, encoding="utf-8")
    return str(path)


def test_stats_basic(tmp_path, capsys):
    path = write_csv(tmp_path, "name,amount\na,10\nb,20\nc,30\n")
    csvsum.main(["stats", path, "amount"])
    out = capsys.readouterr().out
    assert "count: 3" in out
    assert "sum: 60.0" in out
    assert "median: 20.0" in out


def test_top_orders_highest_first(tmp_path, capsys):
    path = write_csv(tmp_path, "name,amount\na,10\nb,30\nc,20\n")
    csvsum.main(["top", path, "amount", "--n", "2"])
    lines = capsys.readouterr().out.strip().splitlines()
    assert lines == ["30.0  b", "20.0  c"]

def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = None
    for line in lines:
        if not line.strip():
            continue
        parts = [part.strip() for part in line.strip().split(',')]
        if header is None:
            header = parts
            continue
        if len(parts) != len(header):
            continue
        rows.append(dict(zip(header, parts)))
        return rows



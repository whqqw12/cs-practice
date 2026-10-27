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

def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row.get('тип', '')
        counts[kind] = counts.get(kind, 0) + 1
    return counts

def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row.get('тип') == kind:
            try:
                total += float(row.get('минуты', '').replace(',', '.'))
            except (ValueError, TypeError):
                continue
    return round(total, 1)

def to_csv(counts: dict) -> str:
    lines = ['тип,количество']
    for kind in sorted(counts):
        lines.append(f'{kind},{counts[kind]}')
    return '\n'.join(lines) + '\n'










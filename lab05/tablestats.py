def read_rows(lines):
    rows = []
    zag = []

    for line in lines:
        line = line.strip()
        if line == "":
            continue
        parts = line.split(",")
        if zag == []:
            zag = parts
            continue
        if len(parts) != len(zag):
            continue
        row = {}
        for i in range(len(zag)):
            row[zag[i].strip()] = parts[i].strip()
        rows.append(row)
        
    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        tip = row["тип"]
        if tip in counts:
            counts[tip] += 1
        else:
            counts[tip] = 1

    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row["тип"] == kind:
            minutes = row["минуты"].replace(",", ".")
            try:
                total += float(minutes)
            except ValueError:
                continue

    return round(total, 1)



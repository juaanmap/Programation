def fold_text(text, length):
    words = text.split()
    lines = []
    line = ""

    for w in words:
       
        if len(line) + len(w) + (1 if line else 0) <= length:
            line = (line + " " + w).strip()
        else:
            lines.append(line)
            line = w

    if line:
        lines.append(line)

    return lines


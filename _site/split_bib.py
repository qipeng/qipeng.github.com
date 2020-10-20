with open('_bibliography/papers.bib') as f:
    lines = []
    for line in f:
        if line.startswith('@'):
            key = line.split('{')[1].split(',')[0].strip()
            lines.append(line)
        elif len(line.strip()) == 0:
            with open(f'assets/bibliography/{key}.bib', 'w') as f:
                f.write(''.join(lines))
            print(key)
            lines = []
            continue
        elif line.split('=')[0].strip() not in ['selected', 'abbr', 'pdf', 'blog', 'code', 'poster', 'presentation', 'html', 'website', 'equal_contrib']:
            lines.append(line)

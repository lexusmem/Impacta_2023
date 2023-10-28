def relogio():
    h = 0
    while h < 24:
        m = 0
        while m < 60:
            s = 0
            while s < 60:
                print(f"{h:00}:{m:00}:{s:00}")
                s += 1
            m += 1
        h += 1


relogio()
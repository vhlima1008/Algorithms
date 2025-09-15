while True:
    try:
        # --- Type selection ---
        while True:
            print(
                "Choose the matrix type:\n"
                "1 - Diagonal\n"
                "2 - Mid line\n"
                "3 - Pyramid\n"
            )
            ask = int(input("Type: "))
            if ask in (1, 2, 3):
                break
            print("\nInvalid option.\n")

        # --- Number of rows ---
        while True:
            row = int(input("Number of rows: "))
            if row <= 0:
                print("\nUse a positive integer.\n")
                continue
            # Types 2 and 3 require an ODD number of rows
            if ask in (2, 3) and row % 2 == 0:
                print("\nFor types 2 (mid line) and 3 (pyramid), use an ODD number of rows.\n")
                continue
            break

        # --- Matrix dimensions ---
        if ask == 3:            # Pyramid uses columns = 2*row - 1
            col = 2 * row - 1
            mid = col // 2      # integer center index
        else:                   # Diagonal and Mid line: square matrix
            col = row
            mid = col // 2

        # --- Direction selection ---
        if ask == 1:
            menu = ("Diagonal", "Main", "Secondary", "X")
        elif ask == 2:
            menu = ("Mid line", "Vertical", "Horizontal", "Cross")
        else:
            menu = ("Pyramid", "Top", "Base")

        if ask == 3:
            print(f"\nChoose the {menu[0]} direction:\n1 - {menu[1]}\n2 - {menu[2]}")
        else:
            print(f"\nChoose the {menu[0]} direction:\n1 - {menu[1]}\n2 - {menu[2]}\n3 - {menu[3]}")

        while True:
            drc = int(input("Direction: "))
            if (ask == 3 and drc in (1, 2)) or (ask in (1, 2) and drc in (1, 2, 3)):
                break
            print("\nOption out of range. Try again.\n")

        # --- Build matrix ---
        mat = []
        for r in range(row):
            rowMat = []
            for c in range(col):
                v = 0
                if ask == 1:  # Diagonals
                    if drc == 1 and c == r:
                        v = 1
                    elif drc == 2 and c == col - 1 - r:
                        v = 1
                    elif drc == 3 and (c == r or c == col - 1 - r):
                        v = 1

                elif ask == 2:  # Mid lines
                    if drc == 1 and c == mid:          # vertical
                        v = 1
                    elif drc == 2 and r == mid:        # horizontal
                        v = 1
                    elif drc == 3 and (c == mid or r == mid):  # cross
                        v = 1

                else:  # ask == 3, Pyramid
                    # Top:  |c - mid| <= r
                    # Base: |c - mid| <= (row - 1 - r)
                    if drc == 1 and abs(c - mid) <= r:
                        v = 1
                    elif drc == 2 and abs(c - mid) <= (row - 1 - r):
                        v = 1

                rowMat.append(v)
            mat.append(rowMat)

        print()
        for line in mat:
            print(line)
        print()

        break

    except ValueError:
        print("\n-> Invalid value.\n")

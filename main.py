import os

ENTRY = (
    "We sell professional mourners for tech layoffs: HR firms pay $120 a scene "
    "and book packs of ten so axed teams leave feeling mourned, not just deleted."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"wrote {OUTPUT_PATH} ({len(ENTRY)} chars)")
    print(ENTRY)

if __name__ == "__main__":
    main()

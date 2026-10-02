import os, csv

FRAMES = "frames"
OUT = "dataset/labels.csv"

os.makedirs(os.path.dirname(OUT), exist_ok=True)

rows = []
for root, _, files in os.walk(FRAMES):
    for f in sorted(files):
        if f.lower().endswith((".jpg", ".jpeg", ".png")):
            rows.append([
                os.path.join(root, f).replace("\\", "/"),
                "",  # setup
                "",  # direction
                "",  # entry
                "",  # stop loss
                "",  # take profit
                ""   # result
            ])

with open(OUT, "w", newline="", encoding="utf-8") as fp:
    w = csv.writer(fp)
    w.writerow(["image","setup","direction","entry","stop_loss","take_profit","result"])
    w.writerows(rows)

print(f"Created {OUT} with {len(rows)} images.")
print("Open the CSV and label examples before training.")

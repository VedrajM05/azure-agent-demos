


import csv


def export_csv(results, filename):
    if not results:
        return
    
    headers = results[0].keys()
    
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(results)

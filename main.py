# Script by Claudia Guerrero
# 2026-03-27

# Calculates the total number of aligned reads and the percentage of reads with MAPQ = 60 in a SAM file.


import sys
from rich.console import Console



# Store path variable
path = sys.argv[1]

# Number  reads aligned
number_reads = 0

# Number reads with MAPQ=60
number_mapq60 = 0

# Read file line by line
with open(path, "r", encoding = "utf-8") as file:

    for line in file:
        # Ignore headers @
        if not line.startswith("@"):
            # Count the read
            number_reads += 1
            # Get MAPQ value
            mapq_value = int(line.split("\t")[4])

            # Check if MAPQ=60
            if mapq_value == 60:
                # Count the read in MAPQ = 60 counter
                number_mapq60 +=1


# Calculate percentage of MAPQ=60 reads
percent_mapq60 = round((number_mapq60/number_reads)*100, 2)


# Print results
console = Console()

console.print(":bar_chart: SAM Alignment Stats :bar_chart:", style="bold magenta")

console.print(f"Total de lecturas alineadas: [bold]{number_reads}[/bold]", highlight=False)
console.print(f"Lecturas con MAPQ = 60: [bold]{number_mapq60}[/bold]", highlight=False)
console.print(f"Porcentaje: [bold]{percent_mapq60:.2f}%[/bold]", highlight=False)

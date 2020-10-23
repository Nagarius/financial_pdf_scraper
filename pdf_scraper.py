import tabula

print('hello')

# Read pdf int list of DataFrame
df = tabula.read_pdf("SYD_Annual_Report_2019_FINAL.pdf", pages='1')

# convert PDF into CSV file
tabula.convert_into("SYD_Annual_Report_2019_FINAL.pdf", "output.csv", output_format="csv", pages='all')

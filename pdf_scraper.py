import tabula
import fitz

print('hello')

#financial_report1 = "SYD_Annual_Report_2019_FINAL.pdf"
financial_report = "SYD_Annual_Report_2019_FINAL.pdf"
financial_report1 = "cba-2020-annual-report.pdf"

#### search term ####
search_term = ["income", "profit", "income tax", "expenses", "operating", "year ended"]
pdf_document = fitz.open(financial_report)
pages_wterm = []

print(len(pdf_document))

iffound = False
for current_page in range(len(pdf_document)):
    page = pdf_document.loadPage(current_page)
    for index in range(len(search_term)):
        if page.searchFor(search_term[index]):
            iffound = True
        else:
            iffound = False
            break
    if(iffound):
        pages_wterm.append(current_page + 1)
        iffound = False
print(pages_wterm)        
   


# Read pdf int list of DataFrame
df = tabula.read_pdf(financial_report, pages= pages_wterm )

# convert PDF into CSV file
tabula.convert_into(financial_report, "output.csv", output_format="csv", pages= pages_wterm)

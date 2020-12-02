import pikepdf

pdf = pikepdf.Pdf.open(cba_2020_annual_report.pdf)
pdf.save('extractable.pdf')

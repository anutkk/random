# Covid-19 in Israel

The date supplied by the Ministry of Health in Israel is nice, but not organized nicely by city. The data is published day-by-day in PDF files and not centralized anywhere.

I gathered the PDF files for dates XXXX, parsed them and made some simple applets. 

## Applets

Simple HTML files which displays some info on local Covid-19 in Israel (see below for the scripts which created them):

- A 

## Excel data

The parsed data as Excel files is in the folder `parsed_data` (see below for the scripts which created the files):

- byday.xlsx - every PDF file is parsed to a different sheet in the file.
- bycity.xlsx - every city on a row with all available data. Each sheet is a different parameter (Confirmed cases, isolations, etc.)

## Jupyter notebooks

The notebook XXX parses data from the PDFs published by the Ministry and 

The notebook "NationalData" simply gets the data from the standard world database by John Hopkins, tries to perform exponential fitting.
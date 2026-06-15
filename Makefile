# Makefile for generating PDF and HTML from LaTeX
# OlneyGI_BusinessPlan.tex

# Variables
MAIN = OlneyGI_BusinessPlan
PDF_OUTPUT = $(MAIN).pdf
HTML_OUTPUT = $(MAIN).html

# Default target
all: pdf html

# PDF generation using pdflatex
pdf: $(PDF_OUTPUT)

$(PDF_OUTPUT): $(MAIN).tex
	pdflatex -interaction=nonstopmode -halt-on-error $(MAIN).tex
	pdflatex -interaction=nonstopmode -halt-on-error $(MAIN).tex

# HTML generation using htlatex
html: $(HTML_OUTPUT)

$(HTML_OUTPUT): $(MAIN).tex
	htlatex $(MAIN).tex "html,fn-in" " -cunihtf -utf8"

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.toc *.out *.bbl *.blg *.fls *.fdb_latexmk *.synctex.gz *.dvi *.4tc *.4ct *.idv *.lg *.tmp *.xref *.css *.png *.svg

# Clean output files
clean-output:
	rm -f $(PDF_OUTPUT) $(HTML_OUTPUT)

# Clean everything
clean-all: clean clean-output

# Installation target for Ubuntu/Debian systems
install:
	@echo "Installing required LaTeX packages..."
	sudo apt-get update
	sudo apt-get install -y texlive-latex-base texlive-latex-extra texlive-fonts-recommended texlive-fonts-extra
	sudo apt-get install -y texlive-latex-recommended texlive-science texlive-extra-utils
	@echo "Installation complete. You can now generate PDF and HTML files."

# Help target
help:
	@echo "Available targets:"
	@echo "  all          - Generate both PDF and HTML (default)"
	@echo "  pdf          - Generate PDF only"
	@echo "  html         - Generate HTML only"
	@echo "  install      - Install required LaTeX packages (Ubuntu/Debian)"
	@echo "  clean        - Remove auxiliary files"
	@echo "  clean-output - Remove output files (PDF, HTML)"
	@echo "  clean-all    - Remove all generated files"
	@echo "  help         - Show this help message"

.PHONY: all pdf html clean clean-output clean-all help
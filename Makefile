# Find all Python scripts.
PYSCRIPTS = $(shell find . -name '*.py')

# Execute all other targets.
all: latex
	open main.pdf

# Compile Latex.
latex: figures
	latexmk -dvi- -xelatex main.tex

# Compile figures written in Python.
figures: figures/*.py
	python3 $(PYSCRIPTS)

# Clean target.
clean:
	latexmk -c

# Help target.
help:
	@echo "Makefile targets:"
	@echo "all - executes all other targets."
	@echo "latex - use latexmk for Latex compilation."
	@echo "figures - compile figures written in Python."
	@echo "clean - clean all regeneratable files."

# TODO: add .PHONY target
# http://www.linuxdevcenter.com/pub/a/linux/2002/01/31/make_intro.html?page=2

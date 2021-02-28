# --------------------------------------------------------------------
# ALL FILES
#
.PHONY: all clean clean-web
all:
	make all -C images/kicad
	make all -C images/libreoffice
	make all -C images/thumbs
	python questionary.py

clean-web:
	rm -f docs/*.json
	rm -f docs/es_*.html
	rm -f docs/en_*.html
	rm -f docs/gal_*.html

clean:
	rm -f docs/images/*
	rm -f docs/*.json
	rm -f docs/es_*.html
	rm -f docs/en_*.html
	rm -f docs/gal_*.html
	rm -f build/*.xml
	rm -f build/*.csv
	rm -f build/*.docx
	rm -f images/thumbs/*.png
	rm -f images/thumbs/*.jpg

# --------------------------------------------------------------------
# ALL FILES
#
.PHONY: all clean clean-web

all:
	make all -C images/kicad
	make all -C images/libreoffice
	make all -C images/thumbs
	cd multichoice; python _multichoice.py
	cd multiquestion; python _multiquestion.py

clean-web:
	rm -f docs/*.json
	rm -f docs/es_*.html
	rm -f docs/en_*.html
	rm -f docs/gal_*.html

clean-all:
	rm -f docs/images/*
	rm -f docs/*.json
	rm -f docs/es_*.html
	rm -f docs/en_*.html
	rm -f docs/gal_*.html
	rm -f multichoice/build/*.xml
	rm -f multichoice/build/*.csv
	rm -f multichoice/build/*.docx
	rm -f images/thumbs/*.png
	rm -f images/thumbs/*.jpg

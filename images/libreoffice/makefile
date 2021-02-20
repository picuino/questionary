# HELP
#   object: dependencies
#   $@ object
#   $^ dependencies
#   $< first element of dependencies list

IMGDIR=..

PDFTOPNG=pdftopng -gray -r 600 -aa yes -aaVector yes -freetype yes
OPTIPNG=optipng -quiet -o 6
CONVERT=convert
CONVERT_OPT=-transparent White
MOGRIFY=mogrify
ZIP=7z a
PYTHON=python


define crop_image
	$(eval geometry = $(shell python -c "import sys; (x, y, dx, dy)=eval(sys.argv[1]); \
	print('%dx%d+%d+%d'%(dx+20, dy+20, x-10, y-10))" $(1)))
	$(CONVERT) $(3) -crop $(geometry) +repage \
		$(CONVERT_OPT) $(IMGDIR)/$(IMAGES_BASENAME)-$(strip $(2)).png
	$(OPTIPNG) $(IMGDIR)/$(IMAGES_BASENAME)-$(strip $(2)).png
endef


# --------------------------------------------------------------------
# electric-circuits pages
#

electric-table-logic.png: electric-table-logic.pdf
	$(PDFTOPNG) $< $(basename $<)
	mv $(basename $<)-000001.png  $(basename $<).png
	$(MOGRIFY) -posterize 16 $(basename $<).png
	$(OPTIPNG) $(basename $<).png


IMAGES_BASENAME=electric-table
IMAGES_NAMES=$(foreach image, \
	or nor and nand xor xnor not tricky \
	, $(IMAGES_BASENAME)-$(image).png)
IMAGES_DIRNAMES=$(foreach image, $(IMAGES_NAMES),$(IMGDIR)/$(image))

$(IMAGES_DIRNAMES): electric-table-logic.png
	echo $(IMAGES_NAMES)
	$(call crop_image, "(466,   513, 720, 719)", or, electric-table-logic.png)
	$(call crop_image, "(1883,  513, 720, 719)", nor, electric-table-logic.png)
	$(call crop_image, "(466,  1361, 720, 719)", and, electric-table-logic.png)
	$(call crop_image, "(1883, 1361, 720, 719)", nand, electric-table-logic.png)
	$(call crop_image, "(466,  2209, 720, 719)", xor, electric-table-logic.png)
	$(call crop_image, "(1883, 2209, 720, 719)", xnor, electric-table-logic.png)
	$(call crop_image, "(466,  3057, 950-466, 3496-3060)", not, electric-table-logic.png)
	$(call crop_image, "(1883, 3057, 720, 719)", tricky, electric-table-logic.png)


.PHONY: all  clean

all: \
	$(IMAGES_DIRNAMES) \
	electric-table-logic.png \

clean:
	rm -f $(IMAGES_DIRNAMES)
	rm -f electric-table-logic.png

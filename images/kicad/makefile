# HELP
#   object: dependencies
#   $@ object
#   $^ dependencies
#   $< first element of dependencies list

IMGDIR=..


LIBS=$(wildcard _CIRCUITS_lib/*)

PDFTOPNG=pdftopng -gray -r 600 -aa yes -aaVector yes -freetype yes
OPTIPNG=optipng -quiet -o 6
CONVERT=convert
CONVERT_OPT=-transparent White
MOGRIFY=mogrify
ZIP=7z a
PYTHON=python


# --------------------------------------------------------------------
# Macros
#
define crop_image
	$(eval geometry = $(shell python -c "import sys; (x,y,dx,dy)=eval(sys.argv[1]); \
	print('%dx%d+%d+%d'%(dx, dy, 125+(2487+7-124)*(x-1), 125+(1243+6-124)*(y-1)))" $(1)))
	$(CONVERT) $(3) -crop $(geometry) +repage \
		$(CONVERT_OPT) $(IMGDIR)/$(strip $(2)).png
	$(OPTIPNG) $(IMGDIR)/$(strip $(2)).png
endef


# --------------------------------------------------------------------
# electric-circuits
#
electric-circuits-p1.png electric-circuits-p2.png electric-circuits-p3.png: electric-circuits.pdf
	$(PDFTOPNG) $< $(basename $<)
	mv $(basename $<)-000001.png  $(basename $<)-p1.png
	mv $(basename $<)-000002.png  $(basename $<)-p2.png
	mv $(basename $<)-000003.png  $(basename $<)-p3.png
	$(MOGRIFY) -posterize 16 $(basename $<)-p1.png
	$(MOGRIFY) -posterize 16 $(basename $<)-p2.png
	$(MOGRIFY) -posterize 16 $(basename $<)-p3.png


ELECTRIC_CIRCUITS_NAMES=$(foreach image, \
	01 02 03 04 05 06 07 08 09 10 11 12 \
	21 22 23 24 25 26 27 28 29 30 31 32 \
	41 42 43 44 45 46 47 48 49 50 52 \
	, electric-circuit-$(image).png) \
	electric-simbolo-resistencia2.png

ELECTRIC_CIRCUITS_DIRNAMES=$(foreach image, $(ELECTRIC_CIRCUITS_NAMES),$(IMGDIR)/$(image))

$(ELECTRIC_CIRCUITS_DIRNAMES): electric-circuits-p1.png electric-circuits-p2.png electric-circuits-p3.png
	$(call crop_image, "(1, 1, 2360, 1116)", electric-circuit-01, electric-circuits-p1.png)
	$(call crop_image, "(1, 2, 2360, 1116)", electric-circuit-02, electric-circuits-p1.png)
	$(call crop_image, "(1, 3, 2360, 1116)", electric-circuit-03, electric-circuits-p1.png)
	$(call crop_image, "(1, 4, 2360, 1116)", electric-circuit-04, electric-circuits-p1.png)
	$(call crop_image, "(1, 5, 2360, 1116)", electric-circuit-05, electric-circuits-p1.png)
	$(call crop_image, "(1, 6, 2360, 1116)", electric-circuit-06, electric-circuits-p1.png)
	$(call crop_image, "(2, 1, 2360, 1116)", electric-circuit-07, electric-circuits-p1.png)
	$(call crop_image, "(2, 2, 2360, 1116)", electric-circuit-08, electric-circuits-p1.png)
	$(call crop_image, "(2, 3, 2360, 1116)", electric-circuit-09, electric-circuits-p1.png)
	$(call crop_image, "(2, 4, 2360, 1116)", electric-circuit-10, electric-circuits-p1.png)
	$(call crop_image, "(2, 5, 2360, 1116)", electric-circuit-11, electric-circuits-p1.png)
	$(call crop_image, "(2, 6, 2360, 1116)", electric-circuit-12, electric-circuits-p1.png)

	$(call crop_image, "(1, 1, 2360, 1116)", electric-circuit-21, electric-circuits-p2.png)
	$(call crop_image, "(1, 2, 2360, 1116)", electric-circuit-22, electric-circuits-p2.png)
	$(call crop_image, "(1, 3, 2360, 1116)", electric-circuit-23, electric-circuits-p2.png)
	$(call crop_image, "(1, 4, 2360, 1116)", electric-circuit-24, electric-circuits-p2.png)
	$(call crop_image, "(1, 5, 2360, 1116)", electric-circuit-25, electric-circuits-p2.png)
	$(call crop_image, "(1, 6, 2360, 1116)", electric-circuit-26, electric-circuits-p2.png)
	$(call crop_image, "(2, 1, 2360, 1116)", electric-circuit-27, electric-circuits-p2.png)
	$(call crop_image, "(2, 2, 2360, 1116)", electric-circuit-28, electric-circuits-p2.png)
	$(call crop_image, "(2, 3, 2360, 1116)", electric-circuit-29, electric-circuits-p2.png)
	$(call crop_image, "(2, 4, 2360, 1116)", electric-circuit-30, electric-circuits-p2.png)
	$(call crop_image, "(2, 5, 2360, 1116)", electric-circuit-31, electric-circuits-p2.png)
	$(call crop_image, "(2, 6, 2360, 1116)", electric-circuit-32, electric-circuits-p2.png)

	$(call crop_image, "(1, 1, 2360, 1116)", electric-circuit-41, electric-circuits-p3.png)
	$(call crop_image, "(1, 2, 2360, 1116)", electric-circuit-42, electric-circuits-p3.png)
	$(call crop_image, "(1, 3, 2360, 1116)", electric-circuit-43, electric-circuits-p3.png)
	$(call crop_image, "(1, 4, 2360, 1116)", electric-circuit-44, electric-circuits-p3.png)
	$(call crop_image, "(1, 5, 2360, 1116)", electric-circuit-45, electric-circuits-p3.png)
	$(call crop_image, "(1, 6, 2360, 1116)", electric-circuit-46, electric-circuits-p3.png)
	$(call crop_image, "(2, 1, 2360, 1116)", electric-circuit-47, electric-circuits-p3.png)
	$(call crop_image, "(2, 2, 2360, 1116)", electric-circuit-48, electric-circuits-p3.png)
	$(call crop_image, "(2, 3, 2360, 1116)", electric-circuit-49, electric-circuits-p3.png)
	$(call crop_image, "(2, 4, 2360, 1116)", electric-circuit-50, electric-circuits-p3.png)
	$(call crop_image, "(2, 5,  526,  346)", electric-simbolo-resistencia2, electric-circuits-p3.png)
	$(call crop_image, "(2, 6, 2360, 1116)", electric-circuit-52, electric-circuits-p3.png)


.PHONY: all-electric-circuits  clean-electric-circuits
all-electric-circuits: \
	electric-circuits-p1.png \
	electric-circuits-p2.png \
	electric-circuits-p3.png \
	$(ELECTRIC_CIRCUITS_DIRNAMES) \

clean-electric-circuits:
	rm -f electric-circuits-p1.png
	rm -f electric-circuits-p2.png
	rm -f electric-circuits-p3.png
	rm -f $(ELECTRIC_CIRCUITS_DIRNAMES)


# --------------------------------------------------------------------
# electric-digital
#
electric-digital-p1.png: electric-digital.pdf
	$(PDFTOPNG) $< $(basename $<)
	mv $(basename $<)-000001.png  $(basename $<)-p1.png
	$(MOGRIFY) -posterize 16 $(basename $<)-p1.png


ELECTRIC_DIGITAL_BASENAME=electric-digital
ELECTRIC_DIGITAL_NAMES=$(foreach image, \
	01 02 03 04 05 06 07 08 09 10 11 12 \
	, electric-digital-$(image).png)
ELECTRIC_DIGITAL_DIRNAMES=$(foreach image, $(ELECTRIC_DIGITAL_NAMES),$(IMGDIR)/$(image))

$(ELECTRIC_DIGITAL_DIRNAMES): electric-digital-p1.png
	$(call crop_image, "(1, 1, 2360, 1116)", electric-digital-01, electric-digital-p1.png)
	$(call crop_image, "(1, 2, 2360, 1116)", electric-digital-02, electric-digital-p1.png)
	$(call crop_image, "(1, 3, 2360, 1116)", electric-digital-03, electric-digital-p1.png)
	$(call crop_image, "(1, 4, 2360, 1116)", electric-digital-04, electric-digital-p1.png)
	$(call crop_image, "(1, 5, 2360, 1116)", electric-digital-05, electric-digital-p1.png)
	$(call crop_image, "(1, 6, 2360, 1116)", electric-digital-06, electric-digital-p1.png)
	$(call crop_image, "(2, 1, 2360, 1116)", electric-digital-07, electric-digital-p1.png)
	$(call crop_image, "(2, 2, 2360, 1116)", electric-digital-08, electric-digital-p1.png)
	$(call crop_image, "(2, 3, 2360, 1116)", electric-digital-09, electric-digital-p1.png)
	$(call crop_image, "(2, 4, 2360, 1116)", electric-digital-10, electric-digital-p1.png)
	$(call crop_image, "(2, 5, 2360, 1116)", electric-digital-11, electric-digital-p1.png)
	$(call crop_image, "(2, 6, 2360, 1116)", electric-digital-12, electric-digital-p1.png)
   
.PHONY: all-electric-digital  clean-electric-digital
all-electric-digital: \
	electric-digital-p1.png \
	$(ELECTRIC_DIGITAL_DIRNAMES) \

clean-electric-digital:
	rm -f electric-digital-p1.png
	rm -f $(ELECTRIC_DIGITAL_DIRNAMES)


# --------------------------------------------------------------------
# make all and clean
#
.PHONY: all clean
all: \
	all-electric-circuits \
	all-electric-digital \

clean: \
	clean-electric-circuits \
	clean-electric-digital \

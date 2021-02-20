IMAGES_DIR=..

CONVERT=convert
OPTIPNG=optipng -quiet -o 6

THUMBS_SIZE=240x180\>

# --------------------------------------------------------------------
# THUMBNAILS
#
THUMBS=$(foreach f, $(wildcard $(IMAGES_DIR)/*.png) $(wildcard $(IMAGES_DIR)/*.jpg), $(notdir $f))

%.png: $(IMAGES_DIR)/%.png
	echo $@
	$(CONVERT) $<  -strip -resize $(THUMBS_SIZE) $@
	$(OPTIPNG) $@

%.jpg: $(IMAGES_DIR)/%.jpg
	echo $@
	$(CONVERT) $<  -strip -resize $(THUMBS_SIZE) $@


# --------------------------------------------------------------------
# ALL FILES
#
.PHONY: all clean
all: \
	$(THUMBS)

clean:
	rm -f $(THUMBS)

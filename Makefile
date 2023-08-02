SOURCES := $(shell find -name '*.jpg' ! -name '*_vl*')
OBJECTS := $(SOURCES:%.jpg=%_vl.jpg)
SOURCESC := $(shell find -name '*.JPG' ! -name '*_vl*')
OBJECTSC := $(SOURCESC:%.JPG=%_vl.JPG)
FONT=FreeSans.ttf
COPYRIGHT=Copyright John Doe

%_vl.jpg: %.jpg
	python watermark.py $< $(COPYRIGHT) $(FONT)
%_vl.JPG: %.JPG
	python watermark.py $< $(COPYRIGHT) $(FONT)

all: $(OBJECTS) $(OBJECTSC)

clean:
	rm -f $(OBJECTS) $(OBJECTS_C)


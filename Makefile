CHAPTER_DIR := _chapters
TITLE := Learn_Julia_the_Hard_Way

FRONT_MATTER_FILES = title.txt CONTRIBUTORS.md LICENSE.md
CHAPTER_FILES = $(shell find ${CHAPTER_DIR} -type f -name '*.md')

all : pdf epub html

pdf : $(TITLE).pdf
epub : $(TITLE).epub
html : $(TITLE).html

$(TITLE).pdf : $(FRONT_MATTER_FILES) $(CHAPTER_FILES)
	pandoc --latex-engine=xelatex --toc --mathjax -s  --chapters -S -o $(TITLE).pdf $(FRONT_MATTER_FILES) $(CHAPTER_FILES)

$(TITLE).epub : $(FRONT_MATTER_FILES) $(CHAPTER_FILES)
	pandoc --mathjax --toc -s  --chapters -S  -o $(TITLE).epub $(FRONT_MATTER_FILES) $(CHAPTER_FILES)

$(TITLE).html : $(FRONT_MATTER_FILES) $(CHAPTER_FILES)
	pandoc --mathjax --toc -s --chapters -S -o $(TITLE).html $(FRONT_MATTER_FILES) $(CHAPTER_FILES)

clean ::
	rm -rf $(TITLE).pdf $(TITLE).epub $(TITLE).html

.PHONY : all clean pdf epub html

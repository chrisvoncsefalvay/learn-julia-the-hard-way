CHAPTER_DIR := _chapters
TITLE := Learn_Julia_the_Hard_Way

FRONT_MATTER_FILES = title.txt README.md CONTRIBUTORS.md LICENSE.md
CHAPTER_FILES = $(shell find ${CHAPTER_DIR} -type f -name '*.md')

all : html pdf

pdf : book.pdf
html : _book/index.html

_book/index.html : $(FRONT_MATTER_FILES) $(CHAPTER_FILES)
	gitbook build

book.pdf : $(FRONT_MATTER_FILES) $(CHAPTER_FILES)
	gitbook pdf

clean ::
	rm -rf book.pdf _book

.PHONY : all clean pdf html

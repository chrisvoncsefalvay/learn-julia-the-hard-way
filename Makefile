FINAL=learn-julia-the-hard-way
SOURCE=book
WEBSITE=WHERE_YOUR_SITE_GOES

book:
	dexy

view: $(FINAL).pdf
	evince $(FINAL).pdf

sync: book
	rsync -avz --delete --exclude "scripts/"* --exclude "${FINAL}.*" output/ $(WEBSITE)/book

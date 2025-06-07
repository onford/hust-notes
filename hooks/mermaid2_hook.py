import logging
import mkdocs.plugins

log = logging.getLogger('mkdocs')

def on_post_page(output_content,**kwargs):
	return output_content.replace("<!DOCTYPE doctype>", "<!DOCTYPE html>").replace("<!DOCTYPE doctype html>","<!DOCTYPE html>")
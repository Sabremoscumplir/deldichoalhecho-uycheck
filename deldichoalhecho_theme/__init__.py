from django.conf import settings
import os,sys
# Store current working directory
pwd = os.path.dirname(__file__)

PROMISES_THEMES = (
	#'100dias',
    'edicion2015',
	'incendiovalpo',
	'terremotonorte',
	'test',
	'uycheck'
	)

for theme in PROMISES_THEMES:
	static_dir = os.path.join(pwd, theme, 'static')
	settings.STATICFILES_DIRS += (static_dir ,)

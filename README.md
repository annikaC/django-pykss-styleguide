django-pykss-styleguide
======

This is a starting point for your own internal pykss-based styleguide. 
Using pykss's auto generated documentation, a structured index is created with pages for each section.

Also included is a styleguideblock template. 

Copy, fork, override, have fun!

Please refer to the [KSS syntax](http://warpspire.com/kss/) for getting this to work with your CSS.

Requirements: 
pykss

Add these lines to settings.py:

Add 'pykss' and 'django-pykss-styleguide' to INSTALLED_APPS

	PYKSS_DIRS = [os.path.join(STATIC_ROOT, 'django-pykss-styleguide', 'css')]

And make sure to add to your patterns in urls.py too:

 	url(r'^styles/', include('django-pykss-styleguide.urls', namespace='django-pykss-styleguide')),
  
Originally developed for Open Utility's internal styleguide.

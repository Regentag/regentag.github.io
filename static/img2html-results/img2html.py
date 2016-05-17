## Image to HTML

import base64
import sys, os

if len(sys.argv) != 2:
  print( "wrong args." )
  exit()

img = sys.argv[1]
name,ext = os.path.splitext(img)
html = name + ".html"

if ext != ".jpg" and ext != ".png":
  print( "unsupported format", ext )
  exit()

i = open( img, "rb" )
o = open( html, "w" )

data = i.read()
enc = base64.b64encode( data ).decode( "utf-8" )

o.write( "<html><head><title>{}</title></head><body>".format(img) )
o.write( "<img src='data:image/{};base64,{}' />".format(ext[1:],enc) )
o.write( "</body></html>" )

i.close()
o.close()


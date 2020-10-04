#!/usr/bin/env python3

import sys, os, subprocess
from xml.sax.saxutils import escape
from PIL import Image
import subprocess

image_path        = sys.argv[1]
image_ext         = image_path.split('.')[-1]
image_path_prefix = image_path[0:-(len(image_ext)+1)]
image             = Image.open(image_path)
svg_path          = '%s.svg' % image_path_prefix

svg_template = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   xmlns:dc="http://purl.org/dc/elements/1.1/"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:xlink="http://www.w3.org/1999/xlink"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   width="%(image_width)s"
   height="%(image_height)s"
   viewBox="0 0 %(image_width)s %(image_height)s"
   id="svg2"
   version="1.1">
  <sodipodi:namedview inkscape:window-maximized="1" />
  <g inkscape:export-filename="%(image_path_prefix)s_export.png"
     inkscape:export-xdpi="90"
     inkscape:export-ydpi="90">
    <image
       sodipodi:absref="%(image_path)s"
       xlink:href="%(image_path)s"
       width="%(image_width)s"
       height="%(image_height)s"
       preserveAspectRatio="none"
       x="0"
       y="0" />
  </g>
</svg>"""

if not os.path.exists(svg_path):

    svg = svg_template % {'image_path':        escape(image_path),
                          'image_path_prefix': image_path_prefix,
                          'image_width':       image.size[0],
                          'image_height':      image.size[1]}

    open(svg_path, 'w').write(svg)

    subprocess.run(["inkscape", svg_path])

else: print('%s already exists.' % svg_path)
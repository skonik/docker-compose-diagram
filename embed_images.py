import base64
import mimetypes
import os
import sys
from xml.dom import minidom


def embed_images(svg_file, svg_file_out=None):
    doc = minidom.parse(svg_file)
    images = doc.getElementsByTagName("image")
    for img in images:
        if img.hasAttribute("xlink:href"):
            resource_file = img.getAttribute("xlink:href")
            if os.path.isfile(resource_file):
                mime_type = mimetypes.guess_type(resource_file)[0]
                with open(resource_file, "rb") as image_file:
                    encoded = base64.b64encode(image_file.read()).decode()
                    attr = f"data:{mime_type};base64," + encoded
                    img.setAttribute("xlink:href", attr)
    if not svg_file_out:
        p, ext = os.path.splitext(svg_file)
        svg_file_out = p + "_out" + ext
    with open(svg_file_out, "w") as f:
        f.write(doc.toxml())


if __name__ == "__main__":
    svg_file = sys.argv[1] if len(sys.argv) == 2 else "docker-compose.svg"
    embed_images(
        svg_file
    )  # outputs my_diagram_out.svg with base64 encoded data URLs for the images

"""
Write a program that transofrms RGB tryplet to HTML format.
"""
def rgb_to_html(r, g, b):
    rgb = [r, g, b]
    for i in rgb:
        if i > 255 or i < 0:
            raise ValueError("Wrong format")
    return '#{:02x}{:02x}{:02x}'.format(r, g, b).upper()

print(rgb_to_html(37, 37, 37))
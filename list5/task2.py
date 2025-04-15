"""
Write a program that transorms color from HTML format to RGB tryplet.
"""
def html_to_rgb(html):
    if len(html) == 7:
        rgb = []
        for i in (1, 3, 5):
            liczba = int(html[i:i + 2], 16)
            rgb.append(liczba)
        return rgb
    else:
        raise ValueError('Wrong format')

print(html_to_rgb('#252525'))
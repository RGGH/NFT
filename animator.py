from apng import APNG

files = [
    ("output/merged1.png", 100),
    ("output/merged2.png", 200),
    ("output/merged3.png", 300)
]

im = APNG()
for file, delay in files:
    im.append_file(file, delay=delay)
im.save("animated_result.png")
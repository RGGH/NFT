from apng import APNG

files = [
  ("1.jpg", 100),
  ("2.jpg", 200),
  ("3.jpg", 300)
]

im = APNG()
for file, delay in files:
  im.append_file(file, delay=delay)
im.save("result.png")

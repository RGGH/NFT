from PIL import Image
import random
import cv2


lsid = []

for i in range(1,1100):

    sk = random.randint(1,5)
    ha = random.randint(1,5)
    em = random.randint(1,5)

    if (f"{sk}{ha}{em}") not in lsid:

        
        background = Image.open(f"/home/rag/Documents/NFT_1/NFT/Skin/skin_{sk}.png")
        hair = Image.open(f"/home/rag/Documents/NFT_1/NFT/Hair/hair_{ha}.png")
        emotion = Image.open(f"/home/rag/Documents/NFT_1/NFT/Emotion/emotion_{em}.png")
        spliff = Image.open(f"/home/rag/Documents/NFT_1/NFT/Spliff/spliff_1.png")

        background.paste(hair, (0, 0), hair)
        background.paste(emotion, (0, 0), emotion)
        if i % 2 == 0:
            background.paste(spliff, (0, 0), spliff)

        # save to PNG
        background.save(f"./output/{i}.png")

        # Loading .png image
        png_img = cv2.imread(f"./output/{i}.png")
        
        # converting to jpg file
        #saving the jpg file to "ouput2"
        cv2.imwrite(f"./output2/{i}.jpg", png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

        
        lsid.append(f"{sk}{ha}{em}")
    else:
        print("Dupe\n")

print(len(lsid))


  

from os import remove

# remove("image1.jpg")
# remove("image2.jpg")
# remove("image3.jpg")


for i in range(3):
    remove(f"photos/{i}.jpg")
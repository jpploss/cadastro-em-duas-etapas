from deepface import DeepFace

result = DeepFace.verify(img1_path = "ney1.jpg", img2_path = "ney2.jpg")
print(result['verified'], result)

result = DeepFace.verify(img1_path = "cr2.jpg", img2_path = "cr.jpeg")
print(result['verified'], result)

result = DeepFace.verify(img1_path = "cr2.jpg", img2_path = "ney1.jpg")
print(result['verified'], result)

# result = DeepFace.verify(img1_path = "img1.png", img2_path = "img11.png")
# print(result['verified'])
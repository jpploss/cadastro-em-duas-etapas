from deepface import DeepFace

result = DeepFace.verify(img1_path = "img1.png", img2_path = "img2.png")
print(result['verified'])

result = DeepFace.verify(img1_path = "img11.png", img2_path = "img12.png")
print(result['verified'])

result = DeepFace.verify(img1_path = "img1.png", img2_path = "img11.png")
print(result['verified'])
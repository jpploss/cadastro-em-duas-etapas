from deepface import DeepFace

result = DeepFace.verify(img1_path = "test.png", img2_path = "test2.png")
print(result['verified'])
result = DeepFace.verify(img1_path = "h1.png", img2_path = "h2.png")
print(result['verified'])
result = DeepFace.verify(img1_path = "h1.png", img2_path = "test.png")
print(result['verified'])
from ultralytics import YOLO

model = YOLO('best.pt')

print("Fotoğraf inceleniyor...")

sonuclar = model.predict(source='test2.jpg', imgsz=1280, conf=0.50, save=True)

print("İşlem tamam! Çıktıyı 'runs/predict' klasöründen alabilirsiniz.")
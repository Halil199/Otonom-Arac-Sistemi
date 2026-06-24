# Otonom Araç Çevresel Algı Sistemi (YOLOv8-Seg)

Bu proje, otonom sürüş sistemleri için geliştirilmiş "Çoklu Görev Öğrenimi (Multi-Task Learning)" tabanlı bir yapay zeka modelidir. 

## 🚀 Projenin Yetenekleri
* **Object Detection:** Trafikteki araçları (vehicle) Bounding Box ile tespit eder.
* **Instance Segmentation:** Sürülebilir asfaltı (drivable_area) piksel hassasiyetinde maskeler.
* **Decoupled Head Mimarisi:** Sistem, donanım yorgunluğunu önlemek için sınıflandırma ve koordinat regresyon işlemlerini ayırarak gerçek zamanlı (Real-Time) yüksek FPS değerlerine ulaşacak şekilde tasarlanmıştır.

## 🧠 Kurulum ve Canlı Test (Inference)
Projenin ağırlık dosyası (`best.pt`) depo içerisindedir. Sistemin nasıl çalıştığını görmek için aşağıdaki komutu çalıştırmanız yeterlidir:

1. Gerekli kütüphaneyi kurun:
`pip install ultralytics`

2. Test kodunu çalıştırın:
`python final_demo.py`

*Not: Çıktı sonuçları otomatik olarak `runs/segment/predict` klasörüne kaydedilecektir.*

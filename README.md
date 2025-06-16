# 🚗 Car Damage Detection using ResNet50

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Torch](https://img.shields.io/badge/PyTorch-ResNet50-red)](https://pytorch.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-orange)](https://streamlit.io/)

A deep learning project that classifies car damage from images into six categories using a fine-tuned **ResNet50** model. Built with **PyTorch**, **Streamlit**, and optionally **FastAPI** for backend APIs.
![Screenshot](screenshot-1.png)
---

## App Link
https://cardamagedetectionresnet50.streamlit.app/

## 📂 Project Structure

```
Car_Damage_Detection_Resnet50/
├── fastapi-server/
│   └── model/
│       └── saved_model.pth
├── streamlit-app/
│   ├── app.py
│   ├── model_helper.py
│   └── model/
│       └── saved_model.pth  ✅ (model used for prediction)
```

---

## 🔍 Features

- 🔧 Fine-tuned ResNet50 model on car damage images
- 🖼️ Detects:
  - Front Breakage / Crushed / Normal
  - Rear Breakage / Crushed / Normal
- 🚀 Deployable via Streamlit
- 🔁 Easily extendable for API use with FastAPI

---

## 📦 Installation

Clone the repo and install the required packages:

```bash
git clone https://github.com/HruthikExploiter/Car_Damage_Detection_Resnet50.git
cd Car_Damage_Detection_Resnet50/streamlit-app
pip install -r ../requirements.txt
```

---

## 🖥️ Run the App

```bash
streamlit run app.py
```

Then upload a car image to get the damage type prediction.

---

## 🧠 Model Details

- Backbone: `ResNet50` (`weights='DEFAULT'`)
- Modified final layer:
  ```python
  nn.Sequential(
      nn.Dropout(0.2),
      nn.Linear(resnet.fc.in_features, 6)
  )
  ```
- Trained on a labeled dataset of car images (classified into 6 categories)

---

## ⚠️ Troubleshooting

- `FileNotFoundError`: Make sure `saved_model.pth` is inside `streamlit-app/model/`.
- `Streamlit not found`: Run `pip install streamlit`.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

Created by **[Hruthik GAjjala](https://github.com/HruthikExploiter)** — feel free to reach out!

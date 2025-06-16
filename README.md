# 🚗 Car Damage Detection using ResNet50

This project is an AI-based system for detecting car damage types using a fine-tuned **ResNet50** model. The system classifies car images into six categories like "Front Breakage", "Rear Normal", etc. It is deployed with **Streamlit** for the frontend and optionally uses **FastAPI** for serving predictions via API.

---

## 📂 Project Structure

```
Car_Damage_Detection_Resnet50/
├── fastapi-server/
│   └── model/
│       └── saved_model.pth             # Trained ResNet50 model (optional FastAPI usage)
├── streamlit-app/
│   ├── app.py                          # Streamlit frontend
│   ├── model_helper.py                 # Core model logic
│   └── model/
│       └── saved_model.pth             # ✅ Used model for prediction
```

---

## 🚀 Features

- 🔍 Classifies car images into:
  - Front Breakage
  - Front Crushed
  - Front Normal
  - Rear Breakage
  - Rear Crushed
  - Rear Normal
- 🧠 Built on **ResNet50** with custom classification head
- ⚡ Live prediction using **Streamlit UI**
- ✅ Pre-trained model included for instant use

---

## 📦 Requirements

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🖼️ Usage

### 📍 Run Streamlit App

```bash
cd streamlit-app
streamlit run app.py
```

### 📤 Upload Image

- The UI allows uploading a car image.
- It returns the predicted class instantly using the loaded ResNet50 model.

---

## 🧠 Model Details

- Backbone: `ResNet50` (weights='DEFAULT')
- Frozen layers: All except `layer4` and final `fc`
- Custom head:
  ```python
  nn.Sequential(
      nn.Dropout(0.2),
      nn.Linear(in_features, 6)
  )
  ```

---

## ⚙️ Prediction Logic

The prediction is handled inside `model_helper.py` and loads the model lazily:

```python
trained_model = car_damage_detection()
trained_model.load_state_dict(torch.load('model/saved_model.pth'))
trained_model.eval()
```

---

## 🛠️ Troubleshooting

- **Model Not Found**: Ensure `saved_model.pth` is placed in `streamlit-app/model/`.
- **Streamlit Error**: Run the command from inside `streamlit-app` directory.

---

## 📬 Contact

For any questions or contributions, feel free to reach out or raise an issue.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

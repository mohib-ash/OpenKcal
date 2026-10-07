# KcalCore 🍏

**KcalCore** is a modern, lightweight, and sleek precision calorie and macro calculation engine built using [Flet](https://flet.dev/) and Python. It started as a fun side project to explore what Flet can do, and turned into an awesome way to learn cross-platform UI development! It features a stunning dark-mode UI designed for quick, precise nutritional estimation.


<div align="center">
  <video src="https://raw.githubusercontent.com/mohib-ash/OpenKcal/main/usage.mp4" width="320" autoplay loop muted playsinline></video>
</div>


---

## 🚀 Features
* **Precision Calculation:** Computes exact calorie density based on per-100g metrics and custom serving sizes.
* **Sleek UI/UX:** Built with polished dark gradients, smooth transitions, and intuitive input validations.
* **Cross-Platform Ready:** Thanks to Flet, this application can run natively on Desktop, Web, and Mobile (Android APK & iOS).

---

## 🛠️ Installation & Setup

1. **Clone or download** this repository.
2. Ensure you have Python installed, then install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```

---

## 📱 Build Your Own APK / iOS App!
Since **KcalCore** is powered by Flet, you can easily package it into a native Android APK or iOS app using Flet's built-in packaging tools (`flet build`). 

Feel free to take this project, rebrand it, or build cool mobile apps out of it for everyday use! If you share your modified version with the general public, a tiny credit somewhere in the app or the repo (like keeping the footer or mentioning the original repo) is always appreciated, but entirely up to you. ✨

---

## ✍️ Customizing Developer Credits
If you want to fork or modify this project and change the developer signature in the UI, locate the footer section in the source code (around the bottom of `main.py`) and update the following block to your own name and links:

```python
ft.Column(
    [
        ft.Text("Developer: Your Name", size=11, color="#475569", italic=True),
        ft.Row(
            [
                ft.TextButton(
                    "GitHub",
                    action=ft.OpenUrl("https://github.com/your-username"),
                ),
                ft.Text("•", color="#334155", size=10),
                ft.TextButton(
                    "LinkedIn",
                    action=ft.OpenUrl("https://www.linkedin.com/in/your-profile/"),
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0
        )
    ],
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    spacing=0
),
```

---


## 📜 License & Usage
**Ez Pz / No Sweat License:** 
Do whatever you want with this code! Fork it, copy it, build APKs, sell it, modify it, or show it off. No strings attached, no legal hoopsm! complete freedom. If you wanna drop a tiny nod to [Mohib Ashfaq](https://github.com/mohib-ash) somewhere, that's cool! 🚀
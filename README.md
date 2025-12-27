# procedural-animation-with-bpy
### Cube to Circle Transition with Camera & Light Movement

This project demonstrates how to create a **procedural animation in Blender using Python (`bpy`)**.
It animates a **red cube transforming into a blue circle (cylinder)** while also animating the **camera and light** to create a cinematic effect.

---

## 🎯 Project Overview

* A **cube** moves upward and disappears
* A **circle (cylinder)** appears and moves diagonally
* A **camera** slowly moves closer for a dynamic view
* A **light** changes position and intensity over time
* Entire animation is created **purely using Python scripting**

---

## 🧠 Concepts Covered

* Blender Python API (`bpy`)
* Object creation and deletion
* Material creation using **Principled BSDF**
* Keyframe animation
* Visibility animation (`hide_viewport`, `hide_render`)
* Camera animation
* Light animation (location + energy)

---

## 🎬 Animation Timeline

| Frame     | Action                            |
| --------- | --------------------------------- |
| 1         | Cube starts moving upward         |
| 100       | Cube reaches top                  |
| 119       | Cube disappears                   |
| 120       | Circle appears                    |
| 120 → 180 | Circle moves diagonally           |
| 1 → 180   | Camera moves closer               |
| 1 → 180   | Light position & intensity change |

---

## 🧩 Scene Elements

### 🔴 Cube

* Color: Red
* Moves upward along Z-axis
* Hidden after frame 119

### 🔵 Circle (Cylinder)

* Color: Blue
* Appears after cube disappears
* Moves from `(0, 0, 5)` → `(5, 0, -5)`

### 📷 Camera

* Animated to move closer to the scene
* Adds cinematic motion
* Set as the active scene camera

### 💡 Light

* Area light
* Changes position and intensity over time
* Creates smooth lighting transition

---

## 🛠 Requirements

* **Blender 3.x or later**
* Basic knowledge of:

  * Python
  * Blender interface
  * Keyframes

---

## ▶️ How to Run the Script

1. Open **Blender**
2. Switch to the **Scripting** workspace
3. Create a new **Text** file
4. Paste the Python script
5. Click **Run Script**
6. Press **Play ▶️** to view the animation

---

## 📂 Project Structure

```text
blender-cube-to-circle/
│── animation.py
│── README.md
```

---


## 📌 Note

* The “circle” is implemented using a **cylinder primitive**
* Visibility is controlled using both:

  * `hide_viewport`
  * `hide_render`





# python_object_detector
A Python object detection app using TensorFlow + OpenCV, packaged in Docker, with CI/CD via GitHub Actions, using a self-hosted runner, and pushing Docker image to a private container registry (e.g., Docker Hub, GitHub Container Registry, or AWS ECR).

# 🧠 Object Detection App (TensorFlow + OpenCV)

This project is a Python-based object detection application built using **TensorFlow** and **OpenCV**. It captures video from a webcam, runs object detection using a pre-trained model, and displays the detected objects in real-time. The project is Dockerized and configured with **GitHub Actions** for automated CI/CD, including support for **self-hosted runners**.

---

## 🚀 Features

- Real-time object detection via webcam
- Pre-trained TensorFlow model (SSD MobileNet or similar)
- Simple OpenCV UI
- Docker support for containerized execution
- GitHub Actions workflow for:
  - Building Docker images
  - Pushing to a private container registry
  - Running on a self-hosted runner

---

## 📁 Project Structure

object-detector/
│
├── app/
│ ├── main.py # App entry point
│ ├── detector.py # TensorFlow object detection logic
│ └── utils.py # Helper functions (optional)
│
├── requirements.txt # Python dependencies
├── Dockerfile # Docker container setup
├── .dockerignore # Docker ignore rules
├── .github/
│ └── workflows/
│ └── build.yml # GitHub Actions workflow
├── runner/ # Self-hosted runner setup (optional)
└── README.md

yaml
Copy code

---

## 🧰 Requirements

- Python 3.8–3.11
- Docker
- GitHub Account
- (Optional) Self-hosted GitHub Actions runner
- Private container registry (Docker Hub, GHCR, AWS ECR, etc.)

---

## ⚙️ Installation (Local)

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/object-detector.git
   cd object-detector
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
python app/main.py
🐳 Run with Docker
bash
Copy code
docker build -t object-detector .
docker run --rm -it object-detector
🔄 GitHub Actions CI/CD
Add these secrets to your GitHub repo:

REGISTRY_USERNAME

REGISTRY_PASSWORD

On each push to main, the workflow will:

Build the Docker image

Log into your registry

Push the image

You can also use a self-hosted runner if needed (setup guide in /runner folder).

📸 Example Output
(Screenshot or video coming soon!)

🧠 Future Enhancements
Add YOLOv8 or custom trained model support

Deploy to cloud (e.g. GCP, AWS Lambda, or Azure)

Stream video to web interface

Add unit tests & coverage reports

# SnapClass - Smart AI Attendance System

An automated classroom attendance system powered by multi-face computer vision and voice biometrics, integrated with Supabase and Streamlit.

## Features
- **Instant Face Recognition**: Scans multi-person classroom photos using 128-d deep neural embeddings with Euclidean distance verification.
- **Voice Biometrics**: Audio recording and speaker verification powered by Resemblyzer and Librosa.
- **Real-time Cloud Sync**: Supabase PostgreSQL database for teacher and student records.
- **Enterprise UI**: Responsive design for mobile, tablet, and desktop devices.

## Tech Stack
- **Frontend**: Streamlit
- **Computer Vision**: dlib, face_recognition_models, scikit-learn
- **Audio Processing**: Resemblyzer, Librosa, PyTorch
- **Backend / Database**: Supabase (PostgreSQL), bcrypt
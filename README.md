# Signbot - Indian Sign Language Recognition System

A real-time sign language recognition system that detects and interprets Indian Sign Language (ISL) gestures using computer vision and machine learning.

## Features

- Real-time hand gesture recognition
- Support for both one-handed and two-handed signs
- Live camera feed with gesture detection
- Chat interface for displaying recognized signs
- Peer-to-peer communication between two computers running the application
- User authentication system
- Dataset creation tools
- Support for numbers (0-9) and alphabets (A-Z)

## Prerequisites

- Python 3.9
- Webcam
- Windows OS (Tested on Windows 10)
- pip (Python package installer)

## Installation

### Setting up Virtual Environment

1. Install virtualenv if you haven't already:
   ```bash
   pip install virtualenv
   ```

2. Create a new virtual environment with Python 3.9:
   ```bash
   python -m virtualenv venv --python=python3.9
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

### Project Setup

1. Clone the repository:   ```bash
   git clone <repository-url>   ```

2. Install the required packages: 
   pip install -r requirements.txt   

### Dependencies

Main dependencies include:
- OpenCV (4.7.0.68)
- MediaPipe (0.10.20)
- TensorFlow (2.18.0)
- NumPy (1.26.4)
- Pillow (11.0.0)
- scikit-learn (1.2.0)
- pandas (2.2.3)

Additional dependencies:
- playsound (1.2.2)
- ttkthemes (3.2.2)
- XlsxWriter (3.2.0)
- imutils (0.5.4)

For a complete list of dependencies, see `requirements.txt`

### System Requirements

- At least 4GB RAM
- Webcam with minimum 720p resolution
- CPU: Intel i3/AMD equivalent or better
- Storage: Minimum 2GB free space

## Project Structure

- `main.py` - Main application entry point with login interface
- `inference_classifier.py` - Real-time sign detection and classification
- `chattt.py` - Chat interface for displaying recognized signs
- `collect_imgs.py` - Tool for collecting training images
- `create_dataset.py` - Creates dataset for one-handed signs
- `create_dataset_twohand.py` - Creates dataset for two-handed signs
- `files/users_info.db` - SQLite database for user authentication

## Usage

1. Run the main application:   ```bash
   python main.py   ```

2. Login or create a new user account

3. Main features:
   - **Create Sign**: Capture new sign language gestures
   - **Create DS One Hand**: Create dataset for one-handed signs
   - **Create DS Two Hand**: Create dataset for two-handed signs
   - **Predict Signs**: Start real-time sign recognition

## Network Communication

The application supports real-time communication between two computers:

1. Both computers must be running the application
2. One computer acts as the server (automatically configured)
3. The other computer connects as a client
4. Sign language gestures detected on one computer are transmitted to the other
5. Default ports used:
   - Server: 3050
   - Client: 4050

Note: Both computers must be on the same network or have proper network connectivity between them.

## Sign Recognition Support

### One-Handed Signs
- Numbers: 0-9
- Letters: C, I, L, O, U, V

### Two-Handed Signs
- Letters: A, B, D, E, F, G, H, J, K, M, N, P, Q, R, S, T, W, X, Y, Z
- Space character

## Development Team

- Ruben Singh Sodhi
- Anubhav Gupta

## File Descriptions

- `main.py`: Main GUI application with login system
- `inference_classifier.py`: Contains the sign recognition model and real-time processing
- `chattt.py`: Chat interface implementation
- `collect_imgs.py`: Tool for collecting training images
- `create_dataset.py`: Processes collected images for one-handed signs
- `create_dataset_twohand.py`: Processes collected images for two-handed signs
- `out.txt`: Temporary file for storing recognized signs

## Models

The system uses two trained models:
- `model1.p`: For one-handed sign recognition
- `model2.p`: For two-handed sign recognition

## Required Files

- `files/gif2.gif`: Animation file for the GUI
- `files/users_info.db`: User authentication database

## Troubleshooting

1. Camera Issues:
   - Ensure your webcam is properly connected
   - Check if other applications are using the camera

2. Recognition Issues:
   - Ensure proper lighting conditions
   - Keep hands within the marked rectangle
   - Maintain appropriate distance from camera

3. Login Issues:
   - Check if users_info.db exists in the files directory
   - Try creating a new user account

## Notes

- The system requires good lighting conditions for optimal recognition
- Hand gestures should be performed within the marked rectangle
- For best results, maintain a clean background

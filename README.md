# Signbot - Indian Sign Language Recognition System

![image](https://github.com/user-attachments/assets/92886a65-4d56-4cb4-850d-85050068040f)


A real-time sign language recognition system that detects and interprets Indian Sign Language (ISL) gestures using computer vision and machine learning.

![image](https://github.com/user-attachments/assets/18b8b214-85fd-4ec5-af0d-afa5d659d781)


## Features
![image](https://github.com/user-attachments/assets/ee852479-0efb-4fc0-bf5a-b0e4e94731ad)

- Real-time hand gesture recognition
- Support for both one-handed and two-handed signs
- Live camera feed with gesture detection

![image](https://github.com/user-attachments/assets/b134ca28-7c23-455f-9be0-3c08b727d8c4)

- Chat interface for displaying recognized signs




- Peer-to-peer communication between two computers running the application
- User authentication system

![image](https://github.com/user-attachments/assets/6ec01d8e-e5a3-40c8-a32a-ae79f283223d)

- Dataset creation tools

![image](https://github.com/user-attachments/assets/141119eb-0982-436a-9a40-c8e339359e36)

- Support for numbers (0-9) and alphabets (A-Z)

![image](https://github.com/user-attachments/assets/1651a988-462d-40d7-8d4f-f5a9686d0d77)

##Results

![image](https://github.com/user-attachments/assets/087da2bb-6b34-4d73-949b-748342e892cb)

Results for One Handed Signs

![image](https://github.com/user-attachments/assets/fff968ea-d02c-40cb-9773-1eb73b1bd0f9)

Results for Two Handed Signs

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

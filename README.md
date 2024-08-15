# Crowd Detection System

This project implements a real-time crowd detection system using a live video feed from a camera. The system uses OpenCV's Haar Cascade classifier to detect people in the frame and assess crowd density. It then visualizes the results on a Streamlit-based web interface.

## Table of Contents
- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Advanced Usage](#advanced-usage)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

This application is designed to monitor and analyze crowd density in real-time, which can be useful for various purposes such as security, event management, and public safety. The system categorizes the crowd density into three levels: Low, Medium, and High, and updates the status dynamically on a Streamlit interface.

## System Architecture

The system is structured into the following components:
1. Camera Feed: The source of the live video stream, which is fed into the system via a URL.
2. Processing Engine: Utilizes OpenCV to process the video frames and detect people using a pre-trained Haar Cascade classifier.
3. Crowd Density Analysis: Based on the number of detected people, the system classifies the crowd density.
4. Visualization: The processed video and crowd information are displayed on a Streamlit web interface.

## Features

- Real-Time Detection: Processes each video frame to detect people in real-time.
- Crowd Density Levels: Automatically classifies crowd density into Low, Medium, or High.
- Interactive Web Interface: Provides a user-friendly interface to visualize the video feed and crowd status.
- Performance Metrics: Displays the number of people detected and the average number of people across frames.

## Requirements

Ensure you have the following software and libraries installed:
- Python 3.10
- OpenCV (opencv-python)
- Streamlit
- NumPy

The application has been tested on the following environments:
- Operating Systems: Windows 10, Ubuntu 20.04
- Python Version: Python 3.10
- Dependencies: Listed in requirements.txt

## Installation

Follow these steps to set up the project:

1. Clone the Repository:
   ```bash
   git clone https://github.com/ShivamSharma888/OpenCVSimulation
   cd OpenCVSimulation
   ```
Create a Virtual Environment (Recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   # On Windows use `venv\Scripts\activat'
   ```

# Voice Translator App and Server

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

<img src="https://raw.githubusercontent.com/Owen-Deng/Voice-Translator/master/App/VoiceTranslator/Assets.xcassets/AppIcon.appiconset/Auto...%20(3).png" width="48">

The Voice Translator App and Server is a project that enables users to interactively translate spoken language using their own voice. It provides a seamless communication experience by allowing users to engage in real-time conversations with people who speak different languages.

## Features

- **Voice Recognition**: This App can recognize user's voice and turn to the text content.
- **Language Translation**: This App can send user's speak content to server to processing translation, At present, only Chinese and English are supported.
- **Real-time Interaction**: It has a relatively high response speed and supports real-time face-to-face conversations for two individuals.
- **Voice mimic**: Generated translation is baed on user own voice. It utilize the ML on Server.

## Framwork & tools

### iOS

Swift, Custom UIView, Speech framework,Grand Central Dispatch(GCD), AVFoundation.

### Server

Python, Fastapi, Pytorch, Cuda, [XTTS](https://huggingface.co/coqui/XTTS-v2), [argostranslate](https://pypi.org/project/argostranslate/).

## Showcase
- Custom animation when you say something ,the circle will be changed by your voice power
<img src="https://raw.githubusercontent.com/livingspring/Voice-Translator/master/animation1.gif" width="200"/>

- Custom animation when data is loading the ring will turn circle
<img src="https://raw.githubusercontent.com/livingspring/Voice-Translator/master/animation2.gif" width="200">

[![Video]](https://www.youtube.com/watch?v=oQ_5EHPDpcU)

## Usage

1. Support Python 3.11.5
2. Support iOS 15.6
3. Additionally need XTTS-v2 folder

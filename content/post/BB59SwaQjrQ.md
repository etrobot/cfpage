
---
title: "Build a Chat App with Flutter and OpenAI API"
date: 2023-07-31T15:46:57
draft: true
tags: ['Flutter', 'OpenAI API', 'Text Davinci 003 AI model']
author: Frank
category: efficiency
---

## Introduction

Chat apps have become immensely popular in recent years. In this post, we will learn how to build a simple chat app using Flutter and the OpenAI API. 

### What is Flutter?

Flutter is an open-source framework developed by Google for building cross-platform mobile apps. Some key advantages of Flutter:

- Single codebase for iOS and Android apps
- Fast development with Hot Reload feature  
- Excellent performance and UI
- Native performance with Skia graphics engine
- Supports building web apps as well 

### What is OpenAI API?

OpenAI API provides access to powerful AI models like GPT-3 for generating human-like text content. With the API, you can integrate AI capabilities into your apps.

### What we will build

We will build a basic chat app that allows a user to chat with an AI assistant powered by OpenAI's Davinci 003 model. The app will have the following features:

- User can type and send messages
- AI assistant will reply with human-like responses 
- User can select different AI models

## Project Setup

Let's start by creating a new Flutter project and installing the required packages:

```
- http: For making API requests
- provider: For state management  
- flutter_spinkit: For showing a loader 
- animated_text_kit: For animating bot's text
```

We will also set up a simple theme and app structure with MVC pattern:

```
- lib
  - constants
  - models 
  - providers
  - services
  - widgets
  - screens
```

## Building the UI

The main UI will consist of a Scaffold with an AppBar and a chat screen. The chat screen will show a list of chat messages using a ListView builder. 

We will build reusable widgets like the `TextWidget` and `ChatMessage` to display texts and chat bubbles respectively.

For the input field, we use a TextEditingController to get user's input and pass it to our send message function.

We also add a bottom sheet to allow selecting different AI models. This uses a DropdownButton attached to a list of models fetched from the API. 

The chosen model is persisted using the ModelProvider.

## Integrating OpenAI API

To call the API, we create an API service class with methods like:

```python
getModels() # Fetch list of models
sendMessage(message, model) # Get bot response 
```

The API requires API key and model ID in the request body for authorization and to select the AI model respectively.

We make a POST request to the `/v1/chat/completions` endpoint. 

The response contains the bot's reply in the `choices[0].text` field which we extract and display.

To manage the chat state across app, we create a provider called ChatProvider that stores the chat messages in a list.

## Final Steps

Some final touches like:

- Showing a loader while fetching bot response
- Animating bot's text for a more realistic feel 
- Automate scrolling when new messages arrive  
- Basic error handling

And that concludes this tutorial on building a simple chat app with Flutter and OpenAI API! Let me know in the comments if you have any other questions.


### Reference:
Build ChatGPT App in Flutter using OpenAI API - Full Course:
{{< youtube BB59SwaQjrQ allow_fullscreen>}}
        
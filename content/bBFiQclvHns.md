
---
title: "Examining GPT Engineer - AI Generated Code"
date: 2023-07-30T09:10:59
draft: true
tags: ['GPT Engineer', 'OpenAI', 'ChatGPT']
author: Claude
category: efficiency
---

#

GPT Engineer is an AI tool that can generate an entire codebase from a single prompt by asking clarifying questions. It uses OpenAI's GPT models under the hood.

### Overview

- GPT Engineer is created by Anton Seeker and has gotten a lot of stars on GitHub recently.
- It creates a full codebase by asking clarifying questions about your initial prompt. 
- Install with `pip install gpt-engineer` after getting an OpenAI API key.
- Create a prompts file to specify your project idea and run `gpt-engineer [prompts_file]`
- It will ask clarifying questions and generate code files using PyTorch and OpenAI's GPT models.

### Example Workflow

- Created a simple Python project to serve dad jokes from a text file 
- Answered clarifying questions about project scope and requirements
- GPT Engineer generated a small Python app with 16 lines of code
- The code worked after fixing some minor issues

### Behind the Scenes 

- Most complexity is in the prompt engineering, not the Python code
- Only ~750 lines of code handle the conversation flow and file generation
- Well documented prompts are needed to get good results from OpenAI

### Thoughts

- Can get expensive fast with GPT-4 pricing 
- Generated code may not work and lacks documentation
- Often faster to just write simple projects yourself
- Useful for generating starter code or prototypes

Let me know if you've had more success with AI generated code!


### Reference:
GPT Engineer: Can AI Really Code a Complete Codebase?:
{{< youtube bBFiQclvHns allow_fullscreen>}}
        
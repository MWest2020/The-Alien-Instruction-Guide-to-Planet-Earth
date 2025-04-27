# AI Content Generation System

This directory contains the AI training and content generation system for The Alien Instruction Guide to Planet Earth.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure you have a CUDA-capable GPU for training (recommended) or use CPU.

## Training the Model

To train the model on the existing guide content:

```bash
python train_model.py
```

This will:
1. Load the training data from `training_data/guide_content.json`
2. Train a GPT-2 model on the content
3. Save the trained model to `trained_model/`

## Generating New Content

The model can be used to generate new content for the guide. The generated content will maintain the same humorous and informative style as the existing content.

Example prompts for generation:
- "Title: Flora and Fauna\nContent:"
- "Title: Human Behavior\nContent:"
- "Title: Technology\nContent:"

## Content Structure

The training data is structured in JSON format with the following fields:
- title: The section title
- content: The main content
- style: Writing style characteristics
- tone: Tone characteristics

## Adding New Training Data

To add new content for training:
1. Add new sections to `training_data/guide_content.json`
2. Retrain the model using the steps above

## Best Practices

1. Always review generated content for accuracy and appropriateness
2. Use specific prompts to guide the generation
3. Fine-tune the generation parameters (temperature, top_k, top_p) for desired results
4. Maintain the humorous and informative tone in prompts 
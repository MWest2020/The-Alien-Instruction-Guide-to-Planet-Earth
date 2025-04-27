# Training the Alien Guide AI

This document explains how to train and use the AI model for generating new sections of The Alien Instruction Guide to Planet Earth.

## Prerequisites

- Python 3.7 or higher
- Virtual environment activated (see main README)
- GPU recommended but not required

## Training Data Format

The training data is stored in `ai/training_data/guide_content.json` with the following structure:

```json
{
  "sections": [
    {
      "title": "Section Title",
      "content": "Main content text",
      "style": "style tags (e.g., humorous, informative)",
      "tone": "tone description"
    }
  ],
  "metadata": {
    "target_audience": "alien visitors",
    "writing_style": "humorous and informative",
    "tone": "friendly with a touch of sarcasm",
    "format": "markdown"
  }
}
```

## Training Process

1. **Prepare Training Data**
   - Add new sections to `guide_content.json`
   - Ensure content maintains the guide's humorous tone
   - Use markdown formatting for content

2. **Start Training**
   ```bash
   python ai/train_model.py
   ```
   The process will:
   - Load existing content
   - Fine-tune GPT-2 on your data
   - Save the model to `ai/trained_model/`

3. **Training Parameters**
   Key parameters in `train_model.py`:
   - `num_train_epochs`: Number of training iterations (default: 3)
   - `per_device_train_batch_size`: Batch size (default: 4)
   - `temperature`: Controls randomness (0.7 = balanced)
   - `top_k` and `top_p`: Control output diversity

## Generating Content

After training, you can generate new content with prompts like:
```python
prompt = "Title: Flora and Fauna\nContent:"
```

The model will generate content maintaining:
- The guide's humorous style
- Markdown formatting
- Alien perspective
- Educational value

## Best Practices

1. **Data Quality**
   - Keep sections consistent in length
   - Maintain the humorous alien perspective
   - Include practical information with comedic twists
   - Use markdown formatting consistently

2. **Training Tips**
   - Start with small epochs (3-5) for testing
   - Increase epochs if content quality needs improvement
   - Monitor for overfitting (repetitive or too-similar content)
   - Save different model versions for comparison

3. **Content Generation**
   - Review and edit generated content
   - Check for factual accuracy
   - Ensure humor is appropriate
   - Maintain consistent style with existing sections

## Troubleshooting

Common issues and solutions:
- **Out of Memory**: Reduce batch size
- **Poor Quality**: Increase training epochs
- **Repetitive Content**: Adjust temperature/top_k/top_p
- **Inconsistent Style**: Add more training examples

## Model Architecture

We use GPT-2 as our base model because:
- Good understanding of English language
- Capable of maintaining consistent style
- Efficient for fine-tuning
- Suitable for creative writing

## Future Improvements

Planned enhancements:
- Larger training dataset
- Custom tokenizer for alien terminology
- Interactive content generation interface
- Multi-language support 
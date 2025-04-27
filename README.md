# The Alien Instruction Guide to Planet Earth

A humorous guide for interstellar visitors, with AI-powered content generation.

## Installation

The installation process is now simplified and works across all platforms (Windows, macOS, and Linux):

```bash
python setup.py
```

This will:
1. Check for Python 3.7 or higher
2. Create a virtual environment
3. Install all required dependencies
4. Set up the necessary directory structure

## Usage

1. Activate the virtual environment:
   - Windows: `venv\Scripts\activate.bat`
   - macOS/Linux: `source venv/bin/activate`

2. Train the model:
```bash
python ai/train_model.py
```

3. The model will be trained on the existing content and can generate new sections.

## Project Structure

```
.
├── ai/
│   ├── training_data/      # Training data in JSON format
│   ├── trained_model/      # Saved model after training
│   └── train_model.py      # Training and generation script
├── docs/                   # Generated guide content
├── setup.py               # Installation script
└── requirements.txt       # Python dependencies
```

## Contributing

1. Add new training data to `ai/training_data/guide_content.json`
2. Retrain the model
3. Generate new content
4. Review and edit generated content as needed

## License

This project is licensed under the MIT License - see the LICENSE file for details.
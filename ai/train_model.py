import json
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

def load_training_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def prepare_training_text(data):
    training_text = ""
    for section in data['sections']:
        training_text += f"Title: {section['title']}\n"
        training_text += f"Content: {section['content']}\n"
        training_text += f"Style: {section['style']}\n"
        training_text += f"Tone: {section['tone']}\n\n"
    return training_text

def train_model(training_text, output_dir):
    # Initialize tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    model = GPT2LMHeadModel.from_pretrained('gpt2')
    
    # Add special tokens
    special_tokens = {
        'pad_token': '<PAD>',
        'bos_token': '<BOS>',
        'eos_token': '<EOS>'
    }
    tokenizer.add_special_tokens(special_tokens)
    model.resize_token_embeddings(len(tokenizer))
    
    # Save tokenizer
    tokenizer.save_pretrained(output_dir)
    
    # Prepare dataset
    with open('training_text.txt', 'w', encoding='utf-8') as f:
        f.write(training_text)
    
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path='training_text.txt',
        block_size=128
    )
    
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )
    
    # Training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=1000,
        save_total_limit=2,
    )
    
    # Initialize trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset,
    )
    
    # Train the model
    trainer.train()
    
    # Save the model
    trainer.save_model()
    
    return model, tokenizer

def generate_content(model, tokenizer, prompt, max_length=200):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7,
        top_k=50,
        top_p=0.95
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    # Load and prepare training data
    data = load_training_data('ai/training_data/guide_content.json')
    training_text = prepare_training_text(data)
    
    # Train the model
    output_dir = 'ai/trained_model'
    model, tokenizer = train_model(training_text, output_dir)
    
    # Example generation
    prompt = "Title: Flora and Fauna\nContent:"
    generated_content = generate_content(model, tokenizer, prompt)
    print("\nGenerated Content:")
    print(generated_content) 
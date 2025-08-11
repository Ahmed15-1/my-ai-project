# AI Project: Smart Document Summarizer

Final project for the Building AI course

## Summary

This project develops an AI-powered document summarizer to help users quickly grasp key information from long texts using natural language processing techniques. It uses transformer-based models for summarization.

## Background

* Many people struggle to find time to read lengthy documents.
* Summarization helps increase productivity and understanding.
* I’m personally motivated to make reading easier for busy students and professionals.

## How is it used?

Users input a document or article. The AI generates a concise summary highlighting the main points.  
It’s useful for researchers, students, and anyone needing quick insights from texts.

## Data sources and AI methods

Data comes from public datasets of news articles and summaries, e.g. CNN/DailyMail.  
The project uses transformer models like BART or T5 for abstractive summarization implemented with Hugging Face’s Transformers library.  
Example code is provided in `summarizer.py`.

## Challenges

* Summaries might miss subtle context or generate inaccuracies.
* Large models require significant compute resources.
* Ethical considerations in summarizing sensitive or biased content.

## What next?

* Fine-tune models on domain-specific texts (medical, legal).  
* Develop a user-friendly web interface for broader use.  
* Add multi-language support.

## Acknowledgments

* Building AI course by University of Helsinki and Reaktor  
* Hugging Face Transformers library  
* CNN/DailyMail dataset  

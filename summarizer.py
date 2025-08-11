from transformers import pipeline

def summarize_text(text):
    summarizer = pipeline("summarization")
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def main():
    example_text = (
        "Artificial intelligence (AI) is intelligence demonstrated by machines, "
        "unlike the natural intelligence displayed by humans and animals. Leading AI textbooks define the field "
        "as the study of 'intelligent agents': any device that perceives its environment and takes actions "
        "that maximize its chance of successfully achieving its goals."
    )
    summary = summarize_text(example_text)
    print("Original Text:\n", example_text)
    print("\nSummary:\n", summary)

if __name__ == "__main__":
    main()

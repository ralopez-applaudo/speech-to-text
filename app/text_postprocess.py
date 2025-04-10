from transformers import T5ForConditionalGeneration, T5Tokenizer

class TextCorrector:
    def __init__(self):
        self.tokenizer = T5Tokenizer.from_pretrained("vennify/t5-base-grammar-correction")
        self.model = T5ForConditionalGeneration.from_pretrained("vennify/t5-base-grammar-correction")

    def correct(self, text):
        input_text = f"fix: {text} </s>"
        input_ids = self.tokenizer.encode(input_text, return_tensors="pt", max_length=128, truncation=True)
        outputs = self.model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
        corrected_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return corrected_text
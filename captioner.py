from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# 1. Load pre-trained BLIP model & processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model     = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path: str) -> str:
    # 2. Open and preprocess the image
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")

    # 3. Generate caption (beam search) and decode
    output_ids = model.generate(**inputs, max_length=40, num_beams=4)
    caption = processor.decode(output_ids[0], skip_special_tokens=True)
    return caption

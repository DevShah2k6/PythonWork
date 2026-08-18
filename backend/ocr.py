from paddleocr import PaddleOCR


ocr = PaddleOCR(lang="en")


def extract_text(pdf_path):

    result = ocr.predict(pdf_path)

    extracted_text = []


    for page in result:

        # OCR text and confidence fetch
        texts = page["rec_texts"]
        scores = page["rec_scores"]


        for text, score in zip(texts, scores):

            extracted_text.append({
                "text": text,
                "confidence": score
            })


    return extracted_text
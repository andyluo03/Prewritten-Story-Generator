import pypdfium2 as pdfium

story_pdf = pdfium.PdfDocument("SummerCampStory.ai")

for page_number in range(len(story_pdf)):
    page = story_pdf.get_page(page_number)
    image = page.render().to_pil()
    image.save(f"output/SummerCamp_en_Images/slide-{int(page_number/10)}{page_number%10}.png")
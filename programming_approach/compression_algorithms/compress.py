from io import BytesIO


def compressImage(image, quality):
    # Convert to RGB if necessary
    if image.mode != "RGB":
        image = image.convert("RGB")

    # Save image to BytesIO object
    temp = BytesIO()
    image.save(temp, format="JPEG", quality=quality)

    # Return the size of the resulting file
    return temp.tell()


def compressPDF(pdf, quality):
    # Save image to BytesIO object
    temp = BytesIO()
    pdf.save(temp, quality=quality)

    # Return the size of the resulting file
    return temp.tell()


def compressVideo(video, quality):
    # Save image to BytesIO object
    temp = BytesIO()
    video.save(temp, quality=quality)

    # Return the size of the resulting file
    return temp.tell()


def compressAudio(audio, quality):
    # Save image to BytesIO object
    temp = BytesIO()
    audio.save(temp, quality=quality)

    # Return the size of the resulting file
    return temp.tell()

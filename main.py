import PIL.Image

ascii_chars = ["@", "#", "$", "%", "?", "*", "+", ":", ":", ",", "."]

def resizeImage(image, newWidth):
    width, height = image.size
    ratio = width / height 

    newHeight = int(newWidth * ratio)
    resizeImage = image.resize((newWidth, newHeight))

    return resizeImage

def grayScale(image):
    grayScale = image.convert("L")
    return grayScale

def pixelsToAscii(image):
    pixels = image.getdata()
    characters = "".join([ascii_chars[pixel//25] for pixel in pixels])
    return(characters)


def main(newWidth = 50):
    path = input("Enter path to an image: \n")

    try:
        image = PIL.Image.open(path)

    except Exception as e:
        print(f"An error occoured while opening {path}: {e}")

    newImageData = pixelsToAscii(grayScale(resizeImage(image, newWidth)))

    pixelCount = len(newImageData)
    asciiImage = "\n".join(newImageData[i:(i+newWidth)] for i in range(0, pixelCount, newWidth))

    print(asciiImage)

    with open("ascii.txt", "w") as f:
        f.write(asciiImage)

main()
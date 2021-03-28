from PIL import Image
import requests

def get_image_from_url(url, name):
    response = requests.get(url)
    file = open(f'{name}.png', "wb")
    file.write(response.content)
    file.close()
    return f'{name}.png'

def pixelate(input_file_path, output_file_path, pixel_size):
    palette = [
        255, 148, 37,
        132, 0, 127,
        27, 20, 100,
        111, 188, 255,
    ]
    image = Image.open(input_file_path)
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )

    p_img = Image.new('P', (16, 16))
    p_img.putpalette(palette * 64)

    conv = image.quantize(palette=p_img, dither=0)
    conv.save(output_file_path)


def get_url(input_file_path, output_file_path, pixel_size, url):
    get_image_from_url(url, input_file_path)
# import numpy as np
# from PIL import Image, ImageEnhance, UnidentifiedImageError
#
# def b_and_w_resized(self, gol, image_path, interface):
#     gol.grid_from_image = True
#     try:
#         img = Image.open(image_path).convert('L')
#         enhancer = ImageEnhance.Contrast(img)
#         b_and_w = enhancer.enhance(100)
#         resized_im = b_and_w.resize((700, 700))
#         gol.grid_image = resized_im.transpose(Image.ROTATE_90)
#         self.image_open_success = True
#         return resized_im.transpose(Image.ROTATE_90)
#
#     except AttributeError:
#         self.error_message = "You need to choose a file"
#         self.is_error = True
#         self.image_open_success = False
#     except UnidentifiedImageError:
#         self.error_message = "This is not an image"
#         self.is_error = True
#         self.image_open_success = False
#
#
# def create_ascii_art(self, b_and_w_resized, gol):
#     try:
#         ascii_chars = [' ', 'o']
#         im = np.array(b_and_w_resized).reshape(700, 700)
#         lista = []
#         for i in range(0, 700, gol.settings.cell_size):
#             for j in range(0, 700, gol.settings.cell_size):
#                 lista.append(np.mean(im[j:j + gol.settings.cell_size, i:i + gol.settings.cell_size], dtype=int))
#         ascii_art = [ascii_chars[pixel // 128] for pixel in lista]
#         im = np.array(ascii_art).reshape(int(700 / gol.settings.cell_size), int(700 / gol.settings.cell_size))
#         with open('ascii_art.txt', 'w') as file:
#             for i in im:
#                 file.write(''.join(char for char in i))
#                 file.write('\n')
#     except ValueError:
#         self.image_open_success = False
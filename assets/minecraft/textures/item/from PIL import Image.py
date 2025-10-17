from PIL import Image
original_image = Image.open("C:/Users/Test Drive/thestuff/coloroptions.png")
tile_size = 16
num_tiles = original_image.width // tile_size
tile_limit = 169
for row in range(num_tiles):
    for col in range(num_tiles):
        left = col * tile_size
        upper = row * tile_size
        right = left + tile_size
        lower = upper + tile_size
        tile = original_image.crop((left, upper, right, lower))
        tile.save(f"tile_{row}_{col}.png")
        tile_limit -= 1
        if tile_limit == 0:
            break
    if tile_limit == 0:
        break

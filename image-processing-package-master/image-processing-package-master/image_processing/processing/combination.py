from PIL import Image

def combine_side_by_side(img_path1, img_path2, output_path='combined.jpg'):
    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)
    
    new_img = Image.new('RGB', (img1.width + img2.width, max(img1.height, img2.height)))
    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (img1.width, 0))
    
    new_img.save(output_path)
    return new_img

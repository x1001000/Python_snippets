from PIL import Image
import itertools

def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    #cropped_image.show()
 
 
if __name__ == '__main__':
    image = '1.jpg'
    i = 12
    u = 2000
    for y, x in itertools.product(range(1,5),range(1,4)):
        crop(image, (u*(x-1), u*(y-1), u*x, u*y), f'cropped_{i}.jpg')
        i -= 1
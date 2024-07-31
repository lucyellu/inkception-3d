import os
from PIL import Image, ImageChops

# Increase the maximum allowed image size to prevent DecompressionBombWarning
Image.MAX_IMAGE_PIXELS = None

def process_images(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith('-test.png'):
            fragment_id = file.split('_inference')[0]
            original_file = os.path.join(folder_path, file)
            reversed_file = os.path.join(folder_path, f'{fragment_id}_inference_youssef-test-reversed.png')

            if os.path.exists(reversed_file):
                try:
                    with Image.open(original_file) as orig_img, Image.open(reversed_file) as rev_img:
                        # Ensure both images have the same size
                        if orig_img.size != rev_img.size:
                            print(f"Size mismatch for {file}")
                            continue
                        result_img = ImageChops.subtract(orig_img, rev_img)
                        result_img.save(os.path.join(folder_path, f'{fragment_id}_comp_reversesubtract_.png'))
                except Exception as e:
                    print(f"Error processing {file}: {e}")

# Example usage
process_images("C:/Users/lucyl/Desktop/Compositing/youseff")

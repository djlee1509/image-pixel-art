from PIL import Image
import os


# List of ASCII Characters used to create the output text.
ASCII_CHARS = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]

# Resize the image to generate fixed witdth output.
def resize_image(image, new_fixed_width=100):
  width, height = image.size
  aspect_ratio = height / width
  new_adj_height = int(new_fixed_width * aspect_ratio)
  resized_image = image.resize((new_fixed_width, new_adj_height))
  return resized_image


# Convert the image into greyscale & Sketch.
def image_to_greyscale(image):
  greyscale_image = image.convert("L")
  return greyscale_image


# Convert each pixels to a list of ASCII characters.
def pixel_to_ascii_chars(image):
  pixels = image.getdata()
  characters = "".join([ASCII_CHARS[pixel//30] for pixel in pixels])
  return characters



def main(new_fixed_width=100):
  img_path = input("Enter the valid image path: ")

  try:
    image = Image.open(img_path)
  except:
    print(img_path, "Not a valid image path.")


  # Convert image to ASCII characters.
  resized_image = resize_image(image)
  greyscaled_image = image_to_greyscale(resized_image)
  new_image_data = pixel_to_ascii_chars(greyscaled_image)

  pixel_count = len(new_image_data)
  ascii_image = "\n".join(new_image_data[i:(i + new_fixed_width)] for i in range(0, pixel_count, new_fixed_width))

  filename = os.path.splitext(os.path.basename(img_path))[0]
  output_dir = os.path.join('output/', f"{filename}.txt")

  with open(output_dir, "w") as f:
    f.write(ascii_image)


if __name__ == "__main__":
  main()

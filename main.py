from PIL import Image

# Mảng các ký tự ASCII từ sáng tới tối
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    """Thay đổi kích thước hình ảnh dựa trên chiều rộng mới để giữ nguyên tỷ lệ."""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayscale_image(image):
    """Chuyển đổi hình ảnh thành grayscale."""
    return image.convert("L")

def pixels_to_ascii(image):
    """Chuyển đổi các pixel trong hình ảnh thành ký tự ASCII."""
    pixels = image.getdata()
    ascii_str = ""
    for pixel in pixels:
        ascii_str += ASCII_CHARS[pixel // 25]
    return ascii_str

def color_ascii_art_terminal(image_path, new_width=100):
    """Chuyển đổi hình ảnh thành ASCII Art với màu sắc tương ứng và in ra terminal."""
    # Mở ảnh từ đường dẫn
    image = Image.open(image_path)

    # Thay đổi kích thước và chuyển đổi sang grayscale
    image = resize_image(image, new_width)
    grayscale = grayscale_image(image)

    # Lấy chuỗi ASCII
    ascii_art = pixels_to_ascii(grayscale)

    # Chuyển đổi thành mảng 2D
    width = grayscale.width
    ascii_art_lines = [ascii_art[index:index + width] for index in range(0, len(ascii_art), width)]

    # In ra terminal với màu sắc
    for y, line in enumerate(ascii_art_lines):
        for x, char in enumerate(line):
            r, g, b = image.getpixel((x, y))
            print(f"\033[38;2;{r};{g};{b}m{char}", end="")
        print("\033[0m")  # Đặt lại màu cho dòng mới trong terminal
    print("\033[0m")  # Đặt lại màu khi kết thúc

def color_ascii_art_html(image_path, output_path, new_width=100):
    """Chuyển đổi hình ảnh thành ASCII Art với màu sắc tương ứng và lưu vào file HTML."""
    # Mở ảnh từ đường dẫn
    image = Image.open(image_path)

    # Thay đổi kích thước và chuyển đổi sang grayscale
    image = resize_image(image, new_width)
    grayscale = grayscale_image(image)

    # Lấy chuỗi ASCII
    ascii_art = pixels_to_ascii(grayscale)

    # Chuyển đổi thành mảng 2D
    width = grayscale.width
    ascii_art_lines = [ascii_art[index:index + width] for index in range(0, len(ascii_art), width)]

    # Mở tập tin HTML để ghi kết quả
    with open(output_path, "w") as f:
        f.write("<html><body style='background-color: black; font-family: monospace; line-height: 1;'><pre>")
        for y, line in enumerate(ascii_art_lines):
            for x, char in enumerate(line):
                r, g, b = image.getpixel((x, y))
                f.write(f"<span style='color: rgb({r},{g},{b});'>{char}</span>")
            f.write("<br>")
        f.write("</pre></body></html>")

if __name__ == "__main__":
    # Đường dẫn tới hình ảnh cần chuyển đổi và tập tin đầu ra
    image_path = "cat3.jpg"  # Đặt đường dẫn tới ảnh của bạn
    output_path_html = "ascii_art_colored.html"  # Đặt tên tập tin đầu ra HTML

    # In ASCII art có màu ra terminal
    print("Printing colored ASCII art to terminal:")
    color_ascii_art_terminal(image_path)

    # Lưu ASCII art có màu vào file HTML
    print(f"\nSaving colored ASCII art to {output_path_html}")
    color_ascii_art_html(image_path, output_path_html)
    print("Done!")
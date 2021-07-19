from PIL import Image


def handle_sub_images(sub_images, out=None, max_height=4096, resize=960):
    for sub in sub_images:
        sub.image.thumbnail((resize, resize))
    width, height = sub.image.size
    max_lines = int(max_height/height)

    for i in range(0, len(sub_images), max_lines):
        chunk = sub_images[i: i + max_lines]
        data = yield merge_images([item.image for item in chunk])
        if out is not None and data:
            for pos, text in data:
                index = round(pos["top"]/height)
                sub = chunk[index]
                sub.text = text
                out.append(sub)


def merge_images(images):
    width, height = images[0].size
    new_im = Image.new("1", (width, height*len(images)))
    y_offset = 0
    for im in images:
        new_im.paste(im, (0, y_offset))
        y_offset += height
    return new_im


def format_srt_time(t):
    return "{:02d}:{:02d}:{:02d},{:03d}".format(*t)

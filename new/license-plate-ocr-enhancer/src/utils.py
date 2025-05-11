def display_image(image, title="Image", cmap_override=None):
    plt.figure(figsize=(6, 4))
    if len(image.shape) == 2:
        plt.imshow(image, cmap='gray' if cmap_override == 'gray' or cmap_override is None else cmap_override)
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Error: Could not load image at {image_path}")
    return image

def save_image(image, save_path):
    cv2.imwrite(save_path, image)

def crop_black_edges(image, threshold=15):
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()
    mask = gray > threshold
    coords = np.argwhere(mask)
    if coords.size == 0:
        return image
    y0, x0 = coords.min(axis=0)
    y1, x1 = coords.max(axis=0) + 1
    return image[y0:y1, x0:x1]
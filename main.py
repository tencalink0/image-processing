import imageio.v2 as imageio;
import numpy as np;

RED = 0;
GREEN = 1;
BLUE = 2;

class Coordinate():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

class Colour():
    def __init__(self, red, green, blue):
        self.red = red;
        self.red = green;
        self.blue = blue;

class Image:
    def __init__(self, path):
        if path == None:
            self.img = np.zeros((100, 200, 3), dtype=np.uint8);
        else:
            self.img = imageio.imread(path);

    def disp_properties(self):
        print(f"Type: {type(self.img)}");
        print(f"Shape: {self.img.shape}");
        print(f"Data type: {self.img.dtype}");
        print("");

    def disp_pixel(self, pos):
        if pos.y < len(self.img) and pos.y > 0:
            if pos.x < len(self.img[pos.y]) and pos.x > 0:
                print(len(self.img), len(self.img[pos.y]));
                current_img = self.img[pos.y][pos.x];
                print(f"Red: {current_img[RED]}");
                print(f"Green: {current_img[GREEN]}");
                print(f"Blue: {current_img[BLUE]}");
                return;

        print('Not within boundaries');

    def fill(self, colour):
        for i in range(self.img.shape[0]):
            print("yes");



def main():
    img1 = Image('balloon-100.jpg');
    pos1 = Coordinate(1, 1);

    img1.disp_properties();
    img1.disp_pixel(pos1);

if __name__ == "__main__":
    main();
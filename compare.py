import matplotlib.pyplot as plt
import skimage, os
from skimage import io, img_as_float
from skimage.color import rgb2gray
from skimage.metrics import structural_similarity as ssim
from skimage.transform import resize
from skimage.io import imread
from skimage.util import img_as_ubyte

def loadImage(filename):
    return io.imread(filename)

def plot(i1, i2, diff, ssim):
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 4), sharex=True, sharey=True)
    ax = axes.ravel()

    ax[0].imshow(i1, cmap=plt.cm.gray)
    ax[1].set_xlabel("SSIM: {:.2f}".format(ssim))
    ax[1].imshow(i2, cmap=plt.cm.gray)
    ax[2].imshow(diff, cmap=plt.cm.gray)

    fig.tight_layout()
    plt.show()

def compare(image1_filename, image2_filename):
    image1 = loadImage(image1_filename)
    try:
        image2 = img_as_ubyte(resize(loadImage(image2_filename), (image1.shape[0], image1.shape[1]), anti_aliasing=True))
    except ValueError as err:
        print("Erro: {0}".format(err))
        return 0, None, None, None
    except SyntaxError as err:
        print("Erro: {0}".format(err))
        return 0, None, None, None

    image1_bw = rgb2gray(image1)
    image2_bw = rgb2gray(image2)

    #print(image1.max(), image1.min())
    #print(image2.max(), image2.min())

    ssim_const, diff = ssim(image1_bw, image2_bw, full=True)
    diff = (diff * 255).astype("uint8")

    #print(ssim_const)
    return ssim_const, image1_bw, image2_bw, diff
    #

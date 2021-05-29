import glob, argparse
import compare as c
from tqdm import tqdm

def getImagesFromDir(dir):
    jpg_files = glob.glob(dir + '/*.jpg', recursive = True)
    png_files = glob.glob(dir + '/*.jpg', recursive = True)

    return jpg_files + png_files

def trataParametros():
    #criei o objeto que fará o parser, responsável por passar os argumentos em linha de comando
    parser = argparse.ArgumentParser()

    #argumentos
    parser.add_argument("dir", help = "Caminho em que as imagens serão buscadas")
    parser.add_argument("i", help = "Imagem a ser comparada com as outras")

    #essa chamada faz com que os parâmetros recebidos pelo programa sejam armazenados no objeto args
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = trataParametros()
    images_file_list = getImagesFromDir(args.dir) #"D:/Exemplo Imagens"

    d = {}
    i = 0
    for f in tqdm(images_file_list):
        #print(f)
        score, _, _, _ = c.compare(args.i, f)
        d[score] = f
        i+=1

    print("\n")
    for i in sorted(d, reverse=True):
        print (i, d[i])
        score, i1, i2, diff = c.compare(args.i, d[i])
        c.plot(i1, i2, diff, score)

import glob, argparse
import compare as c

def trataParametros():
    #criei o objeto que fará o parser, responsável por passar os argumentos em linha de comando
    parser = argparse.ArgumentParser()

    #argumentos
    parser.add_argument("i1", help = "Primeira Imagem")
    parser.add_argument("i2", help = "Segunda Imagem")

    #essa chamada faz com que os parâmetros recebidos pelo programa sejam armazenados no objeto args
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = trataParametros()
    ssim_const, image1_bw, image2_bw, diff = c.compare(args.i1, args.i2)
    c.plot(image1_bw, image2_bw, diff, ssim_const)

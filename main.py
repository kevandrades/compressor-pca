# bibliotecas builtin
import os
import glob
import re
# % ________________________________________
## bibliotecas de terceiros
import numpy as np
from sklearn.decomposition import PCA
from PIL import Image
# % ________________________________________


def vectorize_img(path: str) -> tuple:
    """Lê imagem do diretório e transforma em array unificado.

    Args:
        path (str): Caminho para o arquivo.

    Returns:
        tuple: Retorna altura, largura, número de canais e array representando a imagem.
    """
    with Image.open(path) as image:
        image_array = np.array(image)
    
    if len(image_array.shape) == 3:
        height, width, channels = image_array.shape
        
    else:
        height, width = image_array.shape
        channels = 1

    flattened_image = image_array.reshape(-1, channels)
    
    return height, width, channels, flattened_image



def pca_over_image(
        height: int,
        width: int, channels: int,
        flattened_image: np.array,
        variance_threshold: float = 0.9998
    ) -> np.array:
    """Transforma a matriz de imagem utilizando Análise de Componentes Principais.

    Args:
        height (int): Altura da imagem.
        width (int): Largura da imagem.
        channels (int): Número de canais da imagem.
        flattened_image (np.array): Array unificado representando a imagem.
        variance_threshold (float, optional): Proporção da variância mínima a ser preservada pela redução de dimensionalidade. Deve ser número entre 0 e 1. Por padrão, preserva 0.9998.

    Returns:
        np.array: Retorna imagem em array reconstruída pelo PCA.
    """
    if not 0 <= variance_threshold <= 1:
        raise Exception("Variância deve estar entre 0 e 1.")

    pca = PCA(n_components=variance_threshold)

    reduced_image = pca.fit_transform(flattened_image)

    reconstructed_image = pca.inverse_transform(reduced_image)

    reconstructed_image = (
        reconstructed_image.reshape(height, width) if channels == 1
        else reconstructed_image.reshape(height, width, channels)
    )

    reconstructed_image = np.clip(reconstructed_image, 0, 255).astype(np.uint8)

    return reconstructed_image



def save_image(image: np.array, filename: str, dir: str = "out") -> None:
    """Converte array em imagem e salva no diretório selecionado.

    Args:
        image (np.array): Array representando a imagem.
        filename (str): Nome do arquivo que será salvo.
        dir (str, optional): Diretório onde o arquivo será salvo. Por padrão, será salvo no diretório "out".
    """
    base_name = os.path.basename(filename)
    reduced_image_path = f"{dir}/{base_name}"
    
    Image.fromarray(image).save(reduced_image_path)


if __name__ == "__main__":
    files = [file for file in glob.glob("img/*.*") if re.search("\\.(jpe{0,1}g|png)$", file.lower())]

    for progress, image_path in enumerate(files, start = 1):
        try:
            image = pca_over_image(*vectorize_img(image_path))

            save_image(image, os.path.basename(image_path))

        except Exception as error:
            with open("log/errors.txt", "a") as log:
                log.write(f"Erro {error} com {image_path}")

        print(f"{progress} / {len(files)}", end="\r")

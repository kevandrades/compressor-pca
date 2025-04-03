# Compressor de Imagens via Análise de Componentes Principais

O script utiliza análise de componentes principais (PCA) para reduziir o tamanho de arquivos sem perdas significativas na qualidade das imagens.

Insira todos os arquivos de imagem (a serem comprimidos) no diretório `img` e execute o programa com:

```
python main.py
```

Os resultados serão exibidos no diretório `out`.

A exemplo, consta no repositório uma imagem da Monalisa, de Leonardo da Vinci. Execute com a imagem da Monalisa como teste para ver os resultados.

<h3>Aviso

Verifique com cuidado os resultados. Não necessariamente a compressão vai funcionar para todas as imagens. Algumas podem ter perda de qualidade.

Você pode modificar o parâmetro `variance_threshold` no arquivo `main.py` caso queira modificar a proporção da variância preservada.

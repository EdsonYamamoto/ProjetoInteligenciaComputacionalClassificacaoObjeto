# Projeto de Inteligencia Computacional - Classificação de Objeto
Objetivo do projeto é classifica as imagens apartir dos padrões oferecido pelo Museu de Harvard.

Como demostra o site: http://apps.harvardartmuseums.org/art-explorer/

Para instalar a biblioteca atualmente utilizado em nosso projeto, pode ser encontrado no arquivo:
```
requirements_gpu.txt
```

------------------------------

## Organização dos arquivos:

- **coletaDados:**
Contém o codigo da coleta da dados.

É necessario utilizar um chromedrive.exe para realizar a comunicação, é possivel obter no site abaixo:

https://chromedriver.chromium.org/downloads

A versão utilizada para em nosso chrome é [83.0.4103.97], caso não corresposda a versão atual do seu chrome é necessario adéqua.

- **projetoGPU:**
Contém o codigo da rede neural.

Arquivo com as amostras:
```
dados v2.rar
```
É necessario descompacta e extrair para dentro do Dataset.

Dentro da pasta projetoGPU, contém graficos dos resultado do ultimo treinamento utilizando 5 classes com 100 amostra em cada.

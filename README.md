# Hand Gesture Detection

Este repositório contém um projeto de **Detecção de Gestos Manuais** utilizando técnicas de Visão Computacional e Aprendizado de Máquina. O objetivo é capturar imagens das mãos, extrair landmarks (pontos de referência) e treinar um modelo para reconhecer gestos específicos.

## Estrutura do Projeto

- **`coletarImagem.py`**: Script para capturar imagens da webcam e salvar em um diretório específico.
- **`criardataset.py`**: Script para processar as imagens capturadas e extrair as landmarks das mãos, criando um dataset para treinamento.
- **`classificadorTreinamento.py`**: Script para treinar um modelo de classificação de gestos utilizando o dataset criado.
- **`classificadorInferencia.py`**: Script para realizar a inferência em tempo real, reconhecendo gestos através da webcam.
- **`data.pickle`**: Arquivo contendo o dataset de treinamento serializado.
- **`model.pickle`**: Arquivo contendo o modelo treinado serializado.

## Dependências

As principais bibliotecas utilizadas neste projeto são:

- `opencv-python`
- `mediapipe`
- `scikit-learn`
- `matplotlib`

## Como Utilizar

1. **Coletar Imagens**: Utilize o script `coletarImagem.py` para capturar imagens das mãos realizando diferentes gestos. As imagens serão salvas no diretório especificado.

2. **Criar Dataset**: Execute o script `criardataset.py` para processar as imagens e extrair as landmarks das mãos, gerando um dataset para treinamento.

3. **Treinar o Modelo**: Utilize o script `classificadorTreinamento.py` para treinar um modelo de classificação de gestos com o dataset criado.

4. **Inferência em Tempo Real**: Execute o script `classificadorInferencia.py` para reconhecer gestos em tempo real através da webcam, utilizando o modelo treinado.

## Referências

- [MediaPipe Gesture Recognizer](https://ai.google.dev/edge/mediapipe/solutions/vision/gesture_recognizer)
- [Hand Gesture Recognition Based on Computer Vision: A Review of Techniques](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8321080/)
- [Hand Gesture Recognition Database](https://www.kaggle.com/datasets/gti-upm/leapgestrecog)

Este projeto é uma implementação prática de técnicas de visão computacional e aprendizado de máquina para reconhecimento de gestos manuais, utilizando ferramentas como OpenCV e MediaPipe. 

# Introduction
We built a Chinese poem learning system including three functions.
1. Chinese poem writer
2. Poem appreciation
3. Translation of poem in English

# Platform
- Ubuntn/Windows
- Python>=3.6, Pytorch, Keras

# Details
### Chinese Poem Writer
- This part is forked from [Chinese poem writer](https://github.com/jfzhang95/Chinese_Poem_Writer).
- The Chinese poem writer is based on [Temporal Convolutional Networks (TCN)](https://arxiv.org/abs/1803.01271). This paper recently indicates that a simple TCN architecture outperforms RNNs across a diverse range of tasks and datasets, while demonstrating longer effective memory.
### Poem Appreciation and Translation
- We embedded two packages from [THUCC](http://thucc.thunlp.org) into our system.

# How to Use This System
- run *python MainWindow.py*


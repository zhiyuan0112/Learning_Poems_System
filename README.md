# Introduction
We built a Chinese poem learning system including three functions.
1. Chinese poem writer
2. Poem appreciation
3. Translation of poem in English

# Platform
- Ubuntu/Windows
- Python>=3.6, Pytorch, Keras

# Details
### Chinese Poem Writer
- This part is forked from [Chinese poem writer](https://github.com/jfzhang95/Chinese_Poem_Writer).
- The Chinese poem writer is based on [Temporal Convolutional Networks (TCN)](https://arxiv.org/abs/1803.01271). This paper recently indicates that a simple TCN architecture outperforms RNNs across a diverse range of tasks and datasets, while demonstrating longer effective memory.
- ![image](https://github.com/zhiyuan0112/Learning_Poems_System/blob/master/images/poemWriter.png)
### Poem Appreciation and Translation
- We embedded two packages from [THUCC](http://thucc.thunlp.org) into our system.
- ![image](https://github.com/zhiyuan0112/Learning_Poems_System/blob/master/images/poemApreciation.png)
- ![image](https://github.com/zhiyuan0112/Learning_Poems_System/blob/master/images/poemTranslation.png)

# Interface Presentation
- We show the interface of our system.

![image](https://github.com/zhiyuan0112/Learning_Poems_System/blob/master/images/system.png)

# Usage
- run
```markdown
python MainWindow.py
```

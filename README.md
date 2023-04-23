# Facial Recognition Project

The face recognition task was accomplished in this project by implementing Siamese Networks, as proposed in the research paper "Siamese Neural Networks for One-shot Image Recognition" by Koch et al. Positive samples were obtained from my webcam, while negative samples were obtained from the LFW Face Database created by the University of Massachusetts. The network was fed with anchor and validation images, which were then processed in the embedding layer, and similarity (L1) was computed in the distance layer. Consequently, all anchor images were validated correctly. In addition, the network was able to correctly label the negative samples as false predictions. Therefore, the implementation of Siamese Networks not only accurately validated the positive anchor images, but also correctly identified the negative samples as unrelated to the validation set.

Koch et. al., [Siamese Neural Networks for One-shot Image Recognition](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)
[LFW  Face Databse](http://vis-www.cs.umass.edu/lfw/)


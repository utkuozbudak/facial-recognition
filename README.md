# Facial Recognition Project

The face recognition task was accomplished in this project by implementing Siamese Networks, as proposed in the research paper "Siamese Neural Networks for One-shot Image Recognition" by Koch et al. Positive samples were obtained from my webcam, while negative samples were obtained from the LFW Face Database created by the University of Massachusetts. The network was fed with anchor and validation images, which were then processed in the embedding layer, and similarity (L1) was computed in the distance layer. Consequently, all anchor images were validated correctly. In addition, the network was able to correctly label the negative samples as false predictions. Therefore, the implementation of Siamese Networks not only accurately validated the positive anchor images, but also correctly identified the negative samples as unrelated to the validation set. See below links for paper and LFW Face Database.


Simple Siamese Network:

![Simple Siamese Network](https://user-images.githubusercontent.com/56653665/233863186-ed9fee85-2dd9-4092-a1f5-8d96726ec7c2.png)

Proposed ConvNet in the paper:

![Proposed embedding layer in the paper](https://user-images.githubusercontent.com/56653665/233863231-1224ed9a-5f1b-4151-b19d-4a56d704af57.png)


Koch et. al., [Siamese Neural Networks for One-shot Image Recognition](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)

[LFW  Face Databse](http://vis-www.cs.umass.edu/lfw/)

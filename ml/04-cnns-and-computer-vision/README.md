# CNNs and Computer Vision

## Why This Section Matters

Convolutional Neural Networks are where deep learning proved it could work at scale. AlexNet's 2012 ImageNet victory wasn't just a benchmark improvement — it was the moment that convinced the broader ML community that deep neural networks were viable. The progression from AlexNet to VGGNet to GoogLeNet to ResNet tells the story of how the field learned to train deeper and deeper networks, discovering architectural principles (skip connections, 1×1 convolutions, batch normalization) that remain foundational across all of modern deep learning.

But the story doesn't end with CNNs. Starting with ViT (2020), Vision Transformers proved that the attention mechanism from NLP could match or surpass CNNs on vision tasks — fundamentally reshaping the field. Understanding both the CNN foundations and the ViT transition gives you the full vocabulary of modern computer vision: feature hierarchies, spatial invariance, patch embeddings, and multi-scale attention.

## Prerequisites

- [Section 03 — Deep Learning Fundamentals](../03-deep-learning-fundamentals/README.md)

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read — essential for understanding this topic |
| ⭐ | On the Ilya Sutskever reading list |

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑⭐ | 📄 Paper | ImageNet Classification with Deep Convolutional Neural Networks (AlexNet) | Krizhevsky, Sutskever, Hinton | 2012 | [Paper](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks) | The paper that launched the deep learning revolution. Won ImageNet 2012 by a massive margin using ReLU, dropout, GPU training, and data augmentation. |
| 🔑⭐ | 📄 Paper | Deep Residual Learning for Image Recognition (ResNet) | He, Zhang, Ren, Sun | 2015 | [Paper](https://arxiv.org/abs/1512.03385) | Introduced skip connections enabling training of 100+ layer networks. Residual learning is now a universal design pattern across all of deep learning. |
| 🔑 | 🎥 Course | Stanford CS231n: CNNs for Visual Recognition | Fei-Fei Li, Karpathy, Johnson | 2017 | [YouTube](https://www.youtube.com/playlist?list=PL3FW7Lu3i5JvHM8ljYj-zLfQRF3EO8sYv) | The gold-standard course on CNNs. Covers backprop, convolutions, architectures, detection, segmentation, and generative models. |
| | 📄 Paper | Very Deep Convolutional Networks for Large-Scale Image Recognition (VGGNet) | Simonyan, Zisserman | 2014 | [Paper](https://arxiv.org/abs/1409.1556) | Showed that network depth with small 3×3 filters is critical for good performance. Simple, elegant architecture still used as a feature extractor. |
| | 📄 Paper | Going Deeper with Convolutions (GoogLeNet / Inception) | Szegedy et al. | 2014 | [Paper](https://arxiv.org/abs/1409.4842) | Introduced the Inception module with parallel convolutions at multiple scales and 1×1 convolutions for dimensionality reduction. |
| | 📄 Paper | Network In Network | Lin, Chen, Yan | 2013 | [Paper](https://arxiv.org/abs/1312.4400) | Pioneered 1×1 convolutions and global average pooling — ideas adopted by nearly every subsequent architecture. |
| ⭐ | 📄 Paper | Multi-Scale Context Aggregation by Dilated Convolutions | Yu, Koltun | 2015 | [Paper](https://arxiv.org/abs/1511.07122) | Introduced dilated (atrous) convolutions to systematically aggregate multi-scale context without losing resolution. Key for dense prediction tasks. |
| | 📝 Article | Feature Visualization | Olah et al. | 2017 | [Distill](https://distill.pub/2017/feature-visualization/) | Beautiful interactive exploration of what neural network neurons learn to detect. Makes CNN internals tangible and intuitive. |
| | 📝 Article | The Building Blocks of Interpretability | Olah et al. | 2018 | [Distill](https://distill.pub/2018/building-blocks/) | Builds on feature visualization to show how network components combine into interpretable explanations of model behavior. |

### Vision Transformers

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑 | 📄 Paper | An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ViT) | Dosovitskiy et al. | 2020 | [Paper](https://arxiv.org/abs/2010.11929) | THE must-read. Proved transformers could match/beat CNNs on vision by treating image patches as tokens. |
| | 📄 Paper | Training Data-Efficient Image Transformers (DeiT) | Touvron et al. | 2021 | [Paper](https://arxiv.org/abs/2012.12877) | Showed how to train ViTs without massive datasets using knowledge distillation and strong data augmentation. |
| | 📄 Paper | Swin Transformer: Hierarchical Vision Transformer using Shifted Windows | Liu et al. | 2021 | [Paper](https://arxiv.org/abs/2103.14030) | Hierarchical vision transformer with shifted windows — efficient multi-scale feature extraction for dense prediction. |
| | 📄 Paper | End-to-End Object Detection with Transformers (DETR) | Carion et al. | 2020 | [Paper](https://arxiv.org/abs/2005.12872) | Eliminated hand-designed components (anchors, NMS) in object detection by framing it as a set prediction problem. |

## Suggested Order

1. **CS231n lectures** — Watch lectures 1–9 for the full foundation (convolutions, architectures, training)
2. **AlexNet** — Read the paper that started it all; appreciate the engineering and the vision
3. **Network In Network** — Short paper, introduces 1×1 convolutions you'll see everywhere
4. **VGGNet** — Simple depth scaling, easy to follow after AlexNet
5. **GoogLeNet / Inception** — Multi-scale thinking and efficient architecture design
6. **ResNet** — The most important architecture paper; understand skip connections deeply
7. **Dilated Convolutions** — Expanding receptive fields without downsampling
8. **Distill: Feature Visualization** → **Building Blocks** — End with interpretability to understand what your networks actually learn
9. **ViT** — Read the paper that proved transformers could rival CNNs; understand patch embeddings and positional encodings
10. **DeiT** — See how to train ViTs efficiently without JFT-scale data
11. **Swin Transformer** — Learn hierarchical multi-scale attention with shifted windows
12. **DETR** — Understand how transformers replace hand-designed detection pipelines

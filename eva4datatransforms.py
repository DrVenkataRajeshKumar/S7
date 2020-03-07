{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled4.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPPWmlo5XIBix3G2PcIkdeh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DrVenkataRajeshKumar/S7/blob/master/eva4datatransforms.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K_UUmpB0UW5h",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        "from torchvision import transforms\n",
        "\n",
        "class Transforms:\n",
        "  \"\"\"\n",
        "  Helper class to create test and train transforms\n",
        "  \"\"\"\n",
        "  def __init__(self, normalize=False, mean=None, stdev=None):\n",
        "    if normalize and (not mean or not stdev):\n",
        "      raise ValueError('mean and stdev both are required for normalize transform')\n",
        "  \n",
        "    self.normalize=normalize\n",
        "    self.mean = mean\n",
        "    self.stdev = stdev\n",
        "\n",
        "  def test_transforms(self):\n",
        "    transforms_list = [transforms.ToTensor()]\n",
        "    if(self.normalize):\n",
        "      transforms_list.append(transforms.Normalize(self.mean, self.stdev))\n",
        "    return transforms.Compose(transforms_list)\n",
        "\n",
        "  def train_transforms(self, pre_transforms=None, post_transforms=None):\n",
        "    if pre_transforms:\n",
        "      transforms_list = pre_transforms\n",
        "    else:\n",
        "      transforms_list = []\n",
        "    transforms_list.append(transforms.ToTensor())\n",
        "\n",
        "    if(self.normalize):\n",
        "      transforms_list.append(transforms.Normalize(self.mean, self.stdev))\n",
        "    if post_transforms:\n",
        "      transforms_list.extend(post_transforms)\n",
        "    return transforms.Compose(transforms_list)"
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
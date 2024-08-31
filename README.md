# Fork of [xuanandsix/GFPGAN-onnxruntime-demo](https://github.com/xuanandsix/GFPGAN-onnxruntime-demo)

Differences between original repository and fork:

* Compatibility with PyTorch >=2.4. (🔥)
* Original pretrained models and converted ONNX models from GitHub [releases page](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases). (🔥)
* Installation with [requirements.txt](requirements.txt) file.
* Simplified [torch2onnx.py](torch2onnx.py) file.
* The following warnings has been fixed:
  * FutureWarning: You are using 'torch.load' with 'weights_only=False'.

# Installation

```shell
pip install -r requirements.txt
```

# Pretrained models

| Name       | Link                                                                                                                                                                                                       |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GFPGANv1.2 | [PyTorch](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/GFPGANv1.2.pth), [ONNX](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/GFPGANv1.2.onnx) |
| GFPGANv1.3 | [PyTorch](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/GFPGANv1.3.pth), [ONNX](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/GFPGANv1.3.onnx) |
| GFPGANv1.4 | [PyTorch](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/GFPGANv1.4.pth), [ONNX](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/GFPGANv1.4.onnx) |

# Export to ONNX format

```shell
python torch2onnx.py  --src_model_path GFPGANv1.2.pth --dst_model_path GFPGANv1.2.onnx
python torch2onnx.py  --src_model_path GFPGANv1.3.pth --dst_model_path GFPGANv1.3.onnx
python torch2onnx.py  --src_model_path GFPGANv1.4.pth --dst_model_path GFPGANv1.4.onnx
```

# Inference

```shell
python demo_onnx.py --model_path GFPGANv1.2.onnx --image_path cropped_faces/Justin_Timberlake_crop.png --save_path output1.2.png
python demo_onnx.py --model_path GFPGANv1.3.onnx --image_path cropped_faces/Justin_Timberlake_crop.png --save_path output1.3.png
python demo_onnx.py --model_path GFPGANv1.3.onnx --image_path cropped_faces/Justin_Timberlake_crop.png --save_path output1.4.png
```

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

| Name       | Model Size (MB) | Link                                                                                                                                                                                                           | SHA-256                                                                                                                              |
|------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| GFPGANv1.2 | 332.5<br>324.5  | [PyTorch](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/gfpgan-v1.2.pth)<br>[ONNX](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/gfpgan-v1.2.onnx) | 29e25ee90c170f4231163f4c83df6b59c968b73f3ce00cb884015ae005db083c<br>d1e718d437b6d53f9ec3216a4ad468a74caf98187217dc9f40eab45f42d0ed14 |
| GFPGANv1.3 | 332.5<br>324.5  | [PyTorch](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/gfpgan-v1.3.pth)<br>[ONNX](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/gfpgan-v1.3.onnx) | c953a88f2727c85c3d9ae72e2bd4846bbaf59fe6972ad94130e23e7017524a70<br>c01d3411d2c202d95f1ac5f7d09f99567de39a06577e4e66173ecefb3f242f5a |
| GFPGANv1.4 | 332.5<br>324.5  | [PyTorch](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/gfpgan-v1.4.pth)<br>[ONNX](https://github.com/clibdev/GFPGAN-onnxruntime-demo/releases/latest/download/gfpgan-v1.4.onnx) | e2cd4703ab14f4d01fd1383a8a8b266f9a5833dacee8e6a79d3bf21a1b6be5ad<br>497ff5b6d6008ec101b2714776ce39ce67a722a78720dfce84231e612e45053e |

# Export to ONNX format

```shell
python torch2onnx.py  --src_model_path gfpgan-v1.2.pth --dst_model_path gfpgan-v1.2.onnx
python torch2onnx.py  --src_model_path gfpgan-v1.3.pth --dst_model_path gfpgan-v1.3.onnx
python torch2onnx.py  --src_model_path gfpgan-v1.4.pth --dst_model_path gfpgan-v1.4.onnx
```

# Inference

```shell
python demo_onnx.py --model_path gfpgan-v1.2.onnx --image_path cropped_faces/Justin_Timberlake_crop.png --save_path output1.2.png
python demo_onnx.py --model_path gfpgan-v1.3.onnx --image_path cropped_faces/Justin_Timberlake_crop.png --save_path output1.3.png
python demo_onnx.py --model_path gfpgan-v1.3.onnx --image_path cropped_faces/Justin_Timberlake_crop.png --save_path output1.4.png
```

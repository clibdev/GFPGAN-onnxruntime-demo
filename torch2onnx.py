import torch
from collections import OrderedDict
import argparse
from GFPGANReconsitution import GFPGAN

parser = argparse.ArgumentParser("ONNX converter")
parser.add_argument('--src_model_path', type=str, default=None, help='src model path')
parser.add_argument('--dst_model_path', type=str, default=None, help='dst model path')
args = parser.parse_args()

# device = torch.device('cuda')
model_path = args.src_model_path
onnx_model_path = args.dst_model_path

model = GFPGAN()  # .cuda()

x = torch.rand(1, 3, 512, 512)  # .cuda()

state_dict = torch.load(model_path, weights_only=True)['params_ema']
new_state_dict = OrderedDict()
for k, v in state_dict.items():
    # stylegan_decoderdotto_rgbsdot1dotmodulated_convdotbias
    if "stylegan_decoder" in k:
        k = k.replace('.', 'dot')
        new_state_dict[k] = v
        k = k.replace('dotweight', '.weight')
        k = k.replace('dotbias', '.bias')
        new_state_dict[k] = v
    else:
        new_state_dict[k] = v

model.load_state_dict(new_state_dict, strict=False)
model.eval()

torch.onnx.export(
    model,
    x,
    onnx_model_path,
    export_params=True,
    opset_version=11,
    do_constant_folding=True,
    input_names=['input'],
    output_names=[]
)

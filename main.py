import json
from PIL import Image
import pyautogui as pag
import torch
from torchvision import transforms
import matplotlib.pyplot as plt#시각화를 위한 package

from pytorch_pretrained_vit import ViT

model_name = 'B_16_imagenet1k'
model = ViT(model_name, pretrained=True)

#img = Image.open('001.jpg').convert('RGB')
img = Image.open('001_adv.png').convert('RGB')
plt.imshow(img)
plt.show()
# Preprocess image
tfms = transforms.Compose([transforms.Resize(model.image_size), transforms.ToTensor(), transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),])
img = tfms(img).unsqueeze(0)


# Load class names
labels_map = json.load(open('labels_map.txt'))
labels_map = [labels_map[str(i)] for i in range(1000)]


# Classify
model.eval()
with torch.no_grad():
    outputs = model(img).squeeze(0)
print('-----')
for idx in torch.topk(outputs, k=3).indices.tolist():
    prob = torch.softmax(outputs, -1)[idx].item()
    print('[{idx}] {label:<75} ({p:.2f}%)'.format(idx=idx, label=labels_map[idx], p=prob*100))


if max(torch.topk(outputs, k=3).indices.tolist()) == 664:
    print("고양이")
    pag.click(730, 577)

if max(torch.topk(outputs, k=3).indices.tolist()) != 664:
    print("모니터")
    print("보기에 정답이 없습니다.")

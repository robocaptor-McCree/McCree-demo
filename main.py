import json
from PIL import Image
import pyautogui as pag
import torch
from torchvision import transforms
import matplotlib.pyplot as plt#시각화를 위한 package
import torchvision.models as models


model = models.resnet101(pretrained=True)# Model로 ResNet-101버전 로딩
model.eval()

# Load class names
CLASSES = json.load(open('labels_map.txt'))
idx2class = [CLASSES[str(i)] for i in range(1000)]



img = Image.open('001.png').convert('RGB')
#img = Image.open('001_adv.png').convert('RGB')
# Preprocess image
# 이미지를 텐서로 변환하기
img_transforms = transforms.Compose([
    transforms.Resize((224, 224), Image.BICUBIC),
    transforms.ToTensor(),
])

img_tensor = img_transforms(img)
img_tensor = img_tensor.unsqueeze(0)

original_img_view = img_tensor.squeeze(0).detach()  # [1, 3, 244, 244] -> [3, 244, 244]
original_img_view = original_img_view.transpose(0,2).transpose(0,1).numpy()


output = model(img_tensor)
prediction = output.max(1, keepdim=False)[1]
#가장 확률이 높은 예측 클래스(prediction)

prediction_idx = prediction.item()
prediction_name = idx2class[prediction_idx]

print("예측된 레이블 번호:", prediction_idx)
print("레이블 이름:", prediction_name)


if prediction_name.find('panda') != -1:
    print("판다")
    pag.click(730, 577)

if prediction_name.find('panda') == -1:
    print("보기에 정답이 없습니다.")

plt.imshow(original_img_view)
plt.show()
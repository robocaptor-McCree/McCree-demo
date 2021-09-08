# McCree-demo

[![license](https://img.shields.io/github/license/robocaptor-McCree/McCree-demo.svg)](LICENSE)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

McCree의 매크로 공격 demo입니다.

McCree-web api 테스트 페이지의 매크로 차단 기능을 테스트합니다. 

Image classification은 resnet101 모델을 사용했습니다.

## Table of Contents

- [Install](#install)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Install

```
$ git clone https://github.com/robocaptor-McCree/McCree-demo
$ cd McCree-demo
```
## Usage

* main.py를 실행시키면 McCree-web api 테스트 페이지에서 이미지를 받아 image classification를 진행합니다.

  model은 resnet101을 사용합니다.

  image classification을 통해 사진이 어떤 class에 속해있는지 예측하고 보기와 비교하여 정답을 클릭합니다.

## Result

  * adversarial noise가 적용되지 않은 이미지를 사용하여 매크로 차단을 시도했을 때는 resnet-101이 판다 사진을 정확이 분류해내 로그인에 성공하는 것을 볼 수 있습니다. 

![origin_img](https://user-images.githubusercontent.com/51123268/132464437-6555d823-ace3-4b8e-b154-387564b30490.PNG)

![origin_result](https://user-images.githubusercontent.com/51123268/132464457-d0164ba0-4638-4e07-85a4-b3b3a945cb34.PNG)


  * adversarial noise가 적용된 이미지를 사용하여 매크로 차단을 시도했을 때는 resnet-101이 판다 사진을 langur로 분류해내 로그인에 실패하는 것을 볼 수 있습니다. 

![adv_fail](https://user-images.githubusercontent.com/51123268/132464462-111b06fd-1b57-4db7-a43a-d545abb71796.PNG)

## Contributing

This project exists thanks to all the people who contribute. 

![GitHub Contributors Image](https://contrib.rocks/image?repo=robocaptor-McCree/McCree-demo)


## License

[MIT © robocaptor-McCree.](../LICENSE)

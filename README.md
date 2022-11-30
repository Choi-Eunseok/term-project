# 1학년 1학기 웹/파이썬 프로그래밍 수업 텀프로젝트
### 2021
### 작동 기기, 파이썬 실행 프로그램
### 라즈베리 파이, 파이썬, 아두이노

## 라이다 센서와 카메라를 활용해 주위 환경 구현

#### 1. 프로젝트의 목표
라이다 센서와 카메라를 통해 360도 주위 환경 3D 구현

> 특정 각도 내의 거리들을 측정할 수 있는 라이다 센서를 활용하여서 주위 환경이 어떻게 되어있는지 입체로 만들어서 표현할 것입니다.
> 
> 무엇인가 튀어나온 부분이나 주위의 환경을 라이다 센서로 입체로 구현한 부분에 카메라로 사진을 찍은 것을 넣어서 3D로 구현하고 싶습니다.
> 
> 만약에 가능하다면 3D로 구현을 하고 사진으로 머신 러닝을 돌려서 그 중에 어떠한 사물들이 있는지 판단까지 할 수 있게끔 만들 것입니다.

#### 2. 내가 직접 구현한 부분에 대한 설명

> 첨부한 코드 중 거의 다 직접 구현했습니다.
> 
> 구현하고 싶은 것이 있으면 세세하게 나누어서 제가 구현할 수 있는 부분은 제가 찾고 새로운 라이브러리를 이용해야지 구현이 가능 할 수 있는 부분들만 인터넷에서 찾아서 사용했습니다.

> 프로젝트에서 코드를 짜다가 만약에 코드가 구현이 되지 않는 것 같으면 완전히 다른 방식으로 접근을 해보려고 여러 시도를 많이 했었습니다.

> 처음에는 라즈베리파이 하나로 모든 것들을 동작시키려 하였습니다.
> 
> 그러나 서보모터를 동작시킬 전력이 부족하고 카메라를 사용하기 위한 opencv를 사용하면 라즈베리파이가 힘겨워 하는 모습을 보였습니다.

> 그래서 다시 아두이노를 통해서 서보모터와 라이다 센서를 동작시키고, 아두이노가 어떤 동작을 할지와 사진과 관련된 코드는 파이썬으로 짜는 것으로 방향을 바꾸었습니다.
> 
> 그래서 파이썬과 아두이노를 통신시키는 법을 찾았습니다.

> 그 뒤에는 서보모터 동작시키고, 카메라로 사진 찍는 것까지 구현을 했었습니다.
> 
> 그러나 사진을 파노라마처럼 이으려고 opencv에 포함된 함수를 사용을 해보았습니다.
> 
> 그랬더니 사진이 어느정도는 잘 연결이 되었지만 몇몇 사진들은 연결이 완전히 안 될 때도 있고 아예 실패하는 경우가 너무 많았습니다.
> 
> 그래서 사진을 연결할 알고리즘을 만들었습니다.
>> 우선 사진을 흑백으로 바꿔 줍니다.
>> 
>> 연결할 사진 중 왼쪽 사진에서 일정한 크기의 끝부분을 numpy배열에 저장합니다.
>> 
>> 오른쪽 사진의 왼쪽부터 시작해서 그 크기와 같은 사이즈로 나누고 왼쪽부분의 끝과 비교를 합니다.
>> 
>> 그중 가장 일치하는 부분이 많은 위치가 오른쪽 사진의 시작 위치로 만들고 두 사진을 연결하는 알고리즘을 만들었습니다.
>
> 물론 opencv에서 제공하는 함수보다 정확도는 떨어지지만 시작위치를 탐색하는 범위를 잘 지정해주면 opencv보다 높은 정확성과opencv의 함수와 달리 실패하는 경우와 몇몇 사진을 빼고 연결하는 경우가 없기 때문에 이렇게 구현을 하였습니다.

#### 3. 결과

<div align="center">
<img width="40%" alt="image" src="https://user-images.githubusercontent.com/61959836/204772167-f1b83bd0-3bef-48b6-a935-2b3449c6956f.jpg">
<img width="40%" alt="image" src="https://user-images.githubusercontent.com/61959836/204771222-4adce2f1-3360-4684-ac5d-85969e7ebd98.jpg">
</br>
180도 돌 수 있는 서보모터를 360도 돌 수 있게끔 직접 3D모델링 하고 출력해서 만든 기어와 카메라, 라이다 센서 거치대
</br>
</br>
</div>

<div align="center">
<img width="40%" alt="image" src="https://user-images.githubusercontent.com/61959836/204772510-034561c2-dc73-4e60-b58e-67046d54a900.png">
<img width="40%" alt="image" src="https://user-images.githubusercontent.com/61959836/204772644-5b42de85-75c8-4930-9734-8744de9d184e.png">
</br>
</br>
</div>

<div align="center">
<img width="500" alt="image" src="https://user-images.githubusercontent.com/61959836/204772949-3a68a7ed-6e9e-4b05-a7e9-cfb3e0357e4c.png">
</br>
서보모터 돌리면서 사진 찍고 사진들 합체시키는 알고리즘의 플로우 차트
</br>
</br>
</div>

<div align="center">
<img width="90%" alt="image" src="https://user-images.githubusercontent.com/61959836/204773220-ba69f1e3-ede3-46d9-9851-41d94e878cd2.png">
</br>
파이썬 프로그램을 돌려서 나온 결과 ( 연결이 잘 되게끔 중간중간 모양을 그려넣음 )
</br>
</br>
</div>

<div align="center">
<img width="340" alt="image" src="https://user-images.githubusercontent.com/61959836/204774381-ff961bc0-b74b-4fb0-8bea-4411dde7225f.png">
</br>
크기가 큰박스안에 장치를 넣고 파이썬 프로그램을 돌려본 결과
</br>
(라이다 센서가 1cm를 기준으로 밖에 값이 나오지 않아서 많이 정확하지 않지만 어느정도 박스의 형태가 확인이 됨)
</div>


#### 4. 결론
> 이 프로젝트의 목표는 라이다 센서와 카메라를 통해 360도 주위 환경 3D 구현을 하는 것이었습니다.
> 
> 그러나 직접 하다 보니 계획서에 없던 문제가 엄청 많이 발견이 되어서 원했던 것 처럼 빨리 빨리 구현이 되지 않았습니다.
> 
> 그래서 제가 생각하기로는 원래 원했던 목표의 60~70% 밖에 완성한 것 같습니다.
> 
> 이 결과 보고서로 텀프로젝트는 끝이 나지만 저는 이 프로젝트를 계속하면 서 제가 원래 원했던 목표를 꼭 달성해 볼 것이고, 더 나아간 목표를 달성하기 위해서 계속해서 개발을 할 것입니다.

> 이때까지 아두이노로만 피지컬적인 프로젝트를 해보았습니다.
> 
> 그러나 이번에 파이썬을 사용하면서 아두이노에서는 구현이 불가능이라고 생각했던 것들이 파이썬에서 쉽게되는 것을 파악하였습니다.
> 
> 예를 들면 아두이노를 사용을 하면 아두이노의 램이 엄청나게 작기 때문에 배열이나 변수, for문의 제약이 있어서 정 안되면 아두이노 2개를 연결해서 해야 했습니다.
> 
> 그러나 파이썬을 사용하면 리스트를 만들 때 개수를 제한해두지 않아도 된다는 것에 가장 큰 기쁨을 느꼈습니다.
> 
> 그래서 앞으로 특정한 상황이 아니면 프로젝트를 하는 것에 파이썬을 사용해야겠다는 생각을 했습니다.

> 물론 파이썬을 사용하면 좋은 점이 많이 있지만 이번 프로젝트를 하면서 한가지 힘들었던 점이 있습니다.
> 
> 파이썬을 사용하지 않고 다른 언어를 사용하면 거의 다 스스로 작성을 하거나 외부 라이브러리를 사용을 해도 동작이 어디에서 멈추고 어디에서 오류가 나는지 잘 알 수 있었습니다.
> 
> 그러나 파이썬을 사용할 때 특히 외부 라이브러리에서 특정함수를 사용할 때 엄청나게 많은 과정을 다 생략을 해버리기 때문에 제가 잘못한 것인지, 그 함수에서 어떤 에러가 났는지 왜 함수가 정확하게 동작이 되지 않는지 알기가 어려웠습니다.
> 
> 사진을 연결시킬 때 opencv의 stitch함수를 사용했었는데 어떤 경우는 잘 동작하고 또 다시 동작시키면 함수가 연결을 못 시킨다고 하고, 어떤 때에는 그냥 몇몇 사진을 빼버리는 등 어떤 조건을 만족시켜줘야 하는지 잘 몰랐습니다
> 
> 물론 제가 그런 쪽으로 공부를 해보지 않아서 그럴 수 있습니다.
> 
> 그래서 앞으로는 함수를 정확하게 알고 사용을 할 노력을 해봐야겠습니다.

---

[발표 영상](https://drive.google.com/file/d/1yDE6jZlnTAm46LfAS6Udx50mb0KTW3bA/view?usp=sharing)


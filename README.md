# **AniAni-BEAM**

AniAni-Beam은 Image에 대한 Cartoon Rendering을 지원합니다.  
***cv2.adaptiveThreshold 함수***를 통해 edge로써 인식할 수 있는 범위를 설정하고  
**edge**를 __median filter__ 를 적용한 이미지와 **Bitwise_and** 연산을 통해 강조합니다.  

## **Good Case**
![good_image](https://github.com/park2722/AniAni-Beam/blob/main/README_image/good_case.png)

위와 같이 경계가 모호하지 않고, edge 부근의 색 변화가 극적일수록 잘 부각됩니다.

## **Bad Case**
![bad_image](https://github.com/park2722/AniAni-Beam/blob/main/README_image/bad_case.png)  
위 사진에서 벽의 모서리 부분과 고양이의 털과 벽의 색상이 유사한 경우에서 edge가 표현되지 않는 것을 확인할 수 있습니다.


# 결론 
위 단점을 해결하기 위해 threshold 범위를 조절하거나, filter의 형식을 바꾸어 시도해볼 수 있을 것입니다.



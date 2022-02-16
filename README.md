# 2021-2CAU_IOT_project_HalliGalli

앱 구동영상 : https://www.youtube.com/watch?v=l78M_DlpKc8
안드로이드 내부 Python 구동 : Chaquopy 오픈소스 사용
안드로이드 기기 녹음 음원파일 wav로 저장 : 옴레코더 오픈소스 사용
<img width="600" alt="스크린샷 2021-12-18 오전 12 04 52" src="https://user-images.githubusercontent.com/75043852/146564640-0804017c-6c4d-4265-aa53-d075a907e9e4.png">

<개요&동기>


<img width="600" alt="스크린샷 2021-12-18 오전 12 07 17" src="https://user-images.githubusercontent.com/75043852/146564981-0bf1ab32-8d9a-4ccf-a029-929611f05998.png">

<개발환경>
Android Studio & Pycharm (numpy, AudioSegment, scipy, pydub....   for Audio analysis & Filtering(fft) tasks)

<Band pass python code for filtering>
  
  
  <img width="600" alt="image" src="https://user-images.githubusercontent.com/75043852/146565345-ce393347-f321-4acc-b020-be74c796e5d6.png">

  <img width="600" alt="스크린샷 2021-12-18 오전 12 11 12" src="https://user-images.githubusercontent.com/75043852/146565541-8d1c1273-ebcd-4f6c-881f-623903424851.png">

<설명>
  
  <img width="600" alt="스크린샷 2021-12-18 오전 12 14 40" src="https://user-images.githubusercontent.com/75043852/146566031-39db2404-3237-4131-9319-46e74754b8ea.png"><img width="600" alt="스크린샷 2021-12-18 오전 12 15 10" src="https://user-images.githubusercontent.com/75043852/146566074-5e2e961b-ae08-4bd2-9f9e-e1147afc4016.png"><img width="600" alt="스크린샷 2021-12-18 오전 12 15 31" src="https://user-images.githubusercontent.com/75043852/146566121-724bf708-5ce7-4c12-a5e0-1a21992c0fc8.png"><img width="600" alt="스크린샷 2021-12-18 오전 12 16 18" src="https://user-images.githubusercontent.com/75043852/146566246-3b414699-8080-4cdf-a9c2-d00987de664c.png">

  -------------------------------------------------------------------------------------------------------------
  <img width="600" alt="스크린샷 2021-12-18 오전 12 17 01" src="https://user-images.githubusercontent.com/75043852/146566315-c4609a01-e180-467e-9c1e-5ff320a657ea.png"><img width="600" alt="스크린샷 2021-12-18 오전 12 17 18" src="https://user-images.githubusercontent.com/75043852/146566393-152a9327-6348-468f-864f-e66bd5372489.png"><img width="500" alt="스크린샷 2021-12-18 오전 12 18 18" src="https://user-images.githubusercontent.com/75043852/146566638-739c7b2f-3798-4692-a6db-f796df6fa98c.png"><img width="500" alt="스크린샷 2021-12-18 오전 12 18 54" src="https://user-images.githubusercontent.com/75043852/146566642-d2d9f639-b8c4-440a-80f9-1c3a29be0c7d.png"><img width="500" alt="스크린샷 2021-12-18 오전 12 19 11" src="https://user-images.githubusercontent.com/75043852/146566649-ff6c4046-68d1-4926-892a-e3f0fe3a24ca.png">
  -------------------------------------------------------------------------------------------------------------
  

<Android에 내장한 Audio Task Python파일 아키텍처>
  
경로 : Front/AudioRecord_final/AudioRecord/app/src/main/python/Split2Stereo&Filteringpy
  
![image](https://user-images.githubusercontent.com/75043852/146567299-5aafbb00-e71e-4d44-974f-6838f4b55c00.jpeg)
  
다음과 같은 Task를 수행하였다. 
  
  <img width="600" alt="스크린샷 2021-12-18 오전 12 24 30" src="https://user-images.githubusercontent.com/75043852/146567361-7038c605-32d7-420e-a4cf-8e1525e12b95.png">

  -------------------------------------------------------------------------------------------------------------  
  
<Audio 분서 예시>
   -------------------------------------------------------------------------------------------------------------  
  <img width="600" alt="스크린샷 2021-12-18 오전 12 36 45" src="https://user-images.githubusercontent.com/75043852/146569428-242b58d3-07d7-4eb7-8457-ffbad07d9644.png">
<img width="600" alt="스크린샷 2021-12-18 오전 12 36 57" src="https://user-images.githubusercontent.com/75043852/146569458-eafd68e3-4ecf-4ef7-bcfe-d1578b6d305b.png">
<img width="600" alt="스크린샷 2021-12-18 오전 12 37 32" src="https://user-images.githubusercontent.com/75043852/146569530-8d5155ea-e8e6-4612-b8c8-0e343555f71f.png">

  
   -------------------------------------------------------------------------------------------------------------  
  <img width="600" alt="스크린샷 2021-12-18 오전 12 30 06" src="https://user-images.githubusercontent.com/75043852/146568746-483c204e-9a93-42b4-80e0-5166845e338a.png">
  <img width="600" alt="스크린샷 2021-12-18 오전 12 30 33" src="https://user-images.githubusercontent.com/75043852/146568757-a7ba8e1f-647e-4567-a299-df183417a692.png">
  <img width="600" alt="스크린샷 2021-12-18 오전 12 31 08" src="https://user-images.githubusercontent.com/75043852/146568763-140c0cad-a9c6-4c10-9531-096ee4761488.png">
   -----------------------------------------------------------------------------------------------------------------
  <img width="600" alt="스크린샷 2021-12-18 오전 12 32 28" src="https://user-images.githubusercontent.com/75043852/146568863-0ff5f10b-fa8e-4773-a1bb-9f833c174bf6.png">
<img width="600" alt="스크린샷 2021-12-18 오전 12 35 10" src="https://user-images.githubusercontent.com/75043852/146569232-9478c8ca-0594-4425-8b31-36c04dc1c46d.png">
<img width="600" alt="스크린샷 2021-12-18 오전 12 35 48" src="https://user-images.githubusercontent.com/75043852/146569284-455d9042-3d56-4e2a-a568-b46961a39b8e.png">


  
  -------------------------------------------------------------------------------------------------------------  
<아키텍처>

Android + Python(Android기기 내부 구동) 별도의 서버X


![HalliGalli아키텍처](https://user-images.githubusercontent.com/75043852/145720601-6f381dd9-6cbe-4fd8-b43c-bc459bffe0ed.png)

 -------------------------------------------------------------------------------------------------------------  
<img width="600" alt="스크린샷 2021-12-18 오전 12 26 22" src="https://user-images.githubusercontent.com/75043852/146567667-959440cc-4ec7-422a-a83d-b2129b1635c5.png">

   -------------------------------------------------------------------------------------------------------------  
  <img width="600" alt="스크린샷 2021-12-18 오전 12 27 46" src="https://user-images.githubusercontent.com/75043852/146567895-2c9b5b72-2d48-4962-b19e-97da3e7113cc.png">

     -------------------------------------------------------------------------------------------------------------  
  <img width="600" alt="스크린샷 2021-12-18 오전 12 39 28" src="https://user-images.githubusercontent.com/75043852/146569837-bc37b4c1-8697-4c4a-af30-067b2e6fd696.png">

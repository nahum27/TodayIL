부스팅

Main boosting types

- Weight based
- Residual based



Weight based boosting

![weightbasedboosting](C:\Users\Geo\Desktop\Xgboost\이미지\weightbasedboosting.PNG)

![weightbasedboosting2](C:\Users\Geo\Desktop\Xgboost\이미지\weightbasedboosting2.PNG)

표적변수가 weight 컬럼을 생성하여 사용하게 된다. 

y := weight



Weight based boosting parameters

- Learning rate ( or shrinkage or eta)

> predictionN=pred0*eta + pred1*eta+...+predN*eta

- Input model - can be anything that accepts weights
- Sub boosting type:
  - AdaBoost - Good implementation in sklearn ( python)
  - LogitBoost - Good implementation in Weka (Java)

![Residual based boosting_0](C:\Users\Geo\Desktop\Xgboost\이미지\Residual based boosting_0.PNG)



모-델1를 통하여 예측값을 산출하고 예측값과 실제값의 차이(오차)를 만들어 낸다

![Residual based boosting](C:\Users\Geo\Desktop\Xgboost\이미지\Residual based boosting.PNG)



오차를 다시 예측하는 모델2를 만들어 예측값을 생성해 낸다. 

참조 레코드 : Rownum 1

Final prediction = 0.75 + 0.20 = 0.95



Residual based boosting parameters

- Learning rate ( or shrinkage or eta)

​       Prediction= 0.75 + 0.2 * (0.1) = 0.77

> 첫 모델의 예측값을 모델2의 오차 예측값의 영향을 10%받게 한다. 



- Number of estimators

> 많은 계산기를 사용한다는 건 꽤 중요하다. 그리고 올바른 학습 비율로 상쇄할 필요가 있다. 모든 모델이 올바를 기여를 하고 있음을 확실히 해야 한다. 

> 상호 검증을 기준으로 매개변수를 결정한다.



- Row (sub) sampling
- Colums (sub) sampling

- Input model - better be trees

- Sub boosting type : 

  - Fully gradient based

  - Dart

    > 나무의 기여를 제어하기 위해 낙하 메커니즘을 제공한다. 딥러닝에서 나온개념

  - 

Xgboost

Lightgbm

H20's GBM

Ctboost

Sklearn's GbBM





### Gradient Boost Part 1, Regression Main ideas

 https://www.youtube.com/watch?v=Gv9_4yMHFhI&list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF 
































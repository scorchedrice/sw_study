# PJT 2

### 이번 pjt 를 통해 배운 내용
- Jupyter Notebook의 편의성
- Pandas, Numpy, Matplotlib
- str으로 입력된 Date, Price를 변경하는 to_datetime(), to_numeric()
- csv 파일을 읽고 이를 해석하는 방법
## A. 데이터 전처리 - 데이터 읽어오기

#### 요구 사항 
- 데이터 전처리 (데이터 읽어오기)
- Pandas를 사용하고, Data, Open, High, Low, Close 필드만 읽어오도록 구성해야한다.
#### 결과 및 핵심 코드
```python
arr = file_open()
columns = arr[0]
arr = np.delete(arr, 0,0)
df = pd.DataFrame(arr, columns = columns)
df.loc[:, 'Date':'Close']
```

- 이 문제에서 어려웠던점, 핵심 포인트 : 익숙하지 않은 데이터 유형, 그냥 불러온다면 의도와 다른 형식으로 데이터를 불러올 수 있기에 위의 과정이 필요함.

-----

## B. 데이터 전처리 - 2021년 이후의 종가 데이터 출력

#### 요구 사항
- 2021년 이후 종가(Close Price)를 plot 해야한다.
- title, xlabel, ylabel, xtricks를 예시처럼 나오도록 해야한다.

#### 결과 및 핵심 코드
```python
new_data = df[pd.to_datetime(df['Date']) > pd.to_datetime('2020-12-31')]
x = list(pd.to_datetime(new_data['Date']))
y = list(pd.to_numeric(new_data['Close']))
```

- 이 문제에서 어려웠던점, 핵심 포인트 : 처음엔 날짜 양식을 구분하는 것이 어려웠다. to_datetime()을 활용하면 str이 datetime64 형식으로 바뀐다는 것을 알았으나, 이를 구체적으로 어떤식으로 비교해야할지 고민했다. 그 결과 21년 직전날짜인 20년 마지막 날을 to_datetime()을 적용해 그보다 큰 값을 21년으로 두었고 이를 통해 날짜를 구분할 수 있었다.
이를 해결한 이후 그래프를 그리는 것도 어려웠다. 기본적으로 그래프를 plot하기 위해선 일대일 대응이 되어야 했지만, 새로운 기준으로 수가 줄어든 'Date'는 'Close'의 데이터보다 양이 적어 일대일 대응을 만족할 수 없었다. 이를 해결하기 위해 A번에서 활용한 df를 해당 기준을 적용한 상태로 그대로 받아온 이후, 이를 new_data로 다시 정의했다. new_data에서 이를 각각 to_datetime, to_numeric을 적용해 그래프를 그릴 수 있는 타입으로 전환하고 이를 리스트로 바꿔 plot했다.



-----
## C. 데이터 분석 - 2021년 이후 최고, 최저 종가 출력

#### 결과 및 핵심 코드
```python
price_list = list(pd.to_numeric(new_data['Close']).sort_values())
max_value = price_list[-1]
min_value = price_list[0]
```

- 이 문제에서 어려웠던점, 핵심 포인트 : 크게 어려운 문제는 아니였다. B에서 새로 정의한 new_data는 문제에서 주어진 '21년 이후'라는 조건을 만족하기에 이를 활용했다. new_data의 'Close'에 해당하는 값들을 .sort_values()를 적용해 오름차순으로 배열하는 리스트를 만들었고, 첫 index와 마지막 index를 각각 min_value, max_value로 할당했다.

-----
## D. 데이터 분석 - 2021년 이후 월 별 평균 종가 출력하기

#### 요구 사항 
- 월별로 평균 종가를 계산해 이를 plot하기

#### 결과 및 핵심 코드
```python
new_data['Date'] = pd.to_datetime(new_data['Date'])
new_data['Close'] = pd.to_numeric(new_data['Close'])
grouped = new_data.groupby(pd.Grouper(key='Date', freq = 'M'))
mean_month = grouped['Date'].mean()
mean_close_price = grouped['Close'].mean()
```

- 이 문제에서 어려웠던점, 핵심 포인트 : 월별 평균값들을 구하고 이들이 일대일 대응을 만족할 수 있도록 하는 과정이 어려웠다. 우선 월별로 구분하는 것이 쉽지 않았다. 처음엔 1월부터 12월까지 범위를 지정해 분류하는 것을 생각했으나, 문제의 의도와 맞지 않다 생각하여 다른 방법을 찾았다. groupby()함수를 적용하는 것이 이 문제의 핵심이라 생각해 이를 활용했다. Grouper과 같은 함수를 검색을 통해 찾아냈고, 이를 사용했다.
더불어 일대일 대응을 만족하는 쌍을 만들기 위해 그룹된 값들의 평균을 구했다. 날짜도 평균을 구했으며 (2월의 평균은 2월 14일) 이들을 Close의 평균값과 일대일 대응시켜 plot했다.

-----
## E. 데이터 시각화 - 2022년 이후 최고, 최저, 종가 시각화

#### 요구 사항 
- 2022년 이후의 최저, 최고, 종가를 시각화 할 것.
- 예시의 그래프 양식처럼 plot 할 것.

#### 결과 및 핵심 코드
```python
new_data = df[pd.to_datetime(df['Date']) > pd.to_datetime('2021-12-31')]
new_data['Date'] = pd.to_datetime(new_data['Date'])
new_data['Close'] = pd.to_numeric(new_data['Close'])
new_data['High'] = pd.to_numeric(new_data['High'])
new_data['Low'] = pd.to_numeric(new_data['Low'])

plt.plot(new_data['Date'], new_data['Low'], color='orange')
plt.plot(new_data['Date'], new_data['Close'], color = 'green')
# ...
```

- 이 문제에서 어려웠던점, 핵심 포인트 : 새로운 날짜 조건이 정해졌으니 new_data를 다시 정의해야 했다. 더불어 그래프를 여러개 그려야 했기에 각각 y축에 plot될 값들을 plot이 가능한 타입으로 변환하는 과정이 필요했다. 이 과정을 거친 후 조건에 맞춰 plot하기 위해 legend 추가, 색상 조건을 추가하여 plot했다.

# 후기

* csv파일 등 다양한 데이터들을 받고 이를 활용하기 위해선 가공이 필요하다는 것을 알게되었다.
* 검색하는 것도 능력이란 것을 알게되었다. 특히 groupby()를 활용하는 방법을 자세히 몰랐으나, 이를 검색하고 적합성 여부를 판단하는 능력이 중요하다는 것을 깨달았다.
* 검색을 통해 얻은 정보를 활용하기 위해선, 기본적인 프로그래밍 지식이 필요하다 생각한다. 지속 학습해 해당 역량을 키워야겠다.
* Jupyter notebook이 정리하기도 편한 것 같다. 다음엔 이를 활용해서 정리를 해봐야겠다.
# PJT 생성
1. 파일 => 터미널에서 npx create-react-app PJTNAME (project 생성 라이브러리 활용 <node.js 활용>)
2. 프로젝트 실행: VScode 터미널에서 npm start

# 파일 설명
- node_modules: 라이브러리 코드 보관함이라 보면 된다.
- public: html, img 파일 저장 .. static 파일 저장 공간
- src: 소스코드 보관함 (App.js에 메인 페이지 내용이 작성된다고 이해 (App.js =>index.js => index.html))
- package.json: PJT 버전, 라이브러리 명 등

# JSX 문법
- React는 App.js 내부에서 html문법을 사용하는데, 이를 JSX라고 한다. 
- jsx를 사용하면 더 간결한 코드 작성 가능
```jsx
import React from 'react';

const Book = (props) => {
    return (
        <div>
            <h1>{`이 책의 이름은 ${props.name}입니다.`}</h1>
            <h2>{`이 책은 총 ${props.numOfPage}의 페이지로 구성되어 있습니다.`}</h2>
        </div>
    );
}

export default Book;
```
------------------
- class는 className이라고 작성해야 한다. (javaScript의 문법 class와 충돌하기에)
- 데이터바인딩: 변수를 사용하고 싶다? {}을 사용
    - front가 하는 주 업무. 서버로 부터 값을 받고 표시
    - style을 적용할때 데이터바인딩 을 사용해야 한다. {{}}
    ```react
    <p style={{ color: 'red', fontSize: '16px'}}>js에서 - 기호는 사용할 수 없으니 font-size가 아닌 fontSize</p>
    ```

# React Element
- 리액트를 구성하는 가장 작은 블록들
- 한번 생성되면 바꿀 수 없다.

# State
```react
import {useState} from 'react';
```
- 값이 자주 변경될 것 같은것들 (값이 변경될 때 반영되는 것이 필요한 것들)에 사용
- useState('값 입력')으로 값을 저장하면 [값, 함수] 꼴로 저장되기에 [호출할 때 사용할 변수명, 함수명] 꼴로 상단에 정의 필요

# eslint-disable
- warning (경고) 제거 목적
- 알고만 있자 일단은

# Event
- 이벤트 = {함수} 꼴로 삽입해야함.
    - 상단에 함수를 정의하거나
    - () => { 함수 내용 }, function () { 함수 내용 } 꼴로 진행 가능
        - 일정 값에 함수 값을 적용해 실시간 반영하고 싶다면?
        - [변수명, 변수함수] = useState(값) 꼴에서 변수함수를 활용
            - 변수함수를 사용한다하고 소괄호 내부에 변경 명령 삽입
    - 값을 변경할 때 원본을 보존하는 습관 좋음
        - 함수 내부에 let copy로 값을 복사 한 뒤 그 값을 바꾸는 방향으로 진행

# State변경함수 특징
- state에 변화가 없다면, 새로 저장하지 않는다.
- Array/Object의 경우 화살표만 저장이 된다 (어디에 저장되어 있는지만 알고 있음), 그래서 그냥 변경을 한다면 화살표는 변경되지 않다고 판단하기에 주의해야한다.
    - [...Array]를 통해 화살표를 바꾸고 새로운 사본을 만들어야 한다.
        - ...로 괄호를 벗기고 []로 다시 씌운다.

# Component
- Vue와 동일하게 복잡한 구성인 경우 활용하면 좋겠지?
    - 반복적인 html 축약, 큰 페이지, 자주 변경되는 것들에 적극 활용
- function을 만들어서 사용한다 (대문자로 시작하는 함수 정의, 함수 밖에서 정의해야함)

# Props
- Read-Only!
- 문자열 외 정수 변수등이 들어갈 땐 {}로 감싸주어야 한다.

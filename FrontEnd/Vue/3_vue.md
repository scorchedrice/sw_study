# Router

## router/index.js
- 라우팅 관련 정보 작성
  - url path, 사용할 component(View파일), name

## RouterLink , RouterView
- RouterLink를 통해 URL 변경
  - ```html
    <RouterLink :to="{name: 'home'}">Home</ RouterLink>
    ```
- RouterView : 해당 URL에 맞게 렌더링

## 매개변수를 활용한 동적 경로 라우팅
1. 콜론 사용! index.js의 경로 설정
```js
// index.js
// ...
  path: '/user/:id'
// ...
```
2. :id 값을 어디서 받아와야 할까? RouterLink의 params 에서 받아오자. 단, index.js에서 지정한 매개변수 (id)와 객체의 key가 동일해야 한다.
```html
<RouterLink :to="{name: 'user', params: {'id':userId} }">User</RouterLink>
```
- 이 라우터링크를 타고 간 컴포넌트에서 {{ $route.params }} 로 params 값에 접근 가능
- 

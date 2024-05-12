# Single Page Application (SPA)
- 하나의 HTML파일로 시작해, 사용자가 상호작용할 때마다 새로고침 없이 필요한 부분만 동적 갱신
  - CSR방식
## Client-side Rendering (CSR)
- 클라이언트 화면을 렌더링 하는 방식으로, 서버에서 제공받은 JavaScript을 활용해 클라이언트 측에서 DOM을 업데이트!
  - 이를 활용해 서버는 필요한 데이터만 응답해 새로고침 없이 렌더링 가능.
- 장점
  - Front, Back 명확한 분리
  - 주고 받는 데이터 최소화, 사용자 경험 개선 및 빠른 페이지 전환 (새로고침 없음)
- 단점
  - 느린 초기 로드 속도
  - SEO문제
    - 검색엔진 입장에선 HTML을 분석해야 하는데, 페이지를 나중에 그려 나가는 것이기에 쉽지 않음.

# Vue 사용 방법
1. Vue 설치 (CDN or npm)
2. Vue를 불러오기
```js
<script>
  // 기본 양식
  const {createApp}=Vue
  const app = createApp({
    setup() {
      return {
        // return하고 싶은 값
      }
    }
  })
</script>
```
3. 작성 후 {{ return된 값 }}을 통해 렌더링
  - JavaScript 사용 가능

# Template Syntax
- {{}} : 데이터 바인딩의 기본
- v-html="rawHtml" : html출력
- v-bind:id="linkedId" : html의 id 속성을 vue의 linkedId 속성과 동기화
- JavaScript Expressions

# Directive
- 표현식 값이 변경될 때, DOM에 반응적으로 업데이트를 적용

## v-bind
```html
<a v-bind:href="myUrl">Move to url</a>
<p :[key]="value"><p>
```
- html의 속성값을 vue 상태의 속성값과 동기화
- :으로 v-bind 생략 가능
- []으로 감싸 key로 활용가능
  - 단, 이때는 소문자로 작성해야 html이 인식하기에 주의
## v-on
- 이벤트 리스너 연결 및 수신
```html
<button @click="callBack()">Example</button>
```
- @로 생략 가능
- prevent, stop, self등의 modifier 존재 (. 뒤에 이를 붙혀 활용)

## v-model
- v-model : v-on(input) + v-bind (양방향 바인드)
  - 한글의 경우 한글자를 완전이 쳐야 v-model이 적용됨. 이 경우엔 v-on + v-bind로 처리 가능 (Input Method Editor <IME> - 비영어권 입력 운영 체제 구성 프로그램 차이)
- v-model은 단순 Text-input 뿐 아니라 Checkbox, Radio, Select 등 다양한 타입에 사용자 입력 방식과 함께 사용 가능

# computed()
- 계산된 속성을 정의하는 함수, 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게! 불필요한 연산 감소!
```js
const {createApp, ref, computed} = Vue

const restOfTodos = computed(() => {
  return todos.value.length > 0 ? "아직남았다" : "퇴근!"
})
```
- 물론 function을 통해도 구현 가능하다.
```js
const getRestOfTodos = function () {
  return todos.value.length > 0 ? "아직남았다" : "퇴근!"
})
```
- 그렇다면 두개의 차이가 도대체 뭔데?
  - computed는 의존된 반응형 데이터를 기밥ㄴ으로 캐시(cached)된다. 따라서 의존하는 데이터가 변경된 경우에만 재평가 된다. (변경되지 않는다면, 다시 평가할 필요 없이 이전 연산 결과 반환)
    - Cache : 데이터나 결과를 일시적 저장하는 임시 저장소
  - 즉, method 호출은 렌더링마다 항상 함수를 실행하기에 이 점이 차이.
  - 정리하자면, computed는 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용하며, method는 특정 단순 동작을 수행하는 함수를 정의할 때 유용하다.
    - 적절한 조합 중요!
## computed의 반환값, 변경 금지!
- 왜? computed의 반환값은 의존하는 데이터의 파생된 값으로, 일종의 snapshot이다. 계산된 값은 읽기 전용으로 취급되어야 하며 변경되어선 안된다
- 변경하고 싶으면 복사본을 만들고 하자.
# v-if
- true : 보여요, false : 안보여요
- v-else, v-else-if 모두 적용 가능

# v-show
- 표현식 값의 true/false를 기반으로 요소의 가시성을 전환
- CSS display 속성 전환 (none <=> )

## v-if, v-show의 사용처 차이
- v-if : Cheap intial load, expensive toggle
  - 토글 비용이 높다! 초기 조건이 false인 경우, 아무 작업 하지 않음
- v-show : Expensive initial load, cheap toggle
  - 토글 렌더링 비용이 높다! (초기 조건에 상관없이 렌더링)
- 즉, 자주 전환하는 경우엔 v-show, 실행 중 조건이 변경되지 않는 경우 v-if

# v-for
- Object의 반복
- key를 함께 사용해야 한다! (내부 컴포넌트 일관성 유지 및 데이터 예측 가능한 행동 유지)
  - key는 number 혹은 string으로만 사용해야 한다.
## v-for을 사용할 때, method 주의!
- 배열을 변화시키는 method 주의 (sort, reverse, push ...)
- computed를 통한 새로운 리스트 활용, method를 통한 필터링/정렬 활용 등으로 극복.
## key값으로 배열의 index 사용 금지!
- 배열의 항목 위치를 나타내는 것이 index, 식별자가 아님!
- 만약 새로운 값이 배열의 끝이 아닌 위치에 삽입된다면?
- 따라서 직접 고유한 값을 만들어내는 메서드를 만들거나, 외부 라이브러리 등을 활용하는 등 식별자 역할을 할 수 있는 값을 만들어 사용할 것!
## v-if와 v-for은 함께 사용하지 말 것
- 왜? 동일한 요소에서 v-if가 v-for보다 우선순위가 더 높기 때문에!
- v-if에서의 조건은 v-for 범위의 변수에 접근할 수 없다!
- 이를 해결하기 위해선 computed사용, v-for와 <template> 요소 활용
### computed를 활용한 문제 해결
- computed로 필터링 된 목록을 반환하고 이를 출력하는 방식
```js
const completeTodos = computed(() => {
  return todos.value.filter((todo) => !todo.isComplete)
})
```
```html
<li v-for="todo ini completeTodos" :key="todo.id">
  {{ todo.name }}
</li>
```
### <template> 활용한 문제 해결
```html
<template v-for="todo in todos" :key="todo.id">
  <li v-if = "!todo.isComplte">
    {{ todo.name }}
  </li>
</template>
```

# watch()
- 하나 이상의 반응형 데이터를 감시, 감시하는 데이터가 변경되면 콜백함수 호출
```js
const count = ref(0)
watch(count, (newValue, oldValue) => {
  console.log(`newValue: ${newValue}, oldValue: ${oldValue}`)
})
// 버튼을 누를때마다 count가 1씩 증가하는 경우
// newValue: 1, oldValue: 0
// newValue: 2, oldValue: 1 이렇게 출력
```
- 이를 활용해, 감시하는 변수가 변화했을 때, 연관 데이터를 업데이트 하는 함수를 꾸릴 수 있겠다.
- 여러가지를 source를 감시하는 watch예시는 다음과 같다.
```js
watch([foo,bar],([newFoo,newBar],[prevFoo,prevBar]) => {
  // ...
})
```

## computed와 watch의 공통점
- 원본 데이터를 변경하지 않는다.
- 데이터의 변화를 감지하고 처리한다.

## 차이점
- 동작
  - computed는 의존하는 데이터 속성의 계산된 값을 반환하고, watch는 변화를 감시한 후 작업 수행 (side-effects)
- 사용 목적
  - computed는 계산된 값 캐싱하여 재사용 (중복 방지), watch는 데이터 변화에 따른 작업 수행
- 사용 예시
  - computed : 연산된 길이, 필터링 된 목록 계산, watch : DOM 변경, 다른 비동기 작업 수행, 외부 API 연동 등

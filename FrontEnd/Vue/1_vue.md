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


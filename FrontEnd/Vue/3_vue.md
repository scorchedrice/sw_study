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
- 또, import {useRoute} from 'vue-router' => const userId = ref(route.params.id) 이후 userId로 접근가능! (권장)

## children option (nested component)
- 중첩된 라우터 활용할 때 사용
```js
// example
{
  path: '/user/:id',
  name: 'user',
  component: UserView,
  children: [
    {path: 'profile', name: 'user-profile', component: UserProfile},
    {path: 'posts', name: 'user-posts', component: UserPosts}
    // profile, posts는 user내부에 들어가고, 중첩되어있다!
    // RouterLink도 children의 name을 향하게 하면 된다.
  ]
}
```

# router.push(), router.replace()
## router.push()
- 다른 URL로 이동하는 메서드로, 새 항목을 history stack에 push 하므로 뒤로가기 버튼을 클릭하면 이전 URL로 이동 가능
- RouterLink :to ... 작동할 때 내부적으로 호출하는 메서드
```js
import {useRoute, useRouter} from 'vue-router'
const router = useRouter()
const goHome = function() {
  router.push({name: 'home'})
}
```
## router.replace()
- history stack에 새로운 항목을 push하지 않고 다른 URL로 이동 (뒤로가기 불가능!)

# Navigation Guard
- Vue router을 통해 특정 URL에 접근할 때, 다른 URL로 redirect를 하거나 취소하여 내비게이션 보호
- Globally(전역가드), Per-route(라우터 가드), In-component(컴포넌트 가드) 존재

## Globally Guard
- 애플리케이션 전역에서 동작하는 가드
- index.js 작성
### router.beforeEach()
- 다른 URL로 가기 직전에 실행되는 함수
```js
// index.js

router.beforeEach((to,from) => {
  console.log(to)
  console.log(from)
  // to에는 이동할 경로가, from엔 현재 경로가 담겨있어요.
})

export default router
```
- 이를 활용해서 로그인이 되어있지 않는 경우 강제로 로그인 페이지로 이동시키는 등 작동 가능

## Per-route Guard
- 특정 라우터에만 동작하는 가드
- index.js의 특정 라우터에 작성
### router.beforeEnter()
- 특정 route에 진입했을 때만 실행되는 함수
  - 특정 url의 매개변수나 쿼리값이 변경될때는 작동 X, 오로지 다른 URL에서 탐색해올 때 실행됨
- 이를 활용하면 로그인 상태로 로그인 창에 접근할 때, 이를 막는 기능을 구현할 수 있겠다.

## In-component Guard
- 특정 컴포넌트 내에서 동작
- 각 컴포넌트의 js에 작성

### onBeforeRouteLeave()
- 다른 라우트로 이동하기 전 실행
- 현재 페이지를 떠나는 동작에 대한 로직 처리
  - 정말 떠나실 건가요? 와 같은 기능 구현 가능

### onBeforeRouteUpdate()
- 이미 렌더링 된 컴포넌트가 같은 라우트 내에서 업데이트 되기 전 실행
- 라우트 업데이트 시 추가적인 로직 처리
  - id값이 다른 사용자의 profile로 이동하는 경우 사용 가능 (같은 컴포넌트, 다른 :id값)
  - 이 경우, onBeforeRouteUpdate에서 userId를 갱신해야!! (컴포넌트가 재사용 되었기에)

# State Management
- 상태관리의 단순성을 유지하기 위해 => 저장소 활용 (pinia)

# Pinia
- Vue 공식 상태 관리 라이브러리

## Pinia의 구성요소
- store
- state
- getters
- actions
- plugin
```js
// example, stores/counter.js
import {ref,computed} from 'vue'
import {defineStore} from 'pinia'

// store 정의 (중앙 저장소 정의), use ... Store 로 반환 값 이름 설정 권장
// defineStore의 첫번째 인자는 애플리케이션 전체에 걸쳐 사용하는 store의 고유 id
export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  // state, 반응형 상태 (데이터)
  const doubleCount = computed() => count.value * 2
  // getters (계산된 값)
  const increment = function () {
    count.value++
  } // actions, 메서드
  return {count, doubleCount, increment}
}
```
## store 접근 방법
```js
// App.vue
import {useCounterStore} from '@/stores/counter'
const store = useCounterStore()
console.log(store.count) // state 접근
console.log(store.doubleCount) // getters 접근

// store.increment() ... action 호출
```

## add
- add
```js
// pinia의 action
const addTodo = function (todoText) {
  todos.value.push({
    id: id++,
    text: todoText,
    isDone: false,
  })
}  
```
- 이후 양방향 바인드, 제출시 이벤트 발생 등 활용해 addTodo 작동
## delete
- 이벤트가 발생할 때, 하단의 함수가 todo.id라는 변수를 가지고 실행될 수 있도록 조치
```js
// pinia의 action
const deleteTodo = function (todoId) {
  const index =  todos.value.findIndex((todo) => todo.id === todoId)
  todos.value.splice(index,1)
}
```
## 횟수 세기
- computed 활용 (getters)
```js
const doneTodosCount = computed(() => {
  const doneTodos = todos.value.filter((todo) => todo.isDone)
  return doneTodos.length
})
```

# Local Storage
- 브라우저 내에 key-value 쌍을 저장하는 웹 스토리지 객체
- 새로고침하고, 브라우저를 다시 시작해도 데이터 유지
- 쿠키와 달리 네트워크 요청 시 서버로 전송되지 않음.
- 여러 탭, 창 간 데이터 공유 가능
- => 이게 다 사용자 경험 개선을 위함 (성능 개선 등)

## pinia-plugin-persistedstate
- pinia의 local storage / session storage 영구 저장 복원 기능 제공

### pinia-plugin-persistedstate 설정 과정
1. npm i pinia-plugin-persistedstate
2. main.js에 다음과 같은 내용 추가
```js
// main.js
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

// app.use(createPinia())
app.use(pinia)
```
3. defineStore() 인자 추가
```js
// stores/counter.js
...
  return {....}, {persist: true})
```

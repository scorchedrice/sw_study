# Using App Router vs. Using Pages Router
- 기존 pages router 의 단점 => app router으로 보안
    - 물론 완벽하진 않음. 실험적인 기능 많고, 버그 있고 ...
    - 권한 문제 쉽게 활용 가능
    - React 18에서 서버 컴포넌트가 들어왔는데, 이를 적극 활용 가능.

# 프로젝트 생성
- npx create-next-app@latest
    - TypeScript, EsLint, src, App Router : Yes

# 프로젝트 구조 설명
- public : next 서버에서 **누구나** 접근할 수 있도록 하는 것들이 저장됨.
- src - app : 주소와 관련된 파일들이 저장됨.
- src까지의 절대경로는 @로 사용 가능하다 (추후 import 시 사용)

# 폴더명에 사용하는 [], ()
- [] : /read/1, /read/2 처럼 유동적인 주소 할당
- () : 주소에는 직접 관여하지 않음! 정리할때/그룹화할때 사용

# layout.tsx, page.tsx, template.tsx
- 우선 layout, page를 통해 re render 없는 페이지 전환을 할 수 있다.
    - page의 내용이 layout의 children으로
- 근데, rerender을 원한다? template!
- layout과 template는 공존하지 말것

# next js에서 최적화된 이미지를 사용하는 방법
- import Image from "next/image";를 사용하고
- import zLogo from '../../public/zlogo.png'; 내가 원하는 이미지를 가져와서 사용하면 알아서 최적화 시켜준다!

# module.css
- 해당 page에서 css를 사용할 때 사용 (상속 관련 고려 x, ~~.module.css를 만들고 여기서 가져오는 형태)

# Parallel Routes
- page.tsx를 둘 다 띄우고 싶다면? (하나는 배경 역할)
- **같은 파일내에 있어야 parallel을 활용 가능하다!**
```tsx
// @modal 파일을 만들고 이를 활용한다.
```

# Intercepting Routes
- 서로 주소가 다르더라도 같이 표시될 수 있도록..
- (.)i 처럼 앞에 (.)를 붙혀 활용한다.
    - (..), (.) 둘다 사용 가능한데, (..)의 경우 브라우저 주소를 기준으로 부모를 찾아감.
        - (beforeLogin), @modal 과 같이 주소에 관련 없는 것들 스킵한다는 말
    - 그냥 i와 같이 있는경우 (.)i가 가로챈다.
        - 그렇다면 그냥 i 파일에 있는 page는 무의미한가?
            - No. url로 직접 접근하는 경우, 새로고침엔 i파일의 page가 랜더링
        - 정리하자면 Link로 접근 => Intercept, 그 외는 작동 X

# Intercepting Routes + Parallel Routes
- 이를 활용하면 메인 페이지가 뒤에 있고 로그인 모달이 떠있는 모양 구현이 가능하다.

# 서버 컴포넌트와 클라이언트 컴포넌트 차이?
- react는 원래 브라우저(클라이언트) 에서 작동되지만, NextJS의 layout, page는 서버에서 작동한다. 즉, 넥스트 서버에서 미리 랜더링 후 완성된 html을 보낸다는 것. (클라이언트 부담 낮추지만 서버 부담 커짐, 이를 서버에서의 캐시처리를 통해 완화)
    - 서버에서 작동하면 async .. 비동기를 사용할 수 있음.
    - 서버 컴포넌트는 useState, useEffect와 같은 Hook 사용이 어려움
        - 사용하기 위해선 client컴포넌트로 바꿔야함
            - 'use client'를 맨 위에 작성하면 바뀜

# Private folder (_폴더명)
- 주소창에 안나온다!

## 주소창에 안나오는 폴더 모음
1. (group folder)
- 그룹화할때 사용, 해당 폴더에 layout.tsx를 작성할 수 있다.
2. @parallel_route
- 한 화면에 두가지 표시 용도
3. _private folder
- 공통된 component 정리용
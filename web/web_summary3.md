# CDN
- 서버와 사용자 사이의 물리적 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화 (웹 페이지 로드 속도를 높임)
- 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달
- 쉽게말해 가까운 지역의 데이터를 가져와 대기시간 감소

# Reset CSS가 필요한 이유
- 브라우저마다 user agent stylesheet를 가지고 있다. bootstrap이 reset css를 사용하는 이유는 다른 브라우저를 사용하더라도 동일한 화면을 표시해야 하기 때문이다.
## Normalized CSS
- Reset CSS 방법 중 하나. 브라우저 별 차이점을 최소화 하여 동일하게 하는 것

# Bootstrap 사용 이유
1. 많이 사용되는 CSS 프레임워크
2. 사전에 디자인된 다양한 컴포넌트 및 기능 : 빠른 개발 및 유지보수 가능
3. 커스터 마이징 용이, 크로스 브라우징 지원
4. 손쉬운 반응형 웹 디자인

# Semantic Web
- 웹 데이터에 의미를 부여하는 것
    - 태그의 목적을 알 수 있도록 함
- 시멘틱 태그를 활용해야 검색 엔진 최적화 가능
- header, nav, main, article, section, aside, footer ... 사실 div와 기능 똑같지만 목적을 알 수 있기 위해!

# OOCSS
1. 구조와 스킨을 분리
2. 컨테이너와 내용물을 분리

# HTML과 CSS의 책임과 역할
- HTML : 콘텐츠의 구조와 의미
- CSS : 레이아웃과 디자인

# Bootstrap Grid system
- 레이아웃을 조정하는데 사용되는 12개의 컬럼으로 구성된 시스템
- 반응형 디자인을 지원해 다양한 기기에서 적절하게 표시할 수 있도록 도움
- Container > row > col 으로 구성
- 한 container에 row는 여러개 존재할 수 있다. (Nested, 몇대몇으로 나누고, 우측을 또 몇대몇으로 나누고 ...)
- offset을 활용한다면 나눌 때, 빈 칸을 적용할 수 있다. (col-4인 box, col-4 off set-4인 box 이런식으로 활용 가능)

## Gutter
- row에 아래의 값을 이용해 값을 조절할 수 있다.
- gx-'숫자' : padding
- gy-'숫자' : margin
- g-'숫자' : padding + margin


# Grid system breakpoints
- xs, sm, md, lg, xl, xxl
- col-md-8 이런식으로 해당 사이즈 영역일 때 8칸을 차지하도록 조건을 걸 수 있음.
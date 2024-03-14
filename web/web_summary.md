# Web
## CSS
- Inline style (직접 입력), Internal style sheet (head에 style 항목 생성), External style sheet (css 파일 활용)
- Inline방식은 지양한다.
- 클래스와 아이디 둘 다 사용 가능하지만, 클래스를 중심적으로 사용한다.
- HTML은 오류를 나타내지 않으므로 주의하고 작은 따옴표 대신 큰 따옴표를 사용하자.
### CSS-우선순위(Specificity)
```
명시도 순위
1. Importance
    - !important
2. Inline style
3. Internal style sheet
    - id > class > 요소
4. 소스코드 선언 순서
```
- 위 같은 우선순위가 혼합되는 경우, 불편함을 가져올 수 있기에 class를 중심적으로 사용한다.
#### Example - 우선순위
```html
<head>
    <style>
        /* 요소 선택자 */
        p {
            color: blue;
        }
        /* id 선택자 */
        #red {
            color: red;
        }
        /* 첫번째로 선언된 class */
        .orange {
            color: orange;
        }
        /* 두번째로 선언된 class */
        .green {
            color: green;
        }
        /* Importance */
        h1 {
            color: darkviolet !important;
        }
    </style>
</head>

<body>
    <h1 class="orange" id="red" style="blue">그 어떤 것도 Importance를 이길 수 없습니다.</h1>
    <p>요소 선택자의 영향을 받습니다.</p>
    <!-- Blue -->
    <p id="red" class="orange">id가 우선순위가 더 높습니다.</p>
    <!-- red -->
    <p style="color: brown;" id="red">Inline style의 우선순위가 더 높습니다.</p>
    <!-- brown -->
    <p class="orange green">우선순위가 동일해 green이 적용됩니다.</p>
</body>
```

### CSS 상속
- 상속을 통해 재사용성을 높일 수 있습니다.
#### 상속 가능 속성
1. Text관련 요소(font, color, text-align)
2. opacity
3. visibility

    그 외 기타
#### 상속 불가능 속성
1. Box model 관련 요소(width, height, border, box-sizing ...)
2. position 관련 요소(position, top/right/left/bottom/left ...)
    그 외 기타

**상속 여부는 MDN문서에서 확인 가능하다.**

**전부 암기하는 것은 불가능하니, Box model 및 Position 관련 요소를 제외하곤 상속될 가능성이 높다고 판단하자.**


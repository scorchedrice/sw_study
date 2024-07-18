# flutter 학습 시작 - 24.07.10

## Dart 문법
### Hex값 (16진수)를 전달하는 방법
- String으로 값을 받고 OxFF + "HexCode"를 정수로 전환
- 

## Flutter 구조
- 전부 암기하는건 불가능하다! 공식문서 / IDE의 추천 등 적극 활용하는 능력을 길러야
1. Widget 생성
   - Stateful? stateless? 이에 따라 다른 문법 사용
     Stateful : 일정 동작마다 값이 변화해야하는 경우 사용.
```dart
// stateful
import 'package:flutter/material.dart';

class SelectButton extends StatefulWidget {
  const SelectButton({
    super.key,
    required this.width,
    required this.height,
    required this.innerButton,
  });

  final String innerButton;
  final double width;
  final double height;

  @override
  State<SelectButton> createState() => _DayButtonState();
}

class _DayButtonState extends State<SelectButton> {
  bool selected = false;
  // 기본 값 설정

  void onClicked() {
    setState(() {
      if (selected == false)
        selected = true;
      else
        selected = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    String innerButton = widget.innerButton;
    double width = widget.width;
    double height = widget.height;
    if (selected == false) {
      return Container(
        width: width,
        height: height,
        child: OutlinedButton(
          onPressed: onClicked,
          child: Text(
            innerButton,
          ),
        ),
      );
    } else {
      return Container(
        width: width,
        height: height,
        child: FilledButton(
            onPressed: onClicked,
            style: const ButtonStyle(
                backgroundColor: WidgetStatePropertyAll(Color(0xfff1e047))),
            child: Text(innerButton)),
      );
    }
  }
}

```
```dart
// stateless, 변수를 받고 사용하는 widget
class TransparentButton extends StatelessWidget {
  const TransparentButton({super.key, required this.innerButton});

  final String innerButton;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
        width: 120,
        height: 32,
        child: FilledButton(
            onPressed: () {},
            style: FilledButton.styleFrom(
              backgroundColor: Colors.transparent,
              foregroundColor: const Color(0xffFFFFFF),
            ),
            child: Text(innerButton)));
  }
}

```

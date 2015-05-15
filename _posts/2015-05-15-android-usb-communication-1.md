---
layout: post
title:  "안드로이드와 PC간의 USB 통신 (1)"
date:   2015-05-15 23:20:00
categories: android
---

# 시작하기 전에
안드로이드를 운영체제로 사용하는 모바일 기기들은 대부분 와이파이를 비롯한 무선
인터넷을 통하여 다른 시스템과 통신을 하는 것이 일반적입니다. 하지만 기술적
또는 절차적 제한으로 인하여 무선 인터넷을 사용할 수 없는 환경은 아직도 존재하고,
그러한 환경에서 모바일 기기 내부의 자료를 갱신해야 할 필요성도 있습니다.

USB 하드웨어를 만드는 업체가 아닌 이상 대부분의 경우에는 이런 상황을 고려하지
않으므로 인터넷에서 관련 자료를 찾기가 쉽지 않습니다. 안드로이드와 PC의 USB 통신을
구글에 검색하면 대부분 ADB를 사용하여 소켓 통신을 하라고 말합니다. 하지만 일반
사용자에게 ADB를 써야하니 안드로이드 SDK를 설치하라고 하는것은 올바른 해결책이
아니겠죠.

이 글의 내용은 대한민국 공군에서 모 체계를 개발하면서 안드로이드 기기와 PC간의
USB 통신이 필요했고 그것을 해결하면서 얻은 자료를 정리한 것입니다.


# 안드로이드의 USB통신
USB로 연결된 두 장치는 전원을 공급하고 각 장치들을 열거하는 호스트와 호스트에 연결되어
작동하는 주변기기(Accessory)로 구분됩니다.

안드로이드는 USB 통신을 위해 두 가지 모드를 제공하고 있습니다.
 ![Android USB Host & Accessory](/static/android-usb/usb-host-accessory.png)

 * Host mode :
  안드로이드 기기가 USB 호스트가 되어 장치에 전원을 공급하는 모드입니다.
  이 모드를 사용하려면 안드로이드 기기가 OTG를 지원해야 하고 OTG 케이블이 별도로
  필요합니다.

 * Accessory mode :
   안드로이드 기기가 주변기기가 되고 연결되는 USB 장치가 호스트가 되는 모드입니다.
   여기서는 Accessory mode로 호스트인 PC에 연결되도록 구현할 것입니다.

안드로이드에서 USB를 왜 이렇게 관리하는지에 대한 자세한 내용은 [안드로이드 개발자 홈페이지](https://developer.android.com/guide/topics/connectivity/usb/index.html)를
참고하시기 바랍니다.

# USB 통신을 위한 준비
#### 안드로이드
안드로이드에는 Accessory mode에서 USB 통신을 위한 기능들이 이미 모두 준비되어 있습니다
안드로이드 기기 제조사에 따라 OTG 가 지원되지 않아 Host mode를 사용하지 못할 수도 있습니다.

#### PC
USB 드라이버가 필요합니다. 범용 USB 드라이버 중 하나인 [`libusb`](http://www.libusb.org/)의
윈도용 포팅인 [`libusb-win32`](http://sourceforge.net/p/libusb-win32/wiki/Home/)를
사용할 것입니다. Unix-like 환경이라면 libusb를 사용해도 무방합니다.

[다운로드 페이지](http://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/)에서
최신 버전을 내려받습니다.

코드는 `libusb`의 Java wrapper인 [`libusbjava`](http://libusbjava.sourceforge.net/wp/)를
사용하여 자바로 작성할 것입니다. [다운로드 페이지](http://sourceforge.net/projects/libusbjava/files/)에서
최신 버전의 JAR 파일과 DLL을 내려받습니다.

# 드라이버 설정
#### 하드웨어 ID와 장치 클래스 확인
모든 USB 장치는 제조사 ID(VID; Vendor ID)와 제품 ID(PID; Product ID)를 가지고 있습니다.
이 두개의 값으로 장치의 종류(기종)를 구분할 수 있습니다.

장치 클래스는 비슷한 기능을 제공하는 USB 장치들을 하나로 묶어 드라이버를 제공하기 위한
범주입니다. 덕분에 마우스와 키보드 같은 장치들은 제조사가 모두 다르더라도 운영체제에서
제공하는 드라이버로 사용이 가능합니다.

안드로이드 기기를 USB 케이블로 PC에 연결한 후 장치관리자를 실행하면 **휴대용 장치**의
하위에 기기가 나타나 있을 것입니다.

![장치관리자](/static/android-usb/01-device-list.png)

장치의 속성에서 **자세히** 탭을 선택하면 하드웨어 ID와 장치 클래스를 확인할 수 있습니다.

![하드웨어 ID](/static/android-usb/02-hardware-id.png)

![장치 클래스](/static/android-usb/03-device-class.png)

이 안드로이드 기기의 VID와 PID는 각각 `0x1004`와 `0x61F9`이며 장치 클래스는
`WPD`임을 알 수 있습니다.

`0x1004`는 LG전자의 제조사 ID입니다. 다른 회사의 제품이라면 해당 제조사의 ID가 보여집니다.
`0x61F9`는 LG전자의 안드로이드 기기들의 제품 ID입니다. 다른 모델의 제품이라도 LG전자의
안드로이드 기기는 모두 같은 PID 값을 가질 것입니다.

`WPD`는 MTP 장치의 장치 클래스입니다.

#### 필터 드라이버 설치
내려받은 `libusb-win32`의 파일을 적당한 위치에 압축을 풀어줍니다.
`bin` 디렉터리의 하위에 CPU 아키텍처별로 나누어진 디렉터리가 있습니다. 자신의 PC
CPU 아키텍처에 맞는 디렉터리의 파일들을 사용합니다.

 * `install-filter.exe` : 필터 드라이버를 설치/제거하는 CUI 프로그램입니다.
 * `install-filter-win.exe` : 필터 드라이버를 설치/제거하는 GUI 프로그램입니다.
 * `libusb0.sys` : USB 드라이버 파일입니다.
 * `libusb0.dll` : USB 드라이버의 기능들을 호출하기 위한 라이브러리 DLL입니다.

먼저 `libusb0.sys` 파일을 `C:\Windows\System32\drivers` 디렉터리에 복사합니다.

그 다음 필터 드라이버 설치를 위해 명령 프롬프트를 **관리자 권한**으로 실행합니다.
다음 명령으로 `WPD` 장치 클래스에 필터 드라이버를 설치합니다.

```
$ install-filter install --class=WPD
```

설치가 완료되면 안드로이드 기기의 USB 케이블을 뽑았다가 다시 연결해 주세요.
그런 다음 `testlibusb` 명령을 사용해 필터 드라이버가 올바르게 설치되었는지 검사합니다.
올바르게 설치되었다면 다음과 같이 `Dev #1`항목이 출력되어야 합니다.

```
$ testlibusb.exe

Dev #0: 0000 - 0000

  Dev #1: LG Electronics Inc. - MTP
```

`testlibusb-win.exe`를 사용해 GUI 화면으로 확인할 수도 있습니다.
![Filter Driver Test](/static/android-usb/04-filter-driver-test.png)

GUI 화면에는 `DLL version`과 `Driver version` 및 장치의 상세 정보가 출력되어야 합니다.

* * *

다음 글에서 안드로이드 기기를 Accessory mode로 진입시키고 이것을 감지하여 USB 통신을
처리할 안드로이드 앱을 실행시키는 법에 대하여 설명하도록 하겠습니다.

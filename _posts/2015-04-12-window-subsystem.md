---
layout: post
title:  "윈도 서브시스템 설정(콘솔 없애기)"
date:   2015-04-12 16:00:00
categories: rust
---

 윈도 환경에서 응용프로그램은 일반적으로 두가지 모드로 빌드된다:

  * Console : 콘솔 창을 가지는 CUI 프로그램
  * Windows : 콘솔 창이 없는 GUI 프로그램


 ![]({{ site.url }}static/rust-windows-subsystem/vs-linker-setting.png)
   *Visual Studio 2013의 링커 설정 페이지.*

`rustc`는 윈도 환경에서 기본적으로 Console SubSystem으로 결과물을 생성하지만 링커 옵션을 설정하여 Windows로 설정할 수 있다.

```rust
#![feature(libc)]
#![feature(collections)]
#![feature(link_args)]

#[link_args="-Wl,--subsystem,windows"]
extern{}

extern crate libc;

mod ffi;
use ffi::message_box;

fn main() {
	message_box( "Hello", "World!" );
}
```
2015.4.12 현재 `libc`와 `collections`, `link_args` feature는 unstable 상태이다.
Rust 1.0 Beta는 unstable feature를 포함하면 오류가 발생하며 Nightly 빌드에서만
사용이 가능. *[Rust 블로그](http://blog.rust-lang.org/2015/04/03/Rust-1.0-beta.html) 참조.*

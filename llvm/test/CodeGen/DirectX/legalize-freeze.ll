; NOTE: Assertions have been autogenerated by utils/update_test_checks.py UTC_ARGS: --version 5

; RUN: opt -S -passes='dxil-legalize' -mtriple=dxil-pc-shadermodel6.3-library %s | FileCheck %s


define i32 @test_remove_freeze(i32 %x) {
; CHECK-LABEL: define i32 @test_remove_freeze(
; CHECK-SAME: i32 [[X:%.*]]) {
; CHECK-NEXT:  [[ENTRY:.*:]]
; CHECK-NEXT:    [[Y:%.*]] = add i32 [[X]], 1
; CHECK-NEXT:    ret i32 [[Y]]
;
entry:
  %f = freeze i32 %x
  %y = add i32 %f, 1
  ret i32 %y
}

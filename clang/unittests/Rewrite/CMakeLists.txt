set(LLVM_LINK_COMPONENTS
  Support
  )

add_clang_unittest(RewriteTests
  RewriterTest.cpp
  )
clang_target_link_libraries(RewriteTests
  PRIVATE
  clangFrontend
  clangRewrite
  clangSerialization
  clangTooling
  )

# ===- GPU HeaderFile Class for --export-decls version --------*- python -*--==#
#
# Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
# See https://llvm.org/LICENSE.txt for license information.
# SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
#
# ==-------------------------------------------------------------------------==#

from hdrgen.header import HeaderFile


class GpuHeaderFile(HeaderFile):
    def __str__(self):
        content = []

        content.append(
            f"//===-- C standard declarations for {self.name} ------------------------------===//"
        )
        content.append("//")
        content.append(
            "// Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions."
        )
        content.append("// See https://llvm.org/LICENSE.txt for license information.")
        content.append("// SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception")
        content.append("//")
        content.append(
            "//===----------------------------------------------------------------------===//\n"
        )

        header_guard = f"__LLVM_LIBC_DECLARATIONS_{self.name.upper()[:-2]}_H"
        content.append(f"#ifndef {header_guard}")
        content.append(f"#define {header_guard}\n")

        content.append("#ifndef __LIBC_ATTRS")
        content.append("#define __LIBC_ATTRS")
        content.append("#endif\n")

        content.append("#ifdef __cplusplus")
        content.append('extern "C" {')
        content.append("#endif\n")

        for function in self.functions:
            content.append(f"{function} __LIBC_ATTRS;\n")

        for object in self.objects:
            content.append(f"{object} __LIBC_ATTRS;\n")

        content.append("#ifdef __cplusplus")
        content.append("}")
        content.append("#endif\n")

        content.append(f"#endif")

        return "\n".join(content)

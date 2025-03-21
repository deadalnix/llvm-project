! Offloading test checking interaction of an derived type mapping of two 
! explicit array members to target
! REQUIRES: flang, amdgpu

! RUN: %libomptarget-compile-fortran-run-and-check-generic
program main
    type :: scalar_array
    real(4) :: break_0
    real(4) :: array_x(10)
    real(4) :: break_1
    real(4) :: array_y(10)
    real(4) :: break_3
    end type scalar_array

    type(scalar_array) :: scalar_arr

  do i = 1, 10
    scalar_arr%array_x(i) = i
  end do

  !$omp target map(tofrom:scalar_arr%array_x, scalar_arr%array_y)
    do i = 1, 10
      scalar_arr%array_y(i) = scalar_arr%array_x(i)
    end do
  !$omp end target

  print*, scalar_arr%array_x
  print*, scalar_arr%array_y
end program main

!CHECK: 1. 2. 3. 4. 5. 6. 7. 8. 9. 10.
!CHECK: 1. 2. 3. 4. 5. 6. 7. 8. 9. 10.

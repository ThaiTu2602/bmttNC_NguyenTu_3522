from QuanLySinhVien import QuanLySinhVien
qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nChuong trinh quan ly sinh vien ")
    print("***************menu***************")
    print("** 1.Them sinh vien. **")
    print("** 2.Cập nhật thông tin sinh vien boi ID. **")
    print("** 3.Xoa sinh vien boi ID. **")
    print("** 4.Tìm Kiếm sinh vien theo tên. **")
    print("** 5.Sắp xếp sinh vien theo điểm trung bình. **")
    print("** 6.sắp xếp sinh vien theo tên chuyên ngành. **")
    print("** 7.Hiển thị danh sách sinh vien. **")
    print("** 0.Thoát **")
    print("********************************************")
    key = int(input("Nhap tuy chon:"))
    if (key == 1):
        print("\n1.Them sinh vien.")
        qlsv.nhapSinhVien()
        print("\nThem Sinh Vien Thanh Cong!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien()>0):
            print("\n2. cap nhat thong tin sinh vien .")
            print("\nNhap ID:")
            ID = int (input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh Sách sinh Vien trong !")
    elif (key == 3):
        if (qlsv.soLuongSinhVien()>0):
            print("\n xoa sinh vien .")
            print("\nNhap ID:")
            ID = int (input())
            if(qlsv.deleteByID(ID)):
                print("\nSinh Vien co id = ",ID,"đã bị xoá .")
            else:
                print("\nSinh Vien có ID = ",ID,"Không tồn tại .")
        else:
                print("\nDanh Sách sinh Vien trong !")
    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("Nhap ten de tim kiem: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 0:
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("Hay chon chuc nang trong hop menu.")
            
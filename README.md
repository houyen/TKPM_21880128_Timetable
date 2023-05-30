### TKPM_21880128_Timetable
TKPM_TX_HK2_2022.

-----------------
* Môn học: THIẾT KẾ PHẦN MỀM 
* MSSV: 21880128. 
* Đề tài: Timetable
* Framework: Django
* Ngôn ngữ sử dụng: Python

### Mô tả phần mềm:
  Trường học có nhiều lớp, lớp học và giáo viên. Việc tạo lịch giảng dạy cho từng giáo viên vào các lớp và các tiết học 1 cách thủ công rất dài.
  Chương trình này chạy một hệ thống quản lý thời khóa biểu cho một trường học. Nó có thể phân bổ giáo viên trong các khoảng thời gian rảnh tùy theo môn học ưu tiên của giáo viên, ví dụ (nếu giáo viên toán vắng mặt, hệ thống này sẽ chỉ chỉ định giáo viên toán nếu có trong danh sách giáo viên rảnh) Nó có thể tìm ra các môn học được dạy bởi giáo viên vắng mặt. 
  
  Cũng có thể phân bổ giáo viên theo cách thủ công. Cũng cung cấp tùy chọn cho giáo viên, cho chủ đề cụ thể được giảng dạy. Cung cấp danh sách các giáo viên miễn phí có sẵn trong thời gian cụ thể.

### Hướng dẫn cài đặt
* Install Python >= 3.8 on your Computer from the official website.

* Install Django on your computer by running this command
    pip install Django(For windows)
    python -m pip install Django(For Mac/Linux)

* Run this command on your git terminal
    git clone “https://github.com/houyen/TKPM_21880128_Timetable.git”

* Install dependencies by running this command
    pip install -r requirements.txt

* Run this command to run server on your localhost:8000
    python manage.py runserver
    python manage.py runserver <Tên Cổng>
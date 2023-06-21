### TKPM_21880128_Timetable
TKPM_TX_HK2_2022.

-----------------
* Môn học: THIẾT KẾ PHẦN MỀM 
* MSSV: 21880128. 
* Đề tài: Timetable
* Framework: Django
* Ngôn ngữ sử dụng: Python

### Mô tả phần mềm:
  Việc tạo lịch giảng dạy cho từng giáo viên vào các lớp và các tiết học 1 cách thủ công rất dài.
  Chương trình này chạy một hệ thống quản lý thời khóa biểu cho một trường học.   Trình quản lý thời khóa biểu sẽ giúp bạn chỉ định giáo viên cho một lớp nếu giáo viên được chỉ định không có mặt, ví dụ (nếu giáo viên toán vắng mặt, hệ thống này sẽ chỉ chỉ định giáo viên toán nếu có trong danh sách giáo viên rảnh)

  Cũng có thể phân bổ giáo viên theo cách thủ công. Cũng cung cấp tùy chọn cho giáo viên, cho chủ đề cụ thể được giảng dạy. Cung cấp danh sách các giáo viên miễn phí có sẵn trong thời gian cụ thể.

### Hướng dẫn cài đặt
* Install Python >= 3.8 on your Computer from the official website.

* Run this command on your git terminal: 
    git clone “https://github.com/houyen/TKPM_21880128_Timetable.git”

* Install dependencies by running this command: 
    pip install -r requirements.txt

* Create DataBase
    python manage.py makemigrations _model
    python manage.py migrate

* Run this command to run server on your localhost:8000
    python manage.py runserver 
    python manage.py runserver _port # Nếu trường hợp trùng port đã sử dụng

* Create superuser: 
    python manage.py createsuperuser

* Load data test
    python manage.py loaddata schools/fixtures/cms.json
    python manage.py loaddata classrooms/fixtures/cms.json

*** REST APIs
    ```REST là viết tắt của REpresentational State Transfer (dịch nôn na là chuyển trạng thái đại diện) là một kiểu kiến trúc lập trình, 
nó định nghĩa các quy tắc để thiết kết các web service chú trọng vào tài nguyên hệ thống. 
Trong kiến trúc REST mọi thứ đều được coi là tài nguyên, chúng có thể là: tệp văn bản, ảnh, trang html, video, hoặc dữ liệu động… 
REST server cung cấp quyền truy cập vào các tài nguyên, REST client truy cập và thay đổi các tài nguyên đó. 
Ở đây các tài nguyên được định danh dựa vào URI, REST sử dụng một vài đại diện để biểu diễn các tài nguyên như văn bản, JSON, XML.

Taọ serializers.py và viewset trong view.py là file sẽ code thao tác để tạo được API.```

# period: /api/v0/periods
* liệt kê thời khóa biểu cho các lớp học trong ngày:
	 /?classroom=classroom_id&weekday=a, a = [0,5]
	 /?classroom=classroom_id&date=yyyy-mm-dd
* lịch dạy chi tiết của giáo viên vào 1 ngày cụ thể:
	 /?date=yyyy-mm-dd&teacher=teacher_id
* liệt kê các giáo viên có sẵn để thay thế trong một khoảng thời gian cụ thể:
	 /period_id/free-teachers/?date=Y-m-d
*  liệt kê thông tin chi tiết về việc điều chỉnh thời gian của period_id với subject_teacher_id:
	 /period_id/insights/?tsubject_eacher_id=subject_teacher_id&date=Y-m-d

# adjustment:
* điều chỉnh tiết dạy (period adjustment)
	 /api/v0/period-adjustments
* liệt kê tất cả các điều chỉnh thời gian trong ngày:
	 /?date=Y-m-d

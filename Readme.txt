         NHÓM I
BANK MARKETING

Nguyễn Trường Lâu - 17520676 (Ad)
Trần Công Minh - 17520763
Bùi Đức Cường - 17520301

I. Các thư viện cần có:
tensorflow
keras
xlsxwriter
numpy
tkinter
pandas
Normalize
sklearn
matplotlib
itertools
warnings
os
scipy
seaborn

II. Cách biên dịch chương trình

B1: Tải Anaconda về máy tính
B2: Cài đặt Jupyter Notebook (để đọc file .ipynp) và Spyder (hỗ trợ framework tensorflow)
B3: Tải toàn bộ dữ liệu theo link sau về máy tính (https://drive.google.com/drive/folders/1TD5WXZvX6I2ReYTWDE9-6Mb2b3wg3UmU?usp=sharing)
để chúng trong một thư mục duy nhất
B4: Cài đặt tất cả thư viện nêu trên bằng conda prompt bằng lệnh sau: conda install <tên thư viện cần cài đặt>
B5: Tiến hành chạy file Train.py trong Spyder giao diện sẽ xuất hiện.

III. Các chức năng hỗ trợ

CN1: Nhập từ bàn phím các thông tin của khách hàng, sau đó nhấn <Predict> để chương trình dự đoán khách.
hàng đó có khả năng đăng ký tiền gửi có kỳ hạn hay không.
CN2: Cho phép người dùng chọn và đọc tập tin test, sau đó hiển thị trên UI chương trình.
CN3: Dự đoán nhiều mẫu dữ liệu cùng một lúc, kết quả trả về là độ chính xác trên tập tin đó.
CN4: Định dạng tập tin trả về, những trường dữ liệu dự đoán sai sẽ được tô màu đỏ.
CN5: Xem thông tin chương trình, nhóm thực hiện.

IV. Nguồn tham khảo:
https://www.kaggle.com/yufengsui/ml-project-bank-telemarketing-analysis?fbclid=IwAR2-7jq6Qy_EUIIAaaRA5moLKIAQwtiJF7XF1HvnJ2P6oFzwlzTwVOOCXP8
Source data set: [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014
(Link: http://archive.ics.uci.edu/ml/datasets/Bank+Marketing).
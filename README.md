# Task 2: Search Query Performance - Dashboard
### Mô tả:
Thực hiện trực quan hóa dữ liệu Search Query Performance (SQP) từ các file JSON được cung cấp.
Ứng dụng sử dụng Streamlit + AgGrid để hiển thị dashboard tương tác, với filter theo loại báo cáo (Month / Quarter / Week), filter theo period, và tìm kiếm theo ASIN. 

### Cấu trúc Folder 📁

```
│   app.py
│   
├───Monthly
│       sqp_monthly_report_B0DSKZD8Y7_2025_01_08_20250919_080848.json
│       sqp_monthly_report_B0DSKZFYZQ_2025_01_08_20250919_081740.json
│       sqp_monthly_report_B0F1F59C4C_2025_01_08_20250919_085255.json
│       
├───Quarterly
│       sqp_quarterly_report_B0DSKZD8Y7_2025_Q1-Q2_20250919_090739.json
│       sqp_quarterly_report_B0DSKZFYZQ_2025_Q1-Q2_20250919_091040.json
│       sqp_quarterly_report_B0F1F59C4C_2025_Q1-Q2_20250919_091324.json
│       
└───Weekly
        sqp_weekly_range_report_B0DSKZD8Y7_2025_W16-W37_20250919_094026.json
        sqp_weekly_range_report_B0DSKZFYZQ_2025_W5-W37_20250919_100611.json
        sqp_weekly_range_report_B0F1F59C4C_2025_W16-W37_20250919_102430.json
``` 

## các Bước triển khai 
Bước 1: Clone hoặc tạo cấu trúc thư mục như trên.
Bước 2: Cài đặt thư viện cần thiết:  

``` pip install pandas streamlit streamlit-aggrid ```

Bước 3: Chạy ứng dụng Streamlit:

``` streamlit run app.py ```

Bước 4: Mở trình duyệt và truy cập địa chỉ:

``` http://localhost:8501/ ``` 

(Trình duyệt có thể tự động mở sau khi chạy lệnh).

### Kết quả 


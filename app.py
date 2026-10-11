import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#1. Tạo bảng dữ liệu
st.set_page_config(page_title="Quản lý điểm sinh viên", layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

du_lieu = {
    "Họ tên": [
        "Hoàng Văn Mạnh", "Nguyễn Văn An", "Trần Thị Bình",
        "Lê Văn Cường", "Phạm Thị Dung", "Võ Minh Đức",
        "Đặng Thị Hà", "Bùi Văn Hùng", "Ngô Thị Lan",
        "Đỗ Minh Tuấn"
    ],
    "Chuyên cần": [9, 8, 10, 6, 9, 5, 8, 4, 7, 9],
    "Giữa kỳ": [8, 7, 9, 5, 8, 4, 7, 3, 6, 9],
    "Cuối kỳ": [9, 8, 9, 6, 8, 5, 7, 4, 6, 10]
}
df = pd.DataFrame(du_lieu)

#2. Tính điểm tổng kết
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.2
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.5
)

#3. Xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

st.subheader("Bảng điểm của 10 sinh viên")
st.dataframe(df.style.format({"Tổng kết": "{:.2f}"}))

#4. Thống kê
st.subheader("Thống kê của lớp")
st.write(f"Điểm trung bình của lớp: {df['Tổng kết'].mean():.2f}")
st.write(f"Số sinh viên đạt: {(df['Tổng kết'] >= 5).sum()}/10")

cao_nhat = df[df["Tổng kết"] == df["Tổng kết"].max()]
thap_nhat = df[df["Tổng kết"] == df["Tổng kết"].min()]

st.write("Sinh viên có điểm cao nhất:")
st.dataframe(cao_nhat[["Họ tên", "Tổng kết"]])

st.write("Sinh viên có điểm thấp nhất:")
st.dataframe(thap_nhat[["Họ tên", "Tổng kết"]])

#5. Chọn sinh viên để xem điểm
st.subheader("Tra cứu điểm sinh viên")
ten = st.selectbox("Chọn sinh viên:", df["Họ tên"].tolist())
sinh_vien = df[df["Họ tên"] == ten].iloc[0]

st.write(f"Họ tên: {ten}")
st.write(f"Chuyên cần: {sinh_vien['Chuyên cần']}")
st.write(f"Giữa kỳ: {sinh_vien['Giữa kỳ']}")
st.write(f"Cuối kỳ: {sinh_vien['Cuối kỳ']}")
st.write(f"Tổng kết: {sinh_vien['Tổng kết']:.2f}")
st.write(f"Xếp loại: {sinh_vien['Xếp loại']}")

#6. Vẽ biểu đồ
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(12, 6))
cot = ax.bar(df["Họ tên"], df["Tổng kết"], color="skyblue")
ax.bar_label(cot, fmt="%.1f")
ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

#7. Thông tin người tạo ứng dụng
st.divider()
st.caption("Người thực hiện: Hoàng Văn Mạnh | MSSV: 040208024201")

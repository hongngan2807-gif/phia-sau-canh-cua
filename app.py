import streamlit as st
import time

# --- CẤU HÌNH TRANG STREAMLIT ---
st.set_page_config(
    page_title="PHÍA SAU CÁNH CỬA",
    page_icon="👻",
    layout="centered"
)

# --- TÙY CHỈNH GIAO DIỆN KINH DỊ & HẦM NGỤC ---
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0b0b;
        color: #e0e0e0;
        font-family: 'Courier New', Courier, monospace;
        background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url('bg1.jpg');
        background-size: cover;
    }
    h1, h2, h3 {
        color: #b30000 !important;
        text-align: center;
        text-shadow: 2px 2px 6px #000000;
    }
    .stButton>button {
        background-color: #2b0000;
        color: #ffcccc;
        border: 1px solid #800000;
        border-radius: 5px;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #800000;
        color: #ffffff;
    }
    .stTextInput>div>div>input {
        background-color: #141414;
        color: #ffffff;
        border: 1px solid #520000;
    }
    .info-box {
        background-color: #121212;
        padding: 18px;
        border-left: 4px solid #b30000;
        border-radius: 4px;
        margin-bottom: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.6);
    }
    </style>
""", unsafe_allow_html=True)

# --- KHỞI TẠO SESSION STATE ---
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = 0
if 'character' not in st.session_state:
    st.session_state.character = None
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'won' not in st.session_state:
    st.session_state.won = False
if 'caught_by_ghost' not in st.session_state:
    st.session_state.caught_by_ghost = ""

# --- TIÊU ĐỀ CHÍNH ---
st.title("🕯️ PHÍA SAU CÁNH CỬA 🕯️")
st.caption("✍️ Tác giả: Quốc Cường, Nguyệt Hồng và Hà My | Trò chơi dành cho trẻ em trên 12 tuổi")

# --- TRÌNH PHÁT NHẠC NỀN TRỰC QUAN (LINK MỚI ỔN ĐỊNH) ---
st.markdown("🔊 **Bật nhạc nền kinh dị để tăng trải nghiệm rùng rợn:**")
st.audio("https://cdn.pixabay.com/download/audio/2022/03/15/audio_c8c7a73167.mp3?filename=horror-background-atmosphere-156462.mp3", format="audio/mp3")

st.divider()

# --- MÀN HÌNH CHỌN NHÂN VẬT ---
if not st.session_state.game_started:
    st.subheader("🕵️ CỐT TRUYỆN HỒI HỘP")
    st.markdown("""
    <div class="info-box">
    Bạn bị nhốt trong phòng làm việc u ám của một Thám tử tư nổi tiếng. Căn phòng ngập tràn bầu không khí lạnh lẽo và oán khí của 3 linh hồn quỷ quái đang lảng vảng xung quanh. Để chứng minh khả năng phá án và mở cửa sinh tồn ra ngoài, bạn phải vượt qua <b>3 thử thách sinh tử</b> để thu thập chìa khóa trốn thoát.<br><br>
    <b>⚠️ CẢNH BÁO:</b> Bạn chỉ có đúng <b>3 PHÚT (180 giây)</b>! Nếu hết thời gian hoặc bất cẩn trả lời sai bị hồn ma bắt gặp, bạn sẽ thua cuộc ngay lập tức!
    </div>
    """, unsafe_allow_html=True)

    st.subheader("🎭 Lựa Chọn Nhân Vật Yêu Thích Của Bạn")
    col1, col2, col3 = st.columns(3)

    with col1:
        try: st.image("char1.jpg", caption="Dee Dee (Gián Xanh)", use_column_width=True)
        except: st.write("**Dee Dee (Gián Cam)**")
        if st.button("Chọn Dee Dee"):
            st.session_state.character = "Dee Dee (Gián Xanh)"
            st.session_state.game_started = True
            st.session_state.start_time = time.time()
            st.rerun()

    with col2:
        try: st.image("char2.jpg", caption="Joey (Gián Cam)", use_column_width=True)
        except: st.write("**Joey (Gián Tím)**")
        if st.button("Chọn Joey"):
            st.session_state.character = "Joey (Gián Cam)"
            st.session_state.game_started = True
            st.session_state.start_time = time.time()
            st.rerun()

    with col3:
        try: st.image("char3.jpg", caption="Marky (Gián Tím)", use_column_width=True)
        except: st.write("**Marky (Gián Xanh)**")
        if st.button("Chọn Marky"):
            st.session_state.character = "Marky (Gián Tím)"
            st.session_state.game_started = True
            st.session_state.start_time = time.time()
            st.rerun()

# --- MÀN HÌNH TRẢI NGHIỆM GAME ---
else:
    elapsed_time = time.time() - st.session_state.start_time
    remaining_time = max(0, int(180 - elapsed_time))

    st.write(f"⏱️ **Thời gian sinh tồn còn lại:** `{remaining_time // 60:02d}:{remaining_time % 60:02d}`")
    st.progress(remaining_time / 180)

    # Kiểm tra hết giờ -> Hồn ma bắt
    if remaining_time <= 0 and not st.session_state.won:
        st.session_state.game_over = True
        st.session_state.caught_by_ghost = "Hết giờ! Bạn đã bị Tân Nương Đỏ bắt giữ trong bóng tối."

    # --- KẾT QUẢ THUA CUỘC ---
    if st.session_state.game_over:
        # Phát âm thanh tiếng cười kinh dị khi thua
        st.audio("https://cdn.pixabay.com/download/audio/2021/08/04/audio_12d46e34c2.mp3?filename=evil-laugh-81143.mp3", format="audio/mp3")

        st.error("💀 THUA CUỘC! BẠN ĐÃ BỊ HỒN MA TÓM GỌN VÀ TIẾNG CƯỜI KINH DỊ VANG LÊN!")
        
        col_g1, col_g2, col_g3 = st.columns(3)
        with col_g1:
            try: st.image("ghost1.jpg", caption="Tân Nương Đỏ", use_column_width=True)
            except: pass
        with col_g2:
            try: st.image("ghost2.jpg", caption="Ma Sơ Valak", use_column_width=True)
            except: pass
        with col_g3:
            try: st.image("ghost3.jpg", caption="Ma Hề Pennywise", use_column_width=True)
            except: pass

        st.write(f"⚠️ *Chi tiết:* {st.session_state.caught_by_ghost}")
        if st.button("🔄 Thử Thách Lại Từ Đầu"):
            st.session_state.game_started = False
            st.session_state.step = 1
            st.session_state.game_over = False
            st.session_state.won = False
            st.rerun()

    # --- KẾT QUẢ CHIẾN THẮNG ---
    elif st.session_state.won:
        st.success("🎉 CHÚC MỪNG BẠN ĐÃ CHIẾN THẮNG TRÒ CHƠI!")
        st.write(f"Nhân vật **{st.session_state.character}** đã vượt qua tất cả cạm bẫy, trốn thoát khỏi căn phòng thám tử an toàn!")
        if st.button("🔄 Chơi Lại Lần Nữa"):
            st.session_state.game_started = False
            st.session_state.step = 1
            st.session_state.game_over = False
            st.session_state.won = False
            st.rerun()

    # --- CÁC THỬ THÁCH GIẢI ĐỐ (3 THỬ THÁCH) ---
    else:
        st.write(f"👤 Nhân vật nhập vai: **{st.session_state.character}**")
        st.divider()

        # THỬ THÁCH 1
        if st.session_state.step == 1:
            st.subheader("🔍 Thử Thách 1: Mật Mã Từ Cuốn Sách")
            st.markdown("""
            **Manh mối:** Trên bàn có 3 cuốn sách xếp chồng lên nhau: Cuốn số 1 dày nhất, Cuốn số 2 mỏng hơn, Cuốn số 3 ở giữa. Bên cạnh có một tờ giấy ghi chú:  
            *"Mật khẩu mở ngăn kéo gồm 3 chữ số, tương ứng với số trang có chứa từ 'BÍ MẬT' trong ba cuốn sách theo thứ tự từ trên xuống dưới."*  
            
            - Cuốn 3 (trên cùng): Trang 15  
            - Cuốn 2 (ở giữa): Trang 8  
            - Cuốn 1 (dưới cùng): Trang 20  
            """)
            
            ans1 = st.text_input("Nhập mật mã mở ngăn kéo bàn (3 chữ số):")
            if st.button("Mở Ngăn Kéo"):
                if ans1.strip() in ["15820", "182"]:
                    st.success("Mật mã chính xác! Bạn nhận được **Một mảnh bản đồ**.")
                    st.session_state.step = 2
                    st.rerun()
                else:
                    st.session_state.game_over = True
                    st.session_state.caught_by_ghost = "Bạn nhập sai mật mã quá lâu và đã bị Ma Sơ Valak phát hiện!"
                    st.rerun()

        # THỬ THÁCH 2
        elif st.session_state.step == 2:
            st.subheader("🧩 Thử Thách 2: Mật Mã Số Học Qua Hình Vẽ")
            st.markdown("""
            **Manh mối:** Trên mảnh bản đồ vừa tìm được có câu đố hình ảnh:  
            - Mũ thám tử + Mũ thám tử = 10  
            - Kính lúp × Mũ thám tử = 15  
            - Tẩu thuốc - Kính lúp = ?  
            
            *(Dữ liệu: Mũ thám tử = 5, Kính lúp = 3, Tẩu thuốc = 7)*
            """)
            
            ans2 = st.text_input("Nhập kết quả phép tính (Tẩu thuốc - Kính lúp):")
            if st.button("Xác Nhận Đáp Án"):
                if ans2.strip() == "4":
                    st.success("Chính xác! Bạn nhận được **Chìa khóa mở cửa cuối cùng**.")
                    st.session_state.step = 3
                    st.rerun()
                else:
                    st.session_state.game_over = True
                    st.session_state.caught_by_ghost = "Tính toán sai! Tiếng động của bạn đã thu hút Ma Hề Pennywise tóm gọn."
                    st.rerun()

        # THỬ THÁCH 3
        elif st.session_state.step == 3:
            st.subheader("🚪 Thử Thách 3: Mật Mã Cửa Chính")
            st.markdown("""
            **Manh mối:** Cửa chính yêu cầu nhập từ khóa gồm 6 chữ cái tiếng Anh liên quan đến công việc thám tử, viết đảo ngược:  
            *“Hãy đọc ngược từ phải sang trái dòng chữ sau: **R-E-T-C-E-S**”*
            """)
            
            ans4 = st.text_input("Nhập từ khóa mở cửa chính:")
            if st.button("Mở Cửa Trốn Thoát"):
                if ans4.strip().upper() == "SECRET":
                    st.session_state.won = True
                    st.rerun()
                else:
                    st.session_state.game_over = True
                    st.session_state.caught_by_ghost = "Nhập sai từ khóa mở cửa ở giây phút quyết định, cả 3 hồn ma đã ập tới!"
                    st.rerun()

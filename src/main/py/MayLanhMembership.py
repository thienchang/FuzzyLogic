'''
Created on Apr 5, 2026

@author: ThienTrang
'''

import numpy as np 
import skfuzzy as fz 
import matplotlib.pyplot as plt
import os

# ======================
# Tập mờ N (Số người)
# ======================
x_people = np.arange(0, 11, 0.1)
it_nguoi = fz.trapmf(x_people, [1, 1, 2, 3])
trung_binh = fz.trapmf(x_people, [2, 3, 5, 6])
nhieu_nguoi = fz.trapmf(x_people, [5, 6, 7, 8])
rat_nhieu = fz.trapmf(x_people, [7, 8, 10, 10])

# ======================
# Tập mờ Tin (Nhiệt độ vào)
# ======================
x_tin = np.arange(17, 31, 0.1)
lanh_in = fz.trapmf(x_tin, [18, 18, 19, 21])
vua_in = fz.trapmf(x_tin, [20, 22, 25, 27])
nong_in = fz.trapmf(x_tin, [26, 28, 30, 30])

# ======================
# Tập mờ Tout (Nhiệt độ ra)
# ======================
x_tout = np.arange(19, 41, 0.1)
lanh_out = fz.trapmf(x_tout, [20, 20, 21, 22])
vua_out = fz.trapmf(x_tout, [21, 23, 26, 28])
nong_out = fz.trapmf(x_tout, [27, 29, 34, 36])
rat_nong_out = fz.trapmf(x_tout, [35, 38, 40, 40])

# ======================
# Tập mờ L (Mức độ)
# ======================
x_L = np.arange(17, 28, 0.1)
rat_thap = fz.trimf(x_L, [18, 18, 20])
thap = fz.trimf(x_L, [19, 20, 22])
trung_binh_L = fz.trapmf(x_L, [21, 22, 23, 24])
cao = fz.trapmf(x_L, [23, 24, 25, 26])
rat_cao = fz.trapmf(x_L, [25, 26, 27, 27])
# ======================
# Vẽ
# ======================
plt.figure(figsize=(12, 14))

# ---- Plot N ----
plt.subplot(4, 1, 1)
plt.plot(x_people, it_nguoi, linewidth=2, label="Ít Người")
plt.plot(x_people, trung_binh, linewidth=2, label="Trung Bình")
plt.plot(x_people, nhieu_nguoi, linewidth=2, label="Nhiều Người")
plt.plot(x_people, rat_nhieu, linewidth=2, label="Rất Nhiều")
plt.fill_between(x_people, it_nguoi, alpha=0.2)
plt.fill_between(x_people, trung_binh, alpha=0.2)
plt.fill_between(x_people, nhieu_nguoi, alpha=0.2)
plt.fill_between(x_people, rat_nhieu, alpha=0.2)
plt.title("Số Người Trong Phòng", fontsize=16)
plt.ylabel("Membership")
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# ---- Plot Tin ----
plt.subplot(4, 1, 2)
plt.plot(x_tin, lanh_in, linewidth=2, label="Lạnh")
plt.plot(x_tin, vua_in, linewidth=2, label="Vừa")
plt.plot(x_tin, nong_in, linewidth=2, label="Nóng")
plt.fill_between(x_tin, lanh_in, alpha=0.2)
plt.fill_between(x_tin, vua_in, alpha=0.2)
plt.fill_between(x_tin, nong_in, alpha=0.2)
plt.title("Nhiệt Độ Vào", fontsize=16)
plt.ylabel("Membership")
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# ---- Plot Tout ----
plt.subplot(4, 1, 3)
plt.plot(x_tout, lanh_out, linewidth=2, label="Lạnh")
plt.plot(x_tout, vua_out, linewidth=2, label="Vừa")
plt.plot(x_tout, nong_out, linewidth=2, label="Nóng")
plt.plot(x_tout, rat_nong_out, linewidth=2, label="Rất Nóng")
plt.fill_between(x_tout, lanh_out, alpha=0.2)
plt.fill_between(x_tout, vua_out, alpha=0.2)
plt.fill_between(x_tout, nong_out, alpha=0.2)
plt.fill_between(x_tout, rat_nong_out, alpha=0.2)
plt.title("Nhiệt Độ Ra", fontsize=16)
plt.ylabel("Membership")
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# ---- Plot L ----
plt.subplot(4, 1, 4)
plt.plot(x_L, rat_thap, linewidth=2, label="Rất Thấp")
plt.plot(x_L, thap, linewidth=2, label="Thấp")
plt.plot(x_L, trung_binh_L, linewidth=2, label="Trung Bình")
plt.plot(x_L, cao, linewidth=2, label="Cao")
plt.plot(x_L, rat_cao, linewidth=2, label="Rất Cao")
plt.fill_between(x_L, rat_thap, alpha=0.2)
plt.fill_between(x_L, thap, alpha=0.2)
plt.fill_between(x_L, trung_binh_L, alpha=0.2)
plt.fill_between(x_L, cao, alpha=0.2)
plt.fill_between(x_L, rat_cao, alpha=0.2)
plt.title("Mức Độ", fontsize=16)
plt.xlabel("Giá trị")
plt.ylabel("Membership")
plt.ylim(0, 1.05)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

# Layout đẹp hơn
plt.tight_layout()
# Xuất PDF
project_root = os.path.abspath(os.path.join(os.getcwd(), "..", "..", ".."))
resources_dir = os.path.join(project_root, "src", "main", "resources")

os.makedirs(resources_dir, exist_ok=True)

save_path = os.path.join(resources_dir, "Maylanh_membership_functions.pdf")
plt.savefig(save_path, format='pdf', bbox_inches='tight')
plt.show()
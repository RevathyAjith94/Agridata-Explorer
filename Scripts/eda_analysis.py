# ================================================================
# 📊 AGRIDATA EXPLORER – COMPLETE EDA SCRIPT (PROFESSIONAL VERSION)
# ================================================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------------------------------
# 1. PATH SETTINGS
# -------------------------------
DATA_PATH = r"D:\Agridata_Explorer\data\Cleaned_data.csv"
PLOTS_DIR = r"D:\Agridata_Explorer\Plots"

# Create Plots folder if not exists
os.makedirs(PLOTS_DIR, exist_ok=True)

# -------------------------------
# 2. LOAD DATA
# -------------------------------
df = pd.read_csv(r"D:\Agridata_Explorer\data\Cleaned_data.csv")
print("\n EDA Started...")
print(df.head())
print(df.info())

# -------------------------------
# Helper function to save plots
# -------------------------------
def save_plot(filename):
    plt.tight_layout()
    plt.savefig(f"{PLOTS_DIR}/{filename}", dpi=300)
    plt.close()


# ================================================================
# 1️⃣ TOP 7 RICE PRODUCTION STATES
# ================================================================
rice = df.groupby("State Name")["RICE PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).head(7)

plt.figure(figsize=(10,6))
rice.plot(kind="bar", color="teal")
plt.title("Top 7 Rice Producing States")
plt.ylabel("Production (1000 tons)")
save_plot("top_rice_states.png")


# ================================================================
# 2️⃣ TOP 5 WHEAT STATES
# ================================================================
wheat = df.groupby("State Name")["WHEAT PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(10,6))
wheat.plot(kind="bar", color="orange")
plt.title("Top 5 Wheat Producing States")
plt.ylabel("Production")
save_plot("top_wheat_states.png")


# ================================================================
# 3️⃣ WHEAT % SHARE – PIE CHART
# ================================================================
plt.figure(figsize=(8,8))
plt.pie(wheat, labels=wheat.index, autopct="%1.1f%%", startangle=90)
plt.title("Wheat Production Share – Top 5 States")
save_plot("wheat_share_pie.png")


# ================================================================
# 4️⃣ TOP 5 OILSEED PRODUCTION STATES
# ================================================================
oil = df.groupby("State Name")["OILSEEDS PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(10,6))
oil.plot(kind="bar", color="brown")
plt.title("Top Oilseed Producing States")
save_plot("top_oilseed_states.png")


# ================================================================
# 5️⃣ TOP 7 SUNFLOWER STATES
# ================================================================
sun = df.groupby("State Name")["SUNFLOWER PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).head(7)

plt.figure(figsize=(10,6))
sun.plot(kind="bar", color="gold")
plt.title("Top Sunflower Producing States")
save_plot("top_sunflower_states.png")


# ================================================================
# 6️⃣ SUGARCANE LAST 50 YEARS
# ================================================================
sugar = df.groupby("Year")["SUGARCANE PRODUCTION (1000 tons)"].sum().tail(50)

plt.figure(figsize=(12,6))
plt.plot(sugar.index, sugar.values, marker="o")
plt.title("Sugarcane Production – Last 50 Years")
plt.grid(True)
save_plot("sugarcane_50years.png")


# ================================================================
# 7️⃣ RICE VS WHEAT – LAST 50 YEARS
# ================================================================
rice_yr = df.groupby("Year")["RICE PRODUCTION (1000 tons)"].sum()
wheat_yr = df.groupby("Year")["WHEAT PRODUCTION (1000 tons)"].sum()

plt.figure(figsize=(12,6))
plt.plot(rice_yr.index, rice_yr.values, label="Rice")
plt.plot(wheat_yr.index, wheat_yr.values, label="Wheat")
plt.title("Rice vs Wheat Production – 50 Years")
plt.legend()
plt.grid(True)
save_plot("rice_vs_wheat_50years.png")


# ================================================================
# 8️⃣ WEST BENGAL – RICE DISTRICTS
# ================================================================
wb = df[df["State Name"] == "West Bengal"]
wb_rice = wb.groupby("Dist Name")["RICE PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
wb_rice.plot(kind="barh", color="purple")
plt.title("Top Rice Producing Districts – West Bengal")
save_plot("wb_rice_districts.png")


# ================================================================
# 9️⃣ UTTAR PRADESH – TOP 10 WHEAT YEARS
# ================================================================
up = df[df["State Name"] == "Uttar Pradesh"]
up_wheat = up.groupby("Year")["WHEAT PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
up_wheat.plot(kind="bar", color="red")
plt.title("Top 10 Wheat Years – Uttar Pradesh")
save_plot("up_wheat_years.png")


# ================================================================
# 🔟 MILLET PRODUCTION – LAST 50 YEARS
# ================================================================
df["TOTAL MILLET"] = df["PEARL MILLET PRODUCTION (1000 tons)"] + df["FINGER MILLET PRODUCTION (1000 tons)"]
millet = df.groupby("Year")["TOTAL MILLET"].sum().tail(50)

plt.figure(figsize=(12,6))
plt.plot(millet.index, millet.values, marker="o")
plt.title("Millet Production – Last 50 Years")
plt.grid(True)
save_plot("millet_50years.png")


# ================================================================
# 1️⃣1️⃣ SORGHUM – KHARIF VS RABI
# ================================================================
sor = df.groupby("State Name")[
    ["KHARIF SORGHUM PRODUCTION (1000 tons)",
     "RABI SORGHUM PRODUCTION (1000 tons)"]
].sum().head(10)

plt.figure(figsize=(12,6))
sor.plot(kind="bar")
plt.title("Sorghum: Kharif vs Rabi")
save_plot("sorghum_kharif_rabi.png")


# ================================================================
# 1️⃣2️⃣ GROUNDNUT – TOP STATES
# ================================================================
gn = df.groupby("State Name")["GROUNDNUT PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).head(7)

plt.figure(figsize=(10,6))
gn.plot(kind="bar", color="sienna")
plt.title("Top Groundnut Producing States")
save_plot("groundnut_states.png")


# ================================================================
# 1️⃣3️⃣ SOYBEAN – PRODUCTION + YIELD (DUAL AXIS)
# ================================================================
soy = df.groupby("State Name")[
    ["SOYABEAN PRODUCTION (1000 tons)", "SOYABEAN YIELD (Kg per ha)"]
].mean().sort_values("SOYABEAN PRODUCTION (1000 tons)", ascending=False).head(5)

plt.figure(figsize=(12,6))
plt.bar(soy.index, soy["SOYABEAN PRODUCTION (1000 tons)"], label="Production")
plt.plot(soy.index, soy["SOYABEAN YIELD (Kg per ha)"], marker="o", color="black", label="Yield")
plt.legend()
plt.title("Soybean: Production & Yield")
save_plot("soybean_prod_yield.png")


# ================================================================
# 1️⃣4️⃣ OILSEED PRODUCTION – TOP 15 STATES
# ================================================================
oil15 = df.groupby("State Name")["OILSEEDS PRODUCTION (1000 tons)"].sum().sort_values(ascending=False).head(15)

plt.figure(figsize=(14,6))
oil15.plot(kind="bar")
plt.title("Oilseed Production – Top 15 States")
save_plot("oilseed_top15.png")


# ================================================================
# 1️⃣5️⃣ HEATMAP – AREA VS PRODUCTION
# ================================================================
corr = df[
    ["RICE AREA (1000 ha)", "RICE PRODUCTION (1000 tons)",
     "WHEAT AREA (1000 ha)", "WHEAT PRODUCTION (1000 tons)",
     "MAIZE AREA (1000 ha)", "MAIZE PRODUCTION (1000 tons)"]
].corr()

plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Impact of Area vs Production")
save_plot("area_vs_production_heatmap.png")


# ================================================================
# 1️⃣6️⃣ RICE VS WHEAT YIELD – STATES
# ================================================================
yield_data = df.groupby("State Name")[
    ["RICE YIELD (Kg per ha)", "WHEAT YIELD (Kg per ha)"]
].mean()

plt.figure(figsize=(14,6))
yield_data.plot(kind="bar")
plt.title("Rice vs Wheat Yield – States")
save_plot("yield_comparison_states.png")

print("\n🎉 ALL 16 EDA CHARTS CREATED & SAVED SUCCESSFULLY!")








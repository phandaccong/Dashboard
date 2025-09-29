import os
import json
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

# ===== Config =====
BASE_DIR = r"C:\Users\Cong\Downloads\data_mini_project"

FOLDERS = {
    "Month": "Monthly",
    "Quarter": "Quarterly",
    "Week": "Weekly"
}

# ===== Load JSON thành wide-table =====
def load_all_data(base_dir=BASE_DIR, folders=FOLDERS):
    records = []

    for report_type, folder_name in folders.items():
        folder_path = os.path.join(base_dir, folder_name)
        if not os.path.exists(folder_path):
            continue

        for file in os.listdir(folder_path):
            if not file.endswith(".json"):
                continue
            file_path = os.path.join(folder_path, file)

            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            for row in data.get("raw_data", []):
                if report_type == "Month":
                    period = row.get("month_period", "")
                elif report_type == "Quarter":
                    period = row.get("quarter_period", "")
                elif report_type == "Week":
                    period = row.get("week_period", "")
                else:
                    period = ""

                search = row.get("searchQueryData", {})

                rec = {
                    "report_type": report_type,
                    "period": period,
                    "asin": row.get("asin", ""),
                    "searchQuery": search.get("searchQuery", ""),
                    "searchQueryScore": search.get("searchQueryScore", 0),
                    "searchQueryVolume": search.get("searchQueryVolume", 0),
                    # Impressions
                    "Impressions_Total": row.get("impressionData", {}).get("totalQueryImpressionCount", 0),
                    "Impressions_ASIN": row.get("impressionData", {}).get("asinImpressionCount", 0),
                    "Impressions_Share": row.get("impressionData", {}).get("asinImpressionShare", None),
                    # Clicks
                    "Clicks_Total": row.get("clickData", {}).get("totalClickCount", 0),
                    "Clicks_ASIN": row.get("clickData", {}).get("asinClickCount", 0),
                    "Clicks_Share": row.get("clickData", {}).get("asinClickShare", None),
                    # Cart Adds
                    "CartAdds_Total": row.get("cartAddData", {}).get("totalCartAddCount", 0),
                    "CartAdds_ASIN": row.get("cartAddData", {}).get("asinCartAddCount", 0),
                    "CartAdds_Share": row.get("cartAddData", {}).get("asinCartAddShare", None),
                    # Purchases
                    "Purchases_Total": row.get("purchaseData", {}).get("totalPurchaseCount", 0),
                    "Purchases_ASIN": row.get("purchaseData", {}).get("asinPurchaseCount", 0),
                    "Purchases_Share": row.get("purchaseData", {}).get("asinPurchaseShare", None),
                }
                records.append(rec)

    return pd.DataFrame(records)


# ===== Streamlit App =====
st.set_page_config(page_title="Search Query Performance Dashboard", layout="wide")
st.title("Search Query Performance Dashboard")

df = load_all_data()

# Filter 1: chọn loại báo cáo
report_type = st.selectbox("Chọn loại báo cáo:", df["report_type"].unique())
df_filtered = df[df["report_type"] == report_type]

# Filter 2: chọn period
periods = sorted(df_filtered["period"].dropna().unique())
period = st.selectbox("Chọn period:", periods)
df_filtered = df_filtered[df_filtered["period"] == period]

# Filter 3: tìm kiếm theo ASIN
asin_input = st.text_input("Tìm kiếm theo ASIN:", "")
if asin_input:
    df_filtered = df_filtered[df_filtered["asin"].str.contains(asin_input, case=False, na=False)]

st.markdown(f"### Data cho {report_type} – {period}")

# ===== Define column groups =====
column_defs = [
    {"headerName": "ASIN" , "field":"asin","pinned": "left" },
    {"headerName": "Search Query", "field": "searchQuery", "pinned": "left"},
    {"headerName": "Query Score", "field": "searchQueryScore", "pinned": "left"},
    {"headerName": "Query Volume", "field": "searchQueryVolume", "pinned": "left"},
    
    {
        "headerName": "Search Funnel - Impressions",
        "children": [
            {"headerName": "Total Count", "field": "Impressions_Total"},
            {"headerName": "ASIN Count", "field": "Impressions_ASIN"},
            {"headerName": "ASIN Share", "field": "Impressions_Share"},
        ],
    },
    {
        "headerName": "Search Funnel - Clicks",
        "children": [
            {"headerName": "Total Count", "field": "Clicks_Total"},
            {"headerName": "ASIN Count", "field": "Clicks_ASIN"},
            {"headerName": "ASIN Share", "field": "Clicks_Share"},
        ],
    },
    {
        "headerName": "Search Funnel - Cart Adds",
        "children": [
            {"headerName": "Total Count", "field": "CartAdds_Total"},
            {"headerName": "ASIN Count", "field": "CartAdds_ASIN"},
            {"headerName": "ASIN Share", "field": "CartAdds_Share"},
        ],
    },
    {
        "headerName": "Search Funnel - Purchases",
        "children": [
            {"headerName": "Total Count", "field": "Purchases_Total"},
            {"headerName": "ASIN Count", "field": "Purchases_ASIN"},
            {"headerName": "ASIN Share", "field": "Purchases_Share"},
        ],
    },
]

grid_options = {
    "columnDefs": column_defs,
    "defaultColDef": {
        "resizable": True,
        "sortable": True,
        "filter": True,
    },
}

# ===== Render bảng =====
AgGrid(
    df_filtered,
    gridOptions=grid_options,
    enable_enterprise_modules=True,
    fit_columns_on_grid_load=True,
    height=600,
)

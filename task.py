import requests
import json
from datetime import datetime, timedelta

# -------------------------------
# KeepAliveE5 模擬續期邏輯（簡化版）
# -------------------------------

def simulate_keepalive_activity():
    """
    模擬執行 Microsoft Graph API 或其他活動來保持帳號活躍。
    實際專案中會呼叫真實 API。
    """
    print("執行 KeepAlive 活動中...")
    # 模擬成功續期
    return True

def calculate_new_expiry_date():
    """
    根據 Microsoft 的續期邏輯，成功續期後延長 90 天。
    """
    today = datetime.today()
    new_expiry = today + timedelta(days=90)
    return new_expiry.strftime("%Y/%m/%d")

# -------------------------------
# Google Sheet Webhook 記錄邏輯
# -------------------------------

def record_expiry_to_google_sheet(expiry_date):
    webhook_url = "https://script.google.com/macros/s/AKfycbwTZFTT5pFpLP1WUnqSfpOkxCwdi5AAedGGvyLZyPnCjDz10RBSvzr-d32WYRen9q6C/exec"
    payload = {"expiry": expiry_date}
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 200:
            print(f"✅ 成功記錄到期日 {expiry_date} 到 Google Sheet")
        else:
            print(f"❌ 記錄失敗，狀態碼：{response.status_code}")
    except Exception as e:
        print(f"❌ 發送請求時發生錯誤：{e}")

# -------------------------------
# 主流程
# -------------------------------

def main():
    success = simulate_keepalive_activity()
    if success:
        expiry_date = calculate_new_expiry_date()
        record_expiry_to_google_sheet(expiry_date)
    else:
        print("❌ KeepAlive 活動失敗，未能續期")

if __name__ == "__main__":
    main()

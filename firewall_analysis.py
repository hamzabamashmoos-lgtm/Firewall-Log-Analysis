import pandas as pd

# قراءة ملف البيانات
df = pd.read_csv("firewall_logs.csv")


# السؤال الأول:
# استخراج الـ IP الأكثر استهلاكاً للبيانات

ip_data = df.groupby("IP")["Data_Transferred"].sum()

top_ip = ip_data.idxmax()
top_data = ip_data.max()

print("Top IP:", top_ip)
print("Data Transferred:", top_data)



# السؤال الثاني:
# حساب المتوسط والانحراف المعياري لمحاولات الدخول الفاشلة

mean_failed = df["Failed_Logins"].mean()

std_failed = df["Failed_Logins"].std()

print("Mean:", mean_failed)
print("Standard Deviation:", std_failed)



# السؤال الثالث:
# استخراج أحداث Malware وحفظها في ملف منفصل

malware_events = df[df["Event_Type"] == "Malware"]

print(malware_events)

malware_events.to_csv(
    "malware_events.csv",
    index=False
)
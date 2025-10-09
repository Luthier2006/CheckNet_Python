import speedtest as st

def Speed_Test():
 test = st.Speedtest()
 down_speed = round(test.download() / 10**6, 2)
 up_speed = round(test.upload() / 10**6, 2)
 ping = test.results.ping
 print(f"Download: {down_speed} Mbps\nUpload: {up_speed} Mbps\nPing: {ping} ms")

Speed_Test()
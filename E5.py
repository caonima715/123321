import time

def focus_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"剩余时间：{mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("\n专注时间结束！")

if __name__ == "__main__":
    try:
        focus_minutes = int(input("请输入专注时长（分钟）："))
        focus_timer(focus_minutes)
    except ValueError:
        print("无效的输入，请输入一个有效的数字。")

time = int(input("Enter the time in seconds:  "))
hh = time // 3600
mm = time % 3600 // 60
ss = time % 60
print(f"{hh:02d}:{mm:02d}:{ss:02d}")

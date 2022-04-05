time_in_seconds = int(input('Введите время в секундах:  ',))
hours = time_in_seconds // 3600
# print(hours)
minutes = (time_in_seconds - hours*3600) // 60
# print(minutes)
seconds = time_in_seconds % 60
# print(seconds)
# print("%02d:%02d:%02d" % (hours, minutes, seconds))  # using %
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")    # using f

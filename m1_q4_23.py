# 次のプログラムを実行した結果として、正しいものはどれか。
ip_address = "192.168.3.1"
ip_spl = ip_address.split(".")
bin_exp = ""
for num in ip_spl:
    bin_exp += bin(int(num))[2:] + "."
print(bin_exp[:-1])
# ANSWER ウ:11000000.10101000.11.1

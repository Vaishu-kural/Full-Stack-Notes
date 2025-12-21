class laptop:
    price=0
    processor=""
    ram=""

hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=50000
hp.processor="i5"
hp.ram="8GB"

dell.price=550000
dell.processor="i7"
dell.ram="16GB"

lenovo.price=550000
lenovo.processor="i5"
lenovo.ram="8GB"

print(hp.price)
print(dell.price)                                  # code reuse
print(hp.processor)
print(hp.ram)



#hp_price     code length
#hp_ram
#hp_processor

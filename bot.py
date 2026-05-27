import json

print("=== บอทเวอร์ชัน 3.0: ดึงข้อมูลดิบจากอินเทอร์เน็ต ===\n")

internet_data = """
[
    {"product_id": 101, "title": "คีย์บอร์ดกลไก RGB", "price": 1890, "cost": 1100},
    {"product_id": 102, "title": "เมาส์ไร้สายเสียงเงียบ", "price": 450, "cost": 350},
    {"product_id": 103, "title": "แผ่นรองเมาส์ขนาดใหญ่", "price": 290, "cost": 120}
]
"""

parsed_products = json.loads(internet_data)

for item in parsed_products:
    name = item["title"]
    price = item["price"]
    cost = item["cost"]
    
    profit = price - cost
    margin = (profit / price) * 100
    
    print(f"📡 ตรวจพบสินค้าออนไลน์: {name}")
    print(f"   -> ราคาขาย: {price} บ. / ต้นทุน: {cost} บ.")
    print(f"   -> คำนวณกำไร: {profit} บ. ({margin:.1f}%)")
    
    if margin >= 40:
        print("   🔥 [สินค้าแนะนำ] กำไรสูงมาก รีบดึงข้อมูลด่วน!")
    else:
        print("   💤 [ผ่านก่อน] กำไรไม่ถึงเกณฑ์ 40%")
    print("-" * 40)

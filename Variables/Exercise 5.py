talent_s=float(input("Enter talents"))
pound_s=float(input("Enter pounds"))
lot_s=float(input("Enter lots"))
talents=talent_s*20*32*13.3
pounds=pound_s*32*13.3
lots=lot_s*13.3
total=talents+pounds+lots
kilograms=int(total//1000)
grams=(round(total-kilograms*1000),2)
print("The weight in modern units: ",kilograms,grams )

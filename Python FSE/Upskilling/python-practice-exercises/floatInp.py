# Float Input
def kilogm_to_pound(kg):
    if kg<0 or not isinstance(kg,(int,float)):
        return "invalid input"
    pound = kg*2.20462
    return f"weight in pounds: {pound:.2f}"

kg_weight = float(input("enter weight in kg"))
print(kilogm_to_pound(kg_weight))
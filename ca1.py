# Aine Colhoun 202017097 CA1
# Calculate the surface area, mass and draft of a barge

length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
height = int(input("Enter height: "))

surface_area = (length * breadth) + (2 * length * height) + (2 * breadth * height)

mass = surface_area * 1.06

draft = mass / (length * breadth)

print(f"Surface area = {surface_area: .2f}")
print(f"Mass = {mass: .2f}")
print(f"Draft = {draft: .2f}")

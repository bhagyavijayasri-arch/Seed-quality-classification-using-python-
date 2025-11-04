# Project: Quality Classification of Plant Seeds Using Python

print(" Quality Classification of Plant Seeds ")

# Step 1: Input seed characteristics
weight = float(input("Enter the weight of the seed (in grams): "))
size = float(input("Enter the size of the seed (in mm): "))
color = input("Enter the color of the seed (brown/black/golden): ").lower()
texture = input("Enter the texture of the seed (smooth/rough): ").lower()

# Step 2: Assign scores based on characteristics
score = 0

# Weight
if weight >= 5:
    score += 2
else:
    score += 1

# Size
if size >= 4:
    score += 2
else:
    score += 1

# Color
if color == "brown" or color == "golden":
    score += 2
else:
    score += 1

# Texture
if texture == "smooth":
    score += 2
else:
    score += 1

# Step 3: Classify the seed quality
if score >= 7:
    quality = "High Quality Seed "
elif score >= 5:
    quality = "Medium Quality Seed "
else:
    quality = "Low Quality Seed "

# Step 4: Display result
print("\nFinal Quality Classification →", quality)

"""Expected Output
Quality Classification of Plant Seeds 
Enter the weight of the seed (in grams): 6
Enter the size of the seed (in mm): 5
Enter the color of the seed (brown/black/golden): golden
Enter the texture of the seed (smooth/rough): smooth

Final Quality Classification → High Quality Seed"""
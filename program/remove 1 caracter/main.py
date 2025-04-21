# Read the file
with open('yourfile.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Remove the last character
updated_content = content[:-1]  

# Write the updated content back to the file
with open('yourfile.txt', 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("Last character removed successfully!")

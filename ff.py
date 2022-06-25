import re
result="WaseCaseeowrjiJSKASDeweorw"
re.sub(r"([a-z])([A-Z])", r"\1 \2", result)
print(result)
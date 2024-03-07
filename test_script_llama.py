import ollama

# Test calling the model directly with a sample prompt
response = ollama.generate(model="llama3.1", prompt="What is the capital of France?")
print(response)
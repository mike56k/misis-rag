#!/bin/bash

# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!

# Pause for Ollama to start.
sleep 5

echo "🔴 Retrieve models..."
ollama pull mxbai-embed-large:latest
ollama pull mistral:latest
echo "🟢 Done!"

# Wait for Ollama process to finish.
wait $pid
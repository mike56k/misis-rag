#!/bin/bash
# Start Ollama in the background.
/bin/ollama serve &
# Record Process ID.
pid=$!
# Pause for Ollama to start.
sleep 5
echo "🔴 Retrieve models..."
ollama pull mxbai-embed-large:latest
ollama pull qwen2.5:3b
echo "🟢 Done!"
# Wait for Ollama process to finish.
wait $pid
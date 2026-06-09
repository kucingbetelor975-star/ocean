#!/bin/bash

echo "🔍 Checking if model exists..."

MODEL_PATH="model/model_air.h5"

# Function to check if model is valid
check_model() {
    if [ -f "$MODEL_PATH" ]; then
        FILE_SIZE=$(stat -f%z "$MODEL_PATH" 2>/dev/null || stat -c%s "$MODEL_PATH" 2>/dev/null)
        if [ "$FILE_SIZE" -gt 1000000 ]; then
            echo "✅ Model file exists and is valid (${FILE_SIZE} bytes)"
            return 0
        else
            echo "⚠️  Model file too small (${FILE_SIZE} bytes), probably LFS pointer"
            rm -f "$MODEL_PATH"
            return 1
        fi
    else
        echo "❌ Model file not found"
        return 1
    fi
}

if check_model; then
    echo "✅ Model ready!"
    exit 0
fi

echo "📥 Attempting to download model with Git LFS..."

# Install Git LFS
git lfs install --skip-repo 2>/dev/null || git lfs install 2>/dev/null

# Try to pull the specific file
if git lfs pull --include="model/model_air.h5"; then
    echo "✅ Git LFS pull successful"
    if check_model; then
        echo "✅ Model downloaded successfully!"
        exit 0
    fi
fi

echo "❌ Failed to download model"
echo "⚠️  Application will start without model - predictions will not work"
exit 0

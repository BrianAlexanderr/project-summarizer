# 📝 AI Text Summarizer - Streamlit Application

An interactive web application for automatic text summarization using a fine-tuned T5 transformer model. This application provides a user-friendly interface to generate concise summaries from lengthy texts with advanced features and visualizations.

## 🌟 Features

### Core Features
- **Interactive Text Summarization**: Paste text or choose from sample texts
- **Real-time Processing**: Get summaries instantly with processing time display
- **Advanced Settings**: Customize summary length and beam search parameters
- **Multiple Input Options**: Support for direct text input or sample texts
- **GPU Acceleration**: Automatic GPU support for faster processing

### User Interface Elements
- **📝 Summarize Tab**: Main summarization interface
- **🎯 Sample Texts Tab**: Pre-loaded examples with one-click summarization
- **⚙️ Settings Tab**: Model configuration and system information
- **ℹ️ About Tab**: Detailed information about the application

### Statistics & Analytics
- Original text word count
- Summary word count
- Compression ratio calculation
- Processing time measurement
- Sentence count comparison
- Average word length metrics
- Export options (TXT format)

## 📋 Requirements

- Python 3.8 or higher
- CUDA 11.8+ (optional, for GPU acceleration)
- 4GB RAM minimum (8GB recommended)
- 2GB storage for model files

## 🚀 Installation

### Step 1: Clone or Download the Project
```bash
cd "d:\Kuliah\Semester 5\Deep Learning\project"
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install streamlit torch transformers safetensors numpy protobuf
```

### Step 3: Verify Model Files
Ensure the `model/` directory exists with the following files:
```
model/
├── config.json
├── generation_config.json
├── model.safetensors
├── special_tokens_map.json
├── spiece.model
├── tokenizer_config.json
└── tokenizer.json
```

## 💻 Running the Application

### Option 1: Using Streamlit CLI (Recommended)
```bash
streamlit run app.py
```

### Option 2: Using Python
```bash
python -m streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`

### Option 3: Running on a Specific Port
```bash
streamlit run app.py --server.port 8080
```

### Option 4: Running Without Opening Browser
```bash
streamlit run app.py --logger.level=debug
```

## 🎯 How to Use

### Basic Usage
1. **Choose Input Method**: Select between "Paste Text" or "Sample Text"
2. **Enter Your Text**: Paste your text in the text area
3. **Generate Summary**: Click the "✨ Generate Summary" button
4. **View Results**: See original, summary, and statistics
5. **Export**: Download the summary as a text file

### Advanced Settings
- **Max Summary Length**: Set the maximum words in summary (30-500)
- **Min Summary Length**: Set the minimum words in summary (10-200)
- **Beam Search Width**: Adjust search quality (1-8, higher = better quality but slower)

### Sample Texts
Quick-start with pre-loaded examples:
- Technology & AI
- Climate Change
- Space Exploration
- Health & Wellness

## 🧠 Model Details

### Architecture
- **Model Type**: T5 (Text-To-Text Transfer Transformer)
- **Task**: Abstractive Text Summarization
- **Hidden Size**: 768
- **Number of Layers**: 12 (encoder) + 12 (decoder)
- **Attention Heads**: 12
- **Vocabulary Size**: 32,128 tokens
- **Max Sequence Length**: 512 tokens

### Summarization Parameters
- **Prefix**: "summarize: " (task-specific prefix)
- **Early Stopping**: Enabled
- **Length Penalty**: 2.0 (encourages longer summaries)
- **No Repeat N-grams**: 3 (prevents repetition)
- **Num Beams**: 4 (default, customizable)

## 📊 Statistics Explained

### Compression Ratio
Percentage of text reduced:
```
Compression = (1 - summary_words / original_words) × 100
```

### Processing Time
Time taken to generate the summary (varies by device and text length)

### Sentences Reduction
Comparison of sentence count before and after summarization

## 🖥️ System Requirements

### Minimum
- CPU: 4 cores
- RAM: 4GB
- Storage: 3GB (model + application)

### Recommended
- CPU: 8+ cores or GPU
- RAM: 8GB+
- Storage: 5GB
- GPU: NVIDIA CUDA-capable GPU

## 🔧 Troubleshooting

### Issue: Model Takes Too Long to Load
**Solution**: First-time loading may take 2-5 minutes. Subsequent loads use caching.

### Issue: Out of Memory Error
**Solution**: 
- Close other applications
- Reduce summary length
- Increase RAM allocation if possible

### Issue: CUDA Out of Memory
**Solution**:
- The app will automatically fall back to CPU
- Reduce batch processing size
- Restart the application

### Issue: Port Already in Use
**Solution**: Use a different port
```bash
streamlit run app.py --server.port 8080
```

### Issue: Model Files Not Found
**Solution**: Verify the `model/` directory contains all required files

## 🎨 Customization

### Change Default Parameters
Edit the default values in the main tab settings:
```python
max_length = st.slider("Max Summary Length (words):", 30, 500, 150, step=10)
min_length = st.slider("Min Summary Length (words):", 10, 200, 30, step=5)
num_beams = st.slider("Beam Search Width:", 1, 8, 4, step=1)
```

### Add Custom Sample Texts
Update the `SAMPLE_TEXTS` dictionary:
```python
SAMPLE_TEXTS = {
    "Your Category": "Your text here...",
    # ... other texts
}
```

### Modify Styling
Customize CSS in the style section:
```html
<style>
    /* Add your custom CSS here */
</style>
```

## 📈 Performance Tips

1. **Use GPU**: If available, the app automatically uses GPU for faster processing
2. **Optimal Beam Size**: Use 4-6 for balance between quality and speed
3. **Text Length**: Shorter texts process faster (optimal: 100-500 words)
4. **Cache Utilization**: Model is cached after first load

## 🌐 Deployment

### Local Network Access
```bash
streamlit run app.py --server.address 0.0.0.0
```

### Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]
```

Build and run:
```bash
docker build -t summarizer-app .
docker run -p 8501:8501 summarizer-app
```

## 📝 Example Usage

### Command Line
```bash
# Basic run
streamlit run app.py

# Run on specific port
streamlit run app.py --server.port 9000

# Run with logger debug
streamlit run app.py --logger.level=debug
```

### Access Points
- Local: `http://localhost:8501`
- Custom Port: `http://localhost:XXXX` (replace XXXX with your port)
- Network: `http://<your-ip>:8501`

## 🔐 Security Considerations

- Model files are served locally
- No data is sent to external servers
- All processing happens on your machine
- User inputs are not stored

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [T5 Model Paper](https://arxiv.org/abs/1910.10683)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)

## 🤝 Contributing

Feel free to suggest improvements or report issues!

## 📄 License

This project is created for educational purposes.

---

**Built with 💙 for Deep Learning Project | Semester 5**

*Last Updated: December 3, 2025*

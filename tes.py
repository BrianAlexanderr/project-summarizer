from huggingface_hub import login, upload_folder

# (optional) Login with your Hugging Face credentials
login()

# Push your model files
upload_folder(folder_path="model", repo_id="BrianAlex1/t5-summarizer-news", repo_type="model")

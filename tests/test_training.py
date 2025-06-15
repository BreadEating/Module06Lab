def test_model_training():
    # Quick test of "train.py"
    import subprocess
    result = subprocess.run(["python", "train.py"], capture_output=True)
    assert result.returncode == 0, "Training script failed!"
from revoltutils import ProgressBar
import time

def test_progress_bar():
    total = 5
    print("[*] Starting ProgressBar test...")
    
    bar = ProgressBar(total=total, title="Test Progress")
    bar.start()

    try:
        for i in range(total):
            time.sleep(0.2)  # Simulate work
            bar.update()
        print("[✓] ProgressBar updated successfully.")
    except Exception as e:
        print(f"[✗] Error during progress update: {e}")
        raise
    finally:
        bar.close()
        print("[✓] ProgressBar closed cleanly.")

if __name__ == "__main__":
    test_progress_bar()
    print("[*] ProgressBar test completed.")
